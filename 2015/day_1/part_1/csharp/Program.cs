class Program
{
    static void Main(string[] args)
    {
        var inputPath = Path.Combine(Directory.GetCurrentDirectory(), "..", "..", "input.txt");

        if (!File.Exists(inputPath))
        {
            Console.WriteLine("Input file not found.");
            return;
        }

        try
        {
            var inputData = File.ReadAllText(inputPath);
            var floorAdjustment = new Dictionary<char, int>
            {
                { '(', 1 },
                { ')', -1 }
            };

            var currentFloor = 0;
            foreach (var c in inputData)
            {
                currentFloor += floorAdjustment.GetValueOrDefault(c, 0);
            }

            Console.WriteLine($"The final floor is {currentFloor}");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"An error occurred: {ex.Message}");
        }
    }
}
