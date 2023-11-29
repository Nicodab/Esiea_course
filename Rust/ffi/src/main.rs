use libc::c_int;
use std::ffi::CString;
use std::os::raw::c_char;
// Prog pour utiliser des fonctions C de libc
// On peut accéder au C grâce au FFI
extern "C" {
    fn atoi(s: *const c_char) -> c_int; // On dit au compilateur qu'on veut utiliser une fonction en C et on donne sa signature ici
}

fn main() {
    let s = CString::new("123").unwrap();
    let n = unsafe {atoi(s.as_ptr())};
    println!("{}", n)
}
