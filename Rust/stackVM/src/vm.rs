use crate::{instruction::Instruction, stack::Stack};
use std::io::stdin;

pub struct Vm{
    // program counter
    pc: usize,
    instructions: Vec<Instruction>,
    stack: Stack
}

impl Vm {
    pub fn new(instructions: Vec<Instruction>) -> Self{
        Vm {
            pc: 0,
            instructions,
            stack: Stack::new(),
        }
    }

    pub fn run(&mut self){
        while self.pc < self.instructions.len() {

            match self.instructions[self.pc] {
                Instruction::Push(value) => self.stack.push(value),
                Instruction::Pop => {
                    let _ret: Option<u32> = self.stack.pop();
                },
                Instruction::Dup => {
                    let n: &u32 = self.stack.peek().expect("Peeked on an empty stack !");
                },
                Instruction::Swap => {
                    let a = self.stack.pop().expect("Popped on an empty stack !");
                    let b = self.stack.pop().expect("Popped on an empty stack !");
                    self.stack.push(a);
                    self.stack.push(b);
                },
                Instruction::Out => {
                    let n = self.stack.peek().expect("Peeked on an empty stack !");
                    println!("{}", n);
                },
                Instruction::OutC => {
                    let n = self.stack.peek().expect("Peeked on an empty stack !");
                    if let Some(c) = std::char::from_u32(*n){
                       println!("{}", n); 
                    } else{
                        println!("{}", n);
                    }
                },
                Instruction::Add => {
                    let a = self.stack.pop().expect("Popped on an empty stack !");
                    let b = self.stack.pop().expect("Popped on an empty stack !");
                    self.stack.push(a+b);
                },
                Instruction::Sub => {
                    let a = self.stack.pop().expect("Popped on an empty stack !");
                    let b = self.stack.pop().expect("Popped on an empty stack !");
                    self.stack.push(a-b);
                },
                Instruction::Mul => {
                    let a = self.stack.pop().expect("Popped on an empty stack !");
                    let b = self.stack.pop().expect("Popped on an empty stack !");
                    self.stack.push(a*b);
                },
                Instruction::Div => {
                    let a = self.stack.pop().expect("Popped on an empty stack !");
                    let b = self.stack.pop().expect("Popped on an empty stack !");
                    self.stack.push(a/b);
                },
                Instruction::In => {
                    println!("Entrez un nombre :");
                    let mut input = String::new();
                    // Lecture de la ligne stdin
                    stdin().read_line(&mut input).expect("Échec de la lecture de la ligne");

                    // Trim pour supprimer les espaces et les sauts de ligne
                    // Conversion de la chaîne en u32
                    let number: u32 = input.trim().parse().expect("Impossible de convertir en nombre");
                    self.stack.push(number);
                },
                Instruction::Jmp(n) => {
                    if n as usize >= self.instructions.len(){
                        panic!("Jump to unknown instructions");
                    } else{
                        self.pc = n as usize;
                        continue;;
                    }
                },
                Instruction::Jz(n) => {
                    if n as usize >= self.instructions.len(){
                        panic!("Jump to unknown instructions");
                    } else{
                        if self.stack.peek() == Some(&0){
                            self.pc = n as usize;
                            continue;
                        }
                    }
                },
                Instruction::Jnz(n) => {
                    if n as usize >= self.instructions.len(){
                        panic!("Jump to unknown instructions");
                    } else{
                        if self.stack.peek() != Some(&0){
                            self.pc = n as usize;
                            continue;
                        }
                    }
                },
                Instruction::Halt => {
                    std::process::exit(0)
                },
                Instruction::Unknow => panic!("Instruction unknow, panicking!"),
            }
            self.pc += 1;
        }
    }
}

#[cfg(test)]
mod tests{
    use crate::disassemble::disassemble;

    use super::Vm;

    #[test]
    fn test_basic_instruction(){
        let instructions = disassemble("steps/step7_2.bin").unwrap();
        let mut vm = Vm::new(instructions);
        vm.run();
    }
    #[test]
    fn test_complexe_instruction(){
        let instructions = disassemble("steps/step7_3.bin").unwrap();
        let mut vm = Vm::new(instructions);
        vm.run();
    }
    // Quand je retire ce 3ème test ça permet au deuxième de s'exéécuter ... Mais quand je le laisse ni la 3eme ni la 2eme ne semblent fonctionner
    #[test]
    fn test_jump_instruction(){
        let instructions = disassemble("steps/step7_4.bin").unwrap();
        let mut vm = Vm::new(instructions);
        vm.run();
    }
}