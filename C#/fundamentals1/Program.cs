using System;

namespace fundamentals1
{
    class Program
    {
        static void Main(string[] args)
        {
            // problem 1
            for (int i = 1; i <= 255; i++)
            {
                Console.WriteLine(i);
            }
            // problem 2
            for (int i = 1; i <= 100; i++)
            {
                if (i%3 == 0 || i%5 == 0 && i%15!=0)
                {
                    Console.WriteLine(i);
                }
            }
            // problem 3
            for (int i = 1; i <= 100; i++)
            {
                if (i%3 == 0)
                {
                    Console.WriteLine("Fizz");
                }
                if (i%5 == 0)
                {
                    Console.WriteLine("Buzz");
                }
                if (i%15 == 0)
                {
                    Console.WriteLine("FizzBuzz");
                }
            }
        }
    }
}
