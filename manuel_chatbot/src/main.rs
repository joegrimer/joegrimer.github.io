/*
Goal - an old fashioned chatbot, that's manually written, and not too clever

Next:
*/


use std::io::{self}; // , Write
use std::time::{SystemTime, UNIX_EPOCH};
// use std::time::Duration;

static ROBOT_NAME: &str = "Manuel";
static USER_NAME: &str = "Joseph";

fn secs_str() -> String {
    return SystemTime::now().duration_since(UNIX_EPOCH).expect("Time went backwards").as_secs().to_string();
}

fn main() {
    use std::fs::OpenOptions;
    use std::io::prelude::*;

    let mut transcript_file = OpenOptions::new()
        .write(true)
        .append(true)
        .create(true)
        .open("chatlog.txt")
        .unwrap();
    print!("You are through to Manuel. You talk first");
    loop {
        let mut user_input = String::new();
        print!("\n:");
        let _ = io::stdout().flush();
        io::stdin().read_line(&mut user_input).expect("Error reading from STDIN");
        let user_line = USER_NAME.to_owned() + " " + &secs_str() + ": " + &user_input;
        print!("{}", user_line);

        let manuel_res = respond_to(user_input);
        let manuel_line = ROBOT_NAME.to_owned() + " " + &secs_str() + ": " + &manuel_res;
        print!("{}", manuel_line);

        if let Err(e) = writeln!(transcript_file, "{}{}", user_line, manuel_line) {
            eprintln!("Couldn't write to file: {}", e);
        }
    }
    print!("End");
}

fn respond_to(input: String) -> &'static str{
    return "I don't understand"
}