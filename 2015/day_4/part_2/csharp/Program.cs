using System;
using System.Collections.Concurrent;
using System.Diagnostics;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

class Program
{
    static void Main(string[] args)
    {
        string inputPath = Path.Combine(Directory.GetCurrentDirectory(), "..", "..", "input.txt");

        if (!File.Exists(inputPath))
        {
            Console.WriteLine("Input file not found.");
            return;
        }

        string input = File.ReadAllText(inputPath);

        Stopwatch sw = Stopwatch.StartNew();

        int validSuffix = ParallelFind(input, "000000");

        sw.Stop();

        Console.WriteLine("The valid suffix is: " + validSuffix);
        Console.WriteLine("Time taken: " + sw.ElapsedMilliseconds + "ms");
    }

    static int ParallelFind(string input, string prefix)
    {
        var q = new ConcurrentQueue<int>();

        Parallel.ForEach(
            Numbers(), 
            () => MD5.Create(), 
            (i, state, md5) => {
                var hashBytes = md5.ComputeHash(Encoding.ASCII.GetBytes(input + i));
                var hash = string.Join("", hashBytes.Select(b => b.ToString("x2")));

                if (hash.StartsWith(prefix)) {
                    q.Enqueue(i);
                    state.Stop();
                }
                return md5;
             }, 
             (_) => {}
        );

        return q.Min();
    }

    static IEnumerable<int> Numbers()
    {
        for (int i = 1; ; i++)
        {
            yield return i;
        }
    }
}
