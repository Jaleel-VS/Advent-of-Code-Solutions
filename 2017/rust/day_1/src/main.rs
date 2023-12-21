use std::fs;

fn main() {
    let file_name = "input.txt";
    let input = fs::read_to_string(file_name).expect("Error reading file");
    let digits: Vec<u32> = input
                            .chars()
                            .map(|c| c.to_digit(10).expect("Not a digit"))
                            .collect();

    // solve part 1
    let sum = solve_part_1(&digits);
    println!("Part 1: {}", sum);

    // solve part 2
    let sum = solve_part_2(&digits);
    println!("Part 2: {}", sum);



}

fn solve_part_1(digits: &Vec<u32>) -> u32 {
    let mut sum = 0;
    
    for i in 0..digits.len() {
        let next = (i + 1) % digits.len();
        if digits[i] == digits[next] {
            sum += digits[i];
        }
    }
    sum
}

fn solve_part_2(digits: &Vec<u32>) -> u32 {
    let mut sum = 0;
    let len = digits.len();

    for i in 0..len{
        let next = (i + len/2) % len;
        if digits[i] == digits[next] {
            sum += digits[i];
        }
    }
    sum
}
