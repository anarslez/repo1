using System;

namespace human
{
    public class Human
    {
        public int strength;
        public int intellegence;
        public int dexterity;
        public int health;
        public string name;
        public Human(string passname)
        {
            name = passname;
            strength = 3;
            intellegence = 3;
            dexterity = 3;
            health = 100;
        }
        public Human(string passname, int str, int intl, int dxt, int hlth)
        {
            name = passname;
            strength = str;
            intellegence = intl;
            dexterity = dxt;
            health = hlth;
        }
        public void attack(object obj)
        {
            Human enemy = obj as Human;
            if (enemy == null)
            {
                Console.WriteLine("Failed Attack");
            }
            else
            {
                enemy.health -= strength * 5;
            }
        }
        public class Wizard : Human
        {
            public Wizard(string passname) : base(passname)
            {
                name = passname;
                strength = 3;
                intellegence = 25;
                dexterity = 3;
                health = 50;
            }
            public Wizard(string passname, int str, int intl, int dxt, int hlth) : base(passname, str, intl, dxt, hlth)
            {
                name = passname;
                strength = str;
                intellegence = intl;
                dexterity = dxt;
                health = hlth;
            }
            public void fireball(object obj)
            {
                Random rand = new Random();
                Human enemy = obj as Human;
                if (enemy == null)
                {
                    Console.WriteLine("Failed Attack");
                }
                else
                {
                    enemy.health -= rand.Next(20, 50);
                }
            }
            public void heal()
            {
                int hlth = health;
                int intl = intellegence;
                health = hlth + intl * 10;
            }
        }
        public class Ninja : Human
        {
            public Ninja(string passname) : base(passname)
            {
                name = passname;
                strength = 3;
                intellegence = 3;
                dexterity = 175;
                health = 100;
            }
            public Ninja(string passname, int str, int intl, int dxt, int hlth) : base(passname, str, intl, dxt, hlth)
            {
                name = passname;
                strength = str;
                intellegence = intl;
                dexterity = dxt;
                health = hlth;
            }
            public void steal(object obj)
            {
                Human enemy = obj as Human;
                if (enemy == null)
                {
                    Console.WriteLine("Failed Attack");
                }
                else
                {
                    enemy.health -= strength * 5;
                    health += 10;
                }
            }
            public void get_away()
            {
                health -= 15;
            }
        }
        public class Samurai : Human
        {
            public Samurai(string passname) : base(passname)
            {
                name = passname;
                strength = 3;
                intellegence = 3;
                dexterity = 3;
                health = 200;
            }
            public Samurai(string passname, int str, int intl, int dxt, int hlth) : base(passname, str, intl, dxt, hlth)
            {
                name = passname;
                strength = str;
                intellegence = intl;
                dexterity = dxt;
                health = hlth;
            }
            public void death_blow(object obj)
            {
                Human enemy = obj as Human;
                if (enemy == null)
                {
                    Console.WriteLine("Failed Attack");
                }
                else
                {
                    if (enemy.health <= 50)
                    {
                        enemy.health = 0;
                    }
                    else
                    {
                        Console.WriteLine("Failed Attack");
                    }
                }
            }
            public void meditate()
            {
                health = 200;
            }
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }
    }
}
