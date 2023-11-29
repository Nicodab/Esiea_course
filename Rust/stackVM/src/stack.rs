#[derive(Debug)]
pub struct Stack {
    items: Vec<u32>,
}

impl Stack {
    pub fn new() -> Self {
        Stack { items: Vec::new() }
    }

    pub fn push(&mut self, value: u32) {
        self.items.push(value);
    }

    pub fn pop(&mut self) -> Option<u32> {
        self.items.pop()
    }

    pub fn peek(&self) -> Option<&u32> {
        self.items.last()
    }
}

#[cfg(test)]
mod tests{
    use super::Stack;

    #[test]
    fn test_stack(){
        let mut stack = Stack::new();
        stack.push(1);
        stack.push(2);
        stack.pop();
        assert_eq!(Some(1), stack.peek().copied()) // on copie le nombre en soit et donc sa valeur, si on retire le copied ça renvoie la référence du nombre car la fonction peek renvoie une référence sur le nb
    }
}
