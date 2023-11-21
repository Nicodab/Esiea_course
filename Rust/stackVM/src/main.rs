// src/main.rs
mod instruction;
mod disassemble;
use clap::{Parser, ValueEnum};
mod compiler;

#[derive(Debug, Copy, Clone, PartialEq, Eq, PartialOrd, ValueEnum)]
enum Mode{
    Disassembler,
    Compiler
}

#[derive(Parser, Debug)]
#[command(author, version, about, long_about = None)]
struct Args{
    #[arg(short, long)]
    inputfile: String,

    #[arg(short, long)] // Permet de mettre -m ou bine --mode
    mode: Mode, // Pas une string
}

fn main() {
    
    let args = Args::parse();
    println!("input: {}", args.inputfile);
    println!("mode: {:?}", args.mode);

    //let output_filename = "output.bin";

    let args: Args = Args::parse();

    match args.mode {
        Mode::Disassembler => {
            // Utilisez un match pour traiter le résultat de la fonction disassemble
            match disassemble::disassemble(&args.inputfile) {
                Ok(instructions) => {
                    // Affichez les instructions désassemblées
                    disassemble::pretty_print(&instructions);
                }
                Err(e) => {
                    eprintln!("Error during disassembly: {}", e);
                }
            }
        },
        Mode::Compiler => {
            match compiler::compile(&args.inputfile) {
                Ok(()) => {
                    println!("Serialization successful.");
                }
                Err(e) => {
                    eprintln!("Error during serialization: {}", e);
                }
            }
        }
    }
}
