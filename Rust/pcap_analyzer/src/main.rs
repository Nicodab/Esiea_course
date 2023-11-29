use pcap::Capture;
use packet::Packet;
use dns_parser;

const DNS_PORT: u16 = 53;

fn main() {
    // Remplacez "your_file.cap" par le chemin de votre fichier .cap
    let file_path = "dns.cap";

    // Ouvrez le fichier .cap
    if let Ok(mut cap) = Capture::from_file(file_path) {
        println!("File opened successfully.");

        // Capture et imprime chaque paquet
        while let Ok(packet) = cap.next_packet() {
            //println!("Packet: {:?}", packet);
            let eth_packet = packet::ether::Packet::new(packet.data).unwrap();
            let ip_packet = packet::ip::v4::Packet::new(eth_packet.payload()).unwrap();
            let udp_packet = packet::udp::Packet::new(ip_packet.payload()).unwrap();

            if udp_packet.source() == DNS_PORT || udp_packet.destination() == DNS_PORT {
                if let Ok(dns_packet) = dns_parser::Packet::parse(udp_packet.payload()){
                    for question in dns_packet.questions {
                        println!("Question: {:?}", question.qname);
                    }
                }
            }
        }
    } else {
        eprintln!("Error opening the file.");
    }
}
