use serde::{Deserialize, Serialize};
// Instriuction that the virtual machine is able to understand
#[derive(Serialize, Deserialize, PartialEq, Debug)]

pub enum Instruction{
    Push(u32),
    Pop,
    Dup, // Duplicate the top pof the stack
    Swap, // Swap the twoi values at the top of the stack
    
    Add,
    Sub,
    Mul,
    Div,

    In, // Read number from stdin
    Out, // Print u32
    OutC, // Print char if possible

    Jmp(u32), // Jump to instruction
    Jz(u32), // Jump to instruction if top of stack is 0
    Jnz(u32), // Jump to instructions if top of stack is not 0

    Halt, // Stop the vm

    Unknow,
}

