using System;

namespace phone
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            Galaxy s8 = new Galaxy("s8",10,"poo","hi ozzy");
            Console.WriteLine(s8.Unlock());
            s8.DisplayInfo();
        }
    }
}
