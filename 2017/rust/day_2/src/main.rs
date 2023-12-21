use std::fs::File;
use std::io::{self, BufRead};

fn main() {
    let file_name = "input.txt"; // Replace with your file name

    // Open the file
    let file = File::open(file_name).expect("Failed to open file");

    // Create a buffered reader
    let reader = io::BufReader::new(file);

    let mut sum_part1 = 0;
    let mut sum_part2 = 0;


    // Iterate over each line
    for line in reader.lines() {

        let line = line.expect("Error reading line").trim().to_string();
        let numbers: Vec<u32> = line
                                .split('\t')
                                .map(|s| s.parse::<u32>().expect("Parse error"))
                                .collect();


        sum_part1 += solve_part_1(&numbers);
        sum_part2 += solve_part_2(&numbers);
        

        
        

    }

    println!("Part 1: {}", sum_part1);
    println!("Part 2: {}", sum_part2);

}

fn solve_part_1(numbers: &Vec<u32>) -> u32 {
    let mut difference = 0;
    if let (Some(max), Some(min)) = (numbers.iter().max(), numbers.iter().min()) {
        difference = max - min;
    }

    difference
}


fn solve_part_2(numbers: &Vec<u32>) -> u32 {
    let mut sum = 0;
    for i in 0..numbers.len() {
        for j in 0..numbers.len() {
            if i != j {
                if numbers[i] % numbers[j] == 0 {
                    sum += numbers[i] / numbers[j];
                }
            }
        }
    }
    sum
}