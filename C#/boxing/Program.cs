using System;
using System.Collections.Generic;
namespace boxing
{
    class Program
    {
        static void Main(string[] args)
        {
            List<object> bikes = new List<object>();
            //Use the Add function in a similar fashion to push
            bikes.Add(7);
            bikes.Add(28);
            bikes.Add(-1);
            bikes.Add(true);
            bikes.Add("chair");
            int sum =0;
            for(var i =0; i < bikes.Count; i++)
            {
                Console.WriteLine(bikes[i]);
                if(bikes[i] is int)
                {
                    int ExplicitInt = (int)bikes[i];
                    sum = sum + ExplicitInt;
                }
            }
            Console.WriteLine(sum);
        }
    }
}
