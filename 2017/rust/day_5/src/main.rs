use std::fs;

fn main() {
    let file_name = "input.txt";
    let input = fs::read_to_string(file_name).expect("Error reading file");
    let mut jumps: Vec<i32> = input.lines().map(|x| x.parse::<i32>().unwrap()).collect();
    let mut jumps2 = jumps.clone();

    // solve part 1

    solve_part_1(&mut jumps);

    // solve part 2

    solve_part_2(&mut jumps2);
}

fn solve_part_1(jumps: &mut Vec<i32>) {
    let mut steps = 0;
    let mut index = 0;
    let mut jump: i32;

    while index < jumps.len() {
        jump = jumps[index];
        jumps[index] += 1;
        index = (index as i32 + jump) as usize;
        steps += 1;
    }

    println!("Part 1: {}", steps);
}

fn solve_part_2(jumps: &mut Vec<i32>) {
    let mut steps = 0;
    let mut index = 0;
    let mut jump: i32;

    while index < jumps.len() {
        jump = jumps[index];

        jumps[index] = if jump >= 3 { jump - 1 } else { jump + 1 };
        index = (index as i32 + jump) as usize;
        steps += 1;
    }

    println!("Part 1: {}", steps);
}
