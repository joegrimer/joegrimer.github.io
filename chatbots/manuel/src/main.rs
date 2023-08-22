/*
Goal - an old fashioned chatbot, that's manually written, and not too clever

Thoughts:
One problem with chatbots is that there are two different parts: Understanding, and responding. "Hello" has no obvious response. Perhaps I only care about the imperative

Next:
text print subject and predicate for debug purposes
I don't understand should be: Please ask me an imperative roodly

*/


use std::time::{SystemTime, UNIX_EPOCH};
use std::collections::HashMap;

//create a dictionary of strings
static ROBOT_NAME: &str = "Manuel";
static USER_NAME: &str = "Joseph";

fn secs_str() -> String {
    return SystemTime::now().duration_since(UNIX_EPOCH).expect("Time went backwards").as_secs().to_string();
}

fn main() {
    use std::fs::OpenOptions;
    use std::io::prelude::*;

    //: HashMap<String, String> = 
    let mut memory = HashMap::new();

    let mut transcript_file = OpenOptions::new()
        .write(true)
        .append(true)
        .create(true)
        .open("chatlog.txt")
        .unwrap();
    print!("You are through to Manuel. You talk first");
    loop {
        // let mut user_input = String::new();
        let user_input = "a poem is a collection of words woven together";
        print!("\n:");
        // let _ = io::stdout().flush();
        // io::stdin().read_line(&mut user_input).expect("Error reading from STDIN");
        let user_line = USER_NAME.to_owned() + " " + &secs_str() + ": " + &user_input;
        print!("{}", user_line);

        let manuel_res = respond_to(memory, user_input);
        let manuel_line = ROBOT_NAME.to_owned() + " " + &secs_str() + ": " + &manuel_res;
        print!("{}", manuel_line);

        if let Err(e) = writeln!(transcript_file, "{}{}", user_line, manuel_line) {
            eprintln!("Couldn't write to file: {}", e);
        }
        break;
    }
    print!("\nEnd");
}

fn write_story() -> String {
    return "Once upon a time there was a dog. The dog died at the end\n".to_string();
}

fn write_poem() -> String {
    return "I live here in australia\nand I like Kagaroos\nHee Hay!\n".to_string();
}

fn remember(memory: &HashMap<String, String>, word: &String, definition: &String) {
    *memory.insert(
        word.clone(),
        definition.clone());
}

fn define(memory: &HashMap<String, String>, word: &String) -> String {
    let definition;
    if memory.contains_key(word) {
        definition = memory[word].to_string();
    } else {
        return format!("I am sorry. I do not know what {} means. Please define it for me", word)
    }
    return format!("{}: {}", word, definition);
}

fn respond_to(memory: HashMap<String, String>, input: &str) -> String{

    // rudimentary normalising
    let linput = input.to_lowercase();
    let words = linput.split(' ');

    let mut verb: String = "".to_string();
    let mut predicate: String = "".to_string();
    // let mut indirect_object: String = "".to_string();
    let mut subject: String = "".to_string();

    for (_, word) in words.enumerate() {
        // println!("{}-", word);
        if verb.len() == 0 && ["is","read","write"].contains(&word){
            verb = word.to_string();
        } else if verb.len() == 0 {
            if subject.len() != 0 {
                subject = format!("{} {}", subject,  word);
            } else {
                subject = word.to_string();
            }
        } else {
            if predicate.len() != 0 {
                predicate = format!("{} {}", predicate,  word);
            } else {
                predicate = word.to_string();
            }
        }
    }
    println!("sub: {} verb: {} dobj: {}", subject, verb, predicate);

    // imperative_switchboard
    if verb == "is" {
        remember(&memory, &subject, &predicate);
    } if verb == "write" {
        if predicate == "story" {
            return write_story();
        } else if predicate == "poem" {
            return write_poem();
        }
    } else if verb == "define" {
        return define(&memory, &predicate);
    }

    return "I don't understand".to_string();
}