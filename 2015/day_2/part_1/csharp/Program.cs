class Program {

    static int getSurfaceArea(int l, int w, int h) {
        return 2*l*w + 2*w*h + 2*h*l;
    }

    static int getSlack(int l, int w, int h) {
        return new int[]{l*w, w*h, h*l}.Min();
    }
    public static void Main(string[] args) {
        string inputPath = Path.Combine(Directory.GetCurrentDirectory(), "..", "..", "input.txt");

        System.Console.WriteLine(inputPath);

        // Check if the input file exists
        if (!File.Exists(inputPath))
        {
            Console.WriteLine("Input file not found.");
            return;
        }

        int totalWrappingPaper = 0;

        foreach (string present in File.ReadLines(inputPath))
        {
            var dimensions = present.Split('x').Select(int.Parse).ToArray();

            int l = dimensions[0], w = dimensions[1], h = dimensions[2];

            totalWrappingPaper += getSurfaceArea(l, w, h) + getSlack(l, w, h);
        }

        Console.WriteLine($"Total wrapping paper: {totalWrappingPaper} sqft");



        
    }
}