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
    }
}
    