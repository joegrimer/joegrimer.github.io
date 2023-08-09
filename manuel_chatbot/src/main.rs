/*
Goal - an old fashioned chatbot, that's manually written, and not too clever

Thoughts:
One problem with chatbots is that there are two different parts: Understanding, and responding. "Hello" has no obvious response. Perhaps I only care about the imperative

Next:
text print subject and predicate for debug purposes
I don't understand should be: Please ask me an imperative roodly

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
        break;
    }
    print!("End");
}

fn write_story() -> &'static str {
    return "Once upon a time there was a dog. The dog died at the end";
}

fn respond_to(input: String) -> &'static str{

    // rudimentary normalising
    input.to_lowercase();

    

    // let words = input.split(' ');
    // println!("{:?}", words);
    // let first_word = words.next();
    // println!("{:?}", first_word);
    // let mut predicate = String::new();


    // for (i, word) in words.iter().enumerate() {
    //     println!("{}-", word);
    //     if i == 0 {
    //         first_word = word;
    //     } else {
    //         predicate.push_str(word);
    //     }
    // }
    // println!("fw: {} pr: {}", first_word, predicate);

    // // imperative_switchboard
    // if first_word == "tell" {
    //     if predicate == "story" {
    //         return write_story();
    //     }
    // }
    return "I don't understand"
}