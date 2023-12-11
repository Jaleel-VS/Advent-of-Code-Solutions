
using System.Security.Cryptography;
using System.Text;

class Program
{
    static int getValidSuffix(string input)
    {
        int suffix = 0;
        while (true)
        {
            string hash = CalculateMD5Hash(input + suffix.ToString());
            if (hash.StartsWith("00000"))
            {
                return suffix;
            }
            suffix++;
        }
    }

    private static string CalculateMD5Hash(string v)
    {
        byte[] inputBytes = Encoding.ASCII.GetBytes(v);
        byte[] hash = MD5.Create().ComputeHash(inputBytes);

        // Convert byte array to hex string
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < hash.Length; i++)
        {
            sb.Append(hash[i].ToString("X2"));
        }

        return sb.ToString();
    }

    static void Main(string[] args)
    {
        string inputPath = Path.Combine(Directory.GetCurrentDirectory(), "..", "..", "input.txt");

        // Check if the input file exists
        if (!File.Exists(inputPath))
        {
            Console.WriteLine("Input file not found.");
            return;
        }

        string input = File.ReadAllText(inputPath);

        int suffix = getValidSuffix(input);

        Console.WriteLine("The valid suffix is: " + suffix);
    }
}
    