// src/disassemble.rs
use bincode;
use std::fs::File;
use std::io::{self, Read};
use std::path::Path;
use crate::instruction::{Instruction, self};

pub fn disassemble(filename: &str) -> io::Result<Vec<Instruction>> {
    let path = Path::new(filename);
    let mut file = File::open(&path)?;

    let mut buffer = Vec::new();
    file.read_to_end(&mut buffer)?;

    // Utilisez `map_err` pour convertir l'erreur de bincode en une erreur de std::io
    let instructions: Vec<Instruction> = bincode::deserialize(&buffer).map_err(|e| {
        io::Error::new(
            io::ErrorKind::InvalidData,
            format!("Failed to deserialize: {}", e),
        )
    })?;
    Ok(instructions)
}

pub fn pretty_print(instructions: &Vec<Instruction>) {
    for instruction in instructions{
        println!("{:?}", instruction);
    }
}

#[cfg(test)]
mod tests{
    use crate::instruction::Instruction;

    use super::disassemble;

    #[test]
    fn deserialization(){
        let instructs : std::io::Result<Vec<Instruction>> = disassemble("fuzzinglabs.bin");
    }

    /*#[test]
    fn serialization(){
        let instructs:std::io::Result<Vec<Instruction>>  = [Push(70),
        OutC,
        Push(117),
        OutC,
        Push(122),
        OutC,
        Push(122),
        OutC,
        Push(105),
        OutC,
        Push(110),
        OutC,
        Push(103),
        OutC,
        Push(108),
        OutC,
        Push(97),
        OutC,
        Push(98), OutC, Push(115), OutC]
    }*/
}
