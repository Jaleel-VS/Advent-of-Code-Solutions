class Program
{
    static void Main(string[] args)
    {
        var inputPath = Path.Combine(Directory.GetCurrentDirectory(), "..", "..", "input.txt");

        // Check if the input file exists
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

            // Iterate through each character in the input data
            for (var i = 0; i < inputData.Length; i++)
            {
                currentFloor += floorAdjustment.GetValueOrDefault(inputData[i], 0);

                // Check if Santa has entered the basement
                if (currentFloor < 0)
                {
                    Console.WriteLine($"The position of the character that causes Santa to first enter the basement is {i + 1}.");
                    break;
                }
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"An error occurred: {ex.Message}");
        }
    }
}
