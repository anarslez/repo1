using System;

namespace puzzles
{
    class Program
    {
        static int[] randarr()
        {
            Random rand = new Random();
            int[] arr = new int[10];
            for (int i = 0; i < arr.Length; i = i + 1)
            {
                arr[i] = rand.Next(5, 25);
            }
            int max = arr[0];
            int min = arr[0];
            int avg = 0;
            for (int i = 0; i < arr.Length; i = i + 1)
            {
                avg = avg + arr[i];
                if (max < arr[i])
                {
                    max = arr[i];
                }
                if (min < arr[i])
                {
                    max = arr[i];
                }
            }
            Console.WriteLine(max);
            Console.WriteLine(min);
            Console.WriteLine(avg);
            return arr;
        }
        static string tosscoin()
        {
            Random rand = new Random();
            int toss = rand.Next(2);
            if (toss < 1)
            {
                return "heads";
            }
            else
            {
                return "tails";
            }
        }
        static double tossmult(int num)
        {
            Random rand = new Random();
            int cnt = 0;
            for (int i = 0; i < num; i++)
            {
                int toss = rand.Next(2);
                if (toss < 1)
                {
                    cnt = cnt + 1;
                }
            }
            double cntd = (double)cnt;
            double numd = (double)num;
            double res = cntd / numd;
            return res;
        }
        static string[] names()
        {
            Random rand = new Random();
            string[] name = { "todd", "tiff", "gen", "sid", "addi" };
            for (int i = 0; i < 5; i++)
            {
                int ind = rand.Next(5);
                if (ind != i)
                {
                    string tmp = name[i];
                    name[i] = name[ind];
                    name[ind] = tmp;
                }
            }
            return name;
        }
        static void Main(string[] args)
        {
            randarr();
            Console.WriteLine(tosscoin());
            Console.WriteLine(tossmult(20));
            Console.WriteLine(names());
        }
    }
}
