# Script that creates C# and Python templates for a given day and year for Adevent of Code

import os
import sys

valid_years = list(range(2015, 2024))
valid_days = list(range(1, 26))

YEAR = None
DAY = None

def get_user_input():
    year = input("Enter year: ")
    while not year.isdigit() or int(year) not in valid_years:
        year = input("Enter year: ")

    day = input("Enter day: ")
    while not day.isdigit() or int(day) not in valid_days:
        day = input("Enter day: ")

    global YEAR
    YEAR = int(year)

    global DAY
    DAY = int(day)

def create_csharp_template(year, day):
    csproj = '''<Project Sdk="Microsoft.NET.Sdk">

<PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net7.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
</PropertyGroup>

</Project>
    '''

    source_code = '''class Program
{
    static void Main(string[] args)
    {
        string inputPath = Path.Combine(Directory.GetCurrentDirectory(), "..", "..", "input.txt");

        // Check if the input file exists
        if (!File.Exists(inputPath))
        {
            Console.WriteLine("Input file not found.");
            return;
        }
    }
}
    '''

    for part in range(1, 3):
        #  write project file 
        with open(f"{year}/day_{day}/part_{part}/csharp/csharp.csproj", "w") as f:
            f.write(csproj)
        
        # write source code
        with open(f"{year}/day_{day}/part_{part}/csharp/Program.cs", "w") as f:
            f.write(source_code)

def create_python_template(year, day):
    source_code = '''import os
INPUT_PATH = None



if __name__ == "__main__":
    INPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "input.txt")

    # Check if the input file exists
    if not os.path.exists(INPUT_PATH):
        print("Input file not found.")
        exit()

    '''

    for part in range(1, 3):
        # write source code
        with open(f"{year}/day_{day}/part_{part}/python/solution.py", "w") as f:
            f.write(source_code)

def create_directories(year, day):
    for part in range(1, 3):
        try:
            os.makedirs(f"{year}/day_{day}/part_{part}/csharp")
            os.makedirs(f"{year}/day_{day}/part_{part}/python")
        except OSError as e:
            print(f"Direcotry {e.filename} already exists.")


if __name__ == "__main__":
    get_user_input()
    create_directories(YEAR, DAY)
    create_csharp_template(YEAR, DAY)
    create_python_template(YEAR, DAY)
            

    

