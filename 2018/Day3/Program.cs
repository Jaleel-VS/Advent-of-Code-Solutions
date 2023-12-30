namespace Day3;

public class Program
{
    public static void Main()
    {
        string? input = GetFileInput();
        if (input == null)
        {
            Console.WriteLine("Input file not found.");
            return;
        }
        
        Console.WriteLine("Part 1 Solution:");
        Console.WriteLine($"Squares: {Part1.getClaimedSquares(input)}");
        Console.WriteLine("Part 2 Solution:");
        // Console.WriteLine($"Prototype: {Part2.getPrototype(input)}");
    }

    private static string? GetFileInput()
    {
        string inputPath = Path.Combine(Directory.GetCurrentDirectory(), "input.txt");
        FileInfo file = new FileInfo(inputPath);

        while (!file.Exists)
        {
            if (file.Directory?.Parent == null)
            {
                return null;
            }
            DirectoryInfo parentDir = file.Directory.Parent;
            file = new FileInfo(Path.Combine(parentDir.FullName, file.Name));
        }

        return File.ReadAllText(file.FullName);
    }

    
}