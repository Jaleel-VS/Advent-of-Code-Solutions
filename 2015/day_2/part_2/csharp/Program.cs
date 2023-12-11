class Program
{

    static int getSmallPerimeter(int l, int w, int h)
    {
        return new int[] { 2 * l + 2 * w, 2 * w + 2 * h, 2 * h + 2 * l }.Min();
    }

    static int getVolume(int l, int w, int h)
    {
        return l * w * h;
    }

    public static void Main(string[] args)
    {
        string inputPath = Path.Combine(Directory.GetCurrentDirectory(), "..", "..", "input.txt");

        // Check if the input file exists
        if (!File.Exists(inputPath))
        {
            Console.WriteLine("Input file not found.");
            return;
        }

        int totalRibbon = 0;

        foreach (string present in File.ReadLines(inputPath))
        {
            var dimensions = present.Split('x').Select(int.Parse).ToArray();

            int l = dimensions[0], w = dimensions[1], h = dimensions[2];

            totalRibbon += getSmallPerimeter(l, w, h) + getVolume(l, w, h);
        }

        Console.WriteLine($"Total ribbon: {totalRibbon} ft");
    }
}