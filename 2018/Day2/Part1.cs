namespace Day2;

public class Part1
{
    public static int GetCheckSum(string input)
    {
        string[] ids = input.Split('\n');

        int exactlyTwo = 0;
        int exactlyThree = 0;

        foreach (var id in ids)
        {
            Dictionary<char, int> lettersCount = new Dictionary<char, int>();

            foreach (var letter in id.ToCharArray())
            {
                if (lettersCount.TryGetValue(letter, out int count))
                {
                    lettersCount[letter] = count + 1;
                }
                else
                {
                    lettersCount.Add(letter, 1);
                }
            }

            var result = GetCounts(lettersCount);

            exactlyTwo += result.twos;
            exactlyThree += result.threes;


        }

        return exactlyTwo * exactlyThree;
    }

    private static (int twos, int threes) GetCounts(Dictionary<char, int> letterCount)
    {
        int twos = 0;
        int threes = 0;

        foreach (var pair in letterCount)
        {
            if (pair.Value == 2 && twos < 1) twos += 1;
            if (pair.Value == 3 && threes < 1) threes += 1;
        }

        return (twos, threes);


    }
}