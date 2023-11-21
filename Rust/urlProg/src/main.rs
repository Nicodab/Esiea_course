use url::Url;

fn main() {
    let args: Vec<String> = std::env::args().collect();
    
    if args.len() == 2 {
        match Url::parse(&args[1]) {
            Ok(url) => {
                println!("Scheme: {}", url.scheme());

                if let username = url.username() {
                    println!("Username: {}", username);
                } else {
                    println!("Username: None");
                }

                println!("Password: {}", url.password().unwrap_or_default());
                println!("Host String: {}", url.host_str().unwrap_or_default());

                match url.host() {
                    Some(host) => println!("Host: {:?}", host),
                    None => println!("Host: None"),
                }

                match url.port() {
                    Some(port) => println!("Port: {:?}", port),
                    None => println!("Port: None"),
                }

                println!("Path: {}", url.path());
                println!("Query: {:?}", url.query());
                println!("Fragment: {:?}", url.fragment());
                println!("Cannot Be a Base: {:?}", url.cannot_be_a_base());
            }
            Err(e) => {
                eprintln!("Error parsing URL: {:?}", e);
            }
        }
    }
}
