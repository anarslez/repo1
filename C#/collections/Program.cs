using System;
using System.Collections.Generic;
namespace collections
{
    class Program
    {
        static void Main(string[] args)
        {
            //problem 1,2,3
            int[] arrayOfInts = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
            string[] arrayOfstrings = { "Tim", "Martin", "Nikki", "Sara" };
            bool[] arrayOfbool = { true, false, true, false, true, false, true, false, true, false };
            //list of flavors
            List<string> ice = new List<string>();
            ice.Add("chocolate");
            ice.Add("vanilla");
            ice.Add("good");
            ice.Add("rainbow");
            ice.Add("strawberry");
            Console.WriteLine(ice.Count);
            Console.WriteLine(ice[2]);
            ice.RemoveAt(2);
            Console.WriteLine(ice.Count);
            //dictionary
            Dictionary<string, string> profile = new Dictionary<string, string>();
            profile.Add("Name", null);
            profile.Add("Language", null);
            profile.Add("Location", null);
            Random rand = new Random();
            profile["Name"] = ice[rand.Next(0, 3)];
            profile["Language"] = ice[rand.Next(0, 3)];
            profile["Location"] = ice[rand.Next(0, 3)];
            foreach (var entry in profile)
            {
                Console.WriteLine(entry.Key + " - " + entry.Value);
            }
        }
    }
}
