use std::fs;
use regex::Regex;
use std::time::{Duration, Instant};

fn main() {
    let start = Instant::now();
    without_threads("dataRust/data.json");
    let duration = start.elapsed();
    println!("{:?}", duration);
}

fn without_threads(path: &str) {
    // Load the file
    let content = fs::read_to_string(path).expect("Erreur lors de la lecture du fichier");

    // Liste des motifs regex à rechercher
    let patterns = vec![
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}", // Email pattern
        r"\+?\d[\d -]{8,12}\d",                            // Phone pattern
    ];

    // Compter les correspondances pour chaque motif
    for pattern in patterns {
        let regex = Regex::new(pattern).expect("Erreur lors de la création de l'objet Regex");

        let matches_count = regex.find_iter(&content).count();

        println!("Nombre de correspondances pour le motif '{}': {}", pattern, matches_count);
    }
}
