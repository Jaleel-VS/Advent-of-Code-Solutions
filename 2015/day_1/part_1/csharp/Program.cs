var inputPath = Path.Combine(Directory.GetCurrentDirectory(), "..", "..", "input.txt");

var inputData = File.ReadAllText(inputPath);

Dictionary<string, int> floorAdjustment = new Dictionary<string, int>();

floorAdjustment.add("(", 1)
floorAdjustment.add(")", -1)

foreach(var floor in inputData)


