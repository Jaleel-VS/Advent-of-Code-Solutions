
class Program
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

        char[] directions = File.ReadAllText(inputPath).ToCharArray();

        Console.WriteLine($"Houses visited: {getHousesVisited(directions)}");
    }

    static int getHousesVisited(char[] directions)
    {
        int x = 0; int y = 0;
        int x2 = 0; int y2 = 0;

        HashSet<string> houses = new HashSet<string>
         {
              $"{x},{y}"
         };

         for (int i = 0; i < directions.Length; i++) {
            if (i % 2 == 0) {
                switch (directions[i])
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
            } else {
                switch (directions[i])
                {
                    case '^':
                        y2++;
                        break;
                    case 'v':
                        y2--;
                        break;
                    case '>':
                        x2++;
                        break;
                    case '<':
                        x2--;
                        break;
                }

                houses.Add($"{x2},{y2}");
            }
         }






        return houses.Count;

    }
}
