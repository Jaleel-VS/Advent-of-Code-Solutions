namespace Day2;

public class Part2
{
    public static string getPrototype(string input)
    {
        string[] ids = input.Split('\n');

        for (int i = 0; i < ids.Length; i++)
        {
            for (int j = 0; j < ids.Length; j++)
            {
                if (i != j)
                {
                    int differingStrings = 0;
                    int differingIndex = -1;

                    for (int k = 0; k < ids[i].Length; k++)
                    {
                        if (ids[i][k] != ids[j][k])
                        {
                            differingStrings += 1;
                            differingIndex = k;
                        }

                        if (differingStrings > 1) break;
                    }

                    if (differingStrings == 1) return ids[i].Remove(differingIndex, 1);
                }
            }
        }

        return "";
    }
}