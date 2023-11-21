use std::io;
fn main() {
    let args: Vec<String> = std::env::args().collect();
    //println!("{:?}", args);

    if args.len() == 4{
        let a: u32 = args[2].parse().unwrap();
        let b: u32 = args[3].parse().unwrap();
    
        match args[1].as_str() {
            "+" => println!("{} + {} = {:?}",a, b, add(a, b)),//.unwrap()),
            "-" => println!("{} + {} = {:?}",a, b, sub(a, b)),//.unwrap()),
            "/" => match div(a,b){
                Ok(result) => println!("{} + {} = {:?}",a, b, result), // on extraie la valeur contenue dans le Ok avec :? vu que c'est de type u32
                Err(err) => println!("Error: {}", err),
            },
            "*" => println!("{} + {} = {:?}", a, b, mult(a, b)),//.unwrap()),
            _ => panic!("Operator not recognized"),
        }
    } 
}

fn add(a:u32, b:u32)->Result<u32,String>{
    Ok(a + b)
}

fn sub(a:u32, b:u32)->Result<u32,String>{
    Ok(a - b)
}

fn div(a:u32, b:u32)->Result<u32,String>{
    if b == 0{
        Err("Cannot divide by zero".to_string())
    }else{
       Ok(a / b) 
    }
    
}

fn mult(a:u32, b:u32)->Result<u32,String>{
    Ok(a * b)
}