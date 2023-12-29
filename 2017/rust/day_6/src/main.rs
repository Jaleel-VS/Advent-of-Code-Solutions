use std::collections::HashSet;
use std::collections::HashMap;
use std::fs;

fn main() {
    let mut states: HashSet<String> = HashSet::new();

    let mut numbers = extract_string_and_get_vector();

    let mut count = 0;

    loop {
        let numbers_string: String = numbers
            .iter()
            .map(|&n| n.to_string())
            .collect::<Vec<String>>()
            .join(" ");

        if states.contains(&numbers_string) {
            break;
        } else {
            states.insert(numbers_string);
            redistribute_blocks(&mut numbers);
            count += 1;
        }
    }

    print!("Part 1 Solution: ");

    println!("Number of cycles: {}", count);

    print!("Part 2 Solution: ");

    solve_part_2();
}


// PART 1

fn extract_string_and_get_vector() -> Vec<u32> {
    let contents = fs::read_to_string("input.txt").expect("Failed to read file");

    let numbers = contents
        .split_whitespace()
        .filter_map(|s| s.parse::<u32>().ok())
        .collect();

    numbers
}

fn redistribute_blocks(numbers: &mut Vec<u32>) {
    let mut max = 0;
    let mut index = 0;

    // Find the max value and its index
    for (i, &num) in numbers.iter().enumerate() {
        if num > max {
            max = num;
            index = i;
        }
    }

    // Set the value at the index to 0
    numbers[index] = 0;

    let numbers_len = numbers.len();

    // Redistribute the blocks
    for i in 0..max {
        numbers[(index + 1 + i as usize) % numbers_len] += 1;
    }

    // No return statement needed
}


// PART 2

fn solve_part_2() {
    let mut states_map: HashMap<String, u32> = HashMap::new();

    let mut numbers = extract_string_and_get_vector();

    let mut count = 0;

    let mut numbers_string;

    loop {
        numbers_string = numbers
            .iter()
            .map(|&n| n.to_string())
            .collect::<Vec<String>>()
            .join(" ");

        if states_map.contains_key(&numbers_string) {
            break;
        } else {
            states_map.insert(numbers_string, count);
            redistribute_blocks(&mut numbers);
            count += 1;
        }
    }

    let first_index = states_map.get(&numbers_string).unwrap();
    let last_index = count;

    println!("Number of cycles: {}", last_index - first_index);
}