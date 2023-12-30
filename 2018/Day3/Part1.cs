using System.Text.RegularExpressions;

namespace Day3;

public class Part1
{
    private static char[,] squareOfFabric = new char[1000, 1000];

    public static int getClaimedSquares(string input)
    {
        string[] claims = input.Split('\n');

        foreach (string claim in claims)
        {
            claimFabric(claim);
        }

        int claimedSquares = 0;

        for (int i = 0; i < squareOfFabric.GetLength(0); i++)
        {
            for (int j = 0; j < squareOfFabric.GetLength(1); j++)
            {
                if (squareOfFabric[i, j] == 'X')
                {
                    claimedSquares++;
                }
            }
        }

        return claimedSquares;

    }

    private static void claimFabric(string instructions)
    {

        (int x, int y, int w, int l) = getDetails(instructions);

        for (int i = x; i < x + w; i++)
        {
            for (int j = y; j < y + l; j++)
            {
                char square = squareOfFabric[i, j];

                switch(square)
                {
                    case '\0':
                       squareOfFabric[i, j] = '#';
                       break;
                    case '#':
                        squareOfFabric[i, j] = 'X';
                        break;
                    default:
                        break;
                }
            }
        }

    }

    private static (int x, int y, int w, int l) getDetails(string instruction)
    {
        string pattern = @"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)";

        Match match = Regex.Match(instruction, pattern);

        int x = -1;
        int y = -1;
        int l = -1;
        int w = -1;

        if (match.Success)
        {
            x = int.Parse(match.Groups[2].Value);
            y = int.Parse(match.Groups[3].Value);
            w = int.Parse(match.Groups[4].Value);
            l = int.Parse(match.Groups[5].Value);


        }


        return (x, y, w, l);



    }
}