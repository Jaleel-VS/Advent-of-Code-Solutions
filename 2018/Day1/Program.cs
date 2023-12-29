namespace Day1;

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
        Console.WriteLine($"Total frequency: {Part1.CalculateFrequency(input)}");
        Console.WriteLine("Part 2 Solution:");
        Console.WriteLine($"Duplicate frequency: {Part2.GetFirstVisitedTwice(input)}");
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