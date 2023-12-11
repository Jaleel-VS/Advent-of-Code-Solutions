class Program
{
    

    static int getHousesVisited(char[] directions)
    {
        int x = 0; int y = 0;

        HashSet<string> houses = new HashSet<string>
        {
            $"{x},{y}"
        };

        foreach (char direction in directions)
        {
            switch (direction)
            {
               
                case '^':
                    y++;
                    break;
                case 'v':
                    y--;
                    break;
                case '>':
                    x++;
                    break;
                case '<':
                    x--;
                    break;
            }

            houses.Add($"{x},{y}");
            
        }


        return houses.Count;
    }


    static void Main(string[] args)
    {
        string inputPath = Path.Combine(Directory.GetCurrentDirectory(), "..", "..", "input.txt");

        // Check if the input file exists
        if (!File.Exists(inputPath))
        {
            Console.WriteLine("Input file not found.");
            return;
        }

        char[] directions = File.ReadAllText(inputPath).ToCharArray();

        Console.WriteLine($"Houses visited: {getHousesVisited(directions)}");
    }
}
    