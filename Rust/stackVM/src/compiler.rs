use crate::instruction::Instruction;
use bincode;
use std::fs::{self, File};
use std::io::{self, Write};
use std::slice::Split;

fn parse_instruction(input: &str) -> Instruction {
    let mut tokens = input.split_whitespace(); // Ou input.split(" ") si vous voulez diviser par des espaces

    if let Some(token) = tokens.next() {
        let lowercase_token = token.to_lowercase();
        match lowercase_token.as_str() {
            "push" => {
                if let Some(value_str) = tokens.next() {
                    // Tentative de conversion de la chaîne en u32
                    if let Ok(value) = value_str.parse::<u32>() {
                        //println!("IN PUSH: {:?}", value);
                        Instruction::Push(value)
                    } else {
                        // Gestion d'une erreur de conversion
                        println!("Error parsing value in PUSH");
                        Instruction::Unknow
                    }
                } else {
                    // Gestion du cas où il manque la valeur après PUSH
                    println!("Error: Missing value after PUSH");
                    Instruction::Unknow
                }
            },
            "pop" => Instruction::Pop,
            "dup" => Instruction::Dup,
            "swap" => Instruction::Swap,
            "add" => Instruction::Add,
            "sub" => Instruction::Sub,
            "mul" => Instruction::Mul,
            "div" => Instruction::Div,
            "in" => Instruction::In,
            "out" => Instruction::Out,
            "outc" => Instruction::OutC,
            "jmp" => {
                //if let Some(number_token: &str) = tokens.next();
                Instruction::Jmp(0)
            },
            "jz" => Instruction::Jz(0),
            "jnz" => Instruction::Jnz(0),
            "halt" => Instruction::Halt,
            _ => Instruction::Unknow,
        }
    } else {
        Instruction::Unknow
    }
}

pub fn compile(input_filename: &str) -> io::Result<()> {
    // Lire le contenu du fichier en tant que chaîne de caractères
    let content = fs::read_to_string(input_filename)?;

    // Initialiser un vecteur pour stocker les instructions
    let mut instructions: Vec<Instruction> = Vec::new();

    // Diviser la chaîne en lignes et itérer sur les lignes
    for line in content.lines() {
        // Traiter chaque ligne en convertissant la chaîne en instruction
        let instruction = parse_instruction(line);

        // Ajouter l'instruction au vecteur
        instructions.push(instruction);
    }

    print!("{:?}", instructions);

    // Sérialiser le vecteur d'instructions en bytes
    let encoded_data = bincode::serialize(&instructions).map_err(|e| {
        io::Error::new(io::ErrorKind::InvalidData, format!("Failed to serialize instructions: {}", e))
    })?;
    // Écrire les bytes sérialisés dans un fichier binaire
    let output_filename = format!("{}.bin", input_filename);
    let mut file = File::create(&output_filename)?;
    file.write_all(&encoded_data)?;

    Ok(())
}