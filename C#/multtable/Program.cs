using System;

namespace multtable
{
    class Program
    {
        static void Main(string[] args)
        {
            //multtable
            int[,] array2D = new int[10, 10];
            for (int i = 1; i < 11; i++)
            {
                for (int j = 1; j < 11; j++)
                {
                    int num = i*j;
                    Console.WriteLine(num); 
                    array2D[i-1,j-1]= i*j;
                }
            }
        }
    }
}
