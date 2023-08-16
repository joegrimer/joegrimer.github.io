fn rays(x: u32, y: u32) -> char{
    if x % y == 0 {return 'X';}
    if (x+1) % y == 0 {return ')';}
    if (x-1) % y == 0 {return '(';}
    if x % (y+1) == 0 {return 'n';}
    if x % (y-1) == 0 {return 'u';}
    return ' ';
}

fn huhA(x: u32, y: u32) -> char{
    if (x*y)%12 == 0 {return 'X';}
    return ' ';
}

fn huhB(x: u32, y: u32) -> char{
    if (x*y)%12 == 6 {return 'X';}
    return ' ';
}

fn huhAB(x: u32, y: u32) -> char{
    if (x*y)%12 == 0 {return 'x';}
    if (x*y)%12 == 6 {return 'o';}
    return ' ';
}

fn huhC(x: u32, y: u32) -> char{
    if (x.pow(y%5)) % 3 == 0 {return 'x';}
    return ' ';
}

fn main() {
    for y in 1..56 {
        for x in 1..178 {
            print!("{}", huhC(x, y));
            // print!("{}", rays(x, y));
        }
        print!("\n");
    }
}
