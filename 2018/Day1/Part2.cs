namespace Day1;

public class Part2
{
    public static int GetFirstVisitedTwice(string input)
    {
        HashSet<int> frequencies = new HashSet<int>(){ 0 };
        string[] lines = input.Split('\n');
        int frequency = 0;

        while (true)
        {
            foreach (string line in lines)
            {
                frequency += int.Parse(line);

                if (!frequencies.Add(frequency))
                {
                    return frequency;
                }

                

            }
        }
    }
}