namespace Day1;

public class Part1
{
    public static int CalculateFrequency(string input)
    {
        int frequency = 0;
        foreach (string line in input.Split('\n'))
        {
            frequency += int.Parse(line);
        }

        return frequency;
    }
}