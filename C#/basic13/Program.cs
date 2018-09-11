using System;
using System.Collections.Generic;
namespace basic13
{
    class Program
    {
        public static void one()
        {
            for (int i = 1; i <= 255; i++)
            {
                Console.WriteLine(i);
            }
        }
        public static void two()
        {
            for (int i = 1; i < 256; i = i + 2)
            {
                Console.WriteLine(i);
            }
        }
        public static void three()
        {
            int sum = 0;
            for (int i = 1; i < 256; i = i + 1)
            {
                sum = sum + i;
                Console.WriteLine(sum);
            }
        }
        public static void four(int[] arr)
        {
            for (int i = 0; i < arr.Length; i = i + 1)
            {
                Console.WriteLine(arr[i]);
            }
        }
        public static int five(int[] arr)
        {
            int max=arr[0];
            for (int i = 0; i < arr.Length; i = i + 1)
            {
                if(max<arr[i])
                {
                    max = arr[i];
                }
            }
            return max;
        }
        public static int six(int[] arr)
        {
            int sum=0;
            for (int i = 0; i < arr.Length; i = i + 1)
            {
                sum = sum+arr[i];
            }
            return sum/arr.Length;
        }
        public static int[] seven()
        {
            int[] y = new int[128];
            int ind = 0;
            for (int i = 1; i < 256; i = i+2)
            {
                y[ind]=i;
                ind = ind + 1;
            }
            return y;
        }
        public static int eight(int[] arr, int y)
        {
            int cnt=0;
            for (int i = 0; i < arr.Length; i = i + 1)
            {
                if(y<arr[i])
                {
                    cnt = cnt+1;
                }
            }
            return cnt;
        }
        public static int[] nine(int[] arr)
        {
            for (int i = 0; i < arr.Length; i = i + 1)
            {
                arr[i] = arr[i]*arr[i];
            }
            return arr;
        }
        public static int[] ten(int[] arr)
        {
            int max=0;
            for (int i = 0; i < arr.Length; i = i + 1)
            {
                if(max>arr[i])
                {
                    arr[i] = 0;
                }
            }
            return arr;
        }
        public static List<int> eleven(int[] arr)
        {
            int max=arr[0];
            int min = arr[0];
            int avg = 0;
            for (int i = 0; i < arr.Length; i = i + 1)
            {
                avg = avg + arr[i];
                if(max<arr[i])
                {
                    max = arr[i];
                }
                if(min<arr[i])
                {
                    max = arr[i];
                }
            }
            List<int> res = new List<int>();
            res.Add(max);
            res.Add(min);
            res.Add(avg/arr.Length);
            return res;
        }
        public static int[] twelve(int[] arr)
        {
            List<int> res = new List<int>();
            for (int i = 0; i < arr.Length; i = i + 1)
            {
                res.Add(arr[i]);
            }
            res.RemoveAt(0);
            res.Add(0);
            for (int i = 0; i < arr.Length; i = i + 1)
            {
                arr[i] = res[i];
            }
            return arr;
        }
        public static string[] thirteen(int[] arr)
        {
            string[] arrnew = new string[arr.Length];
            for (int i = 0; i < arr.Length; i = i + 1)
            {
                if(0>arr[i])
                {
                    arrnew[i] = "Dojo";
                }
                else 
                {
                    arrnew[i] = arr[i].ToString();
                }
            }
            return arrnew;
        }
    }
}
