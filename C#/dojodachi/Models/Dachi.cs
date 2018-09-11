using System.ComponentModel.DataAnnotations;
using System;
namespace dojodachi.Models
    {
       public class Dachi
    {
        public int happiness {get; set;}
        public int fullness {get; set;}
        public int energy {get; set;}
        public int meals {get; set;}
        public string status {get; set;}
        public Dachi()
        {
            happiness = 20;
            fullness = 20; 
            energy = 50; 
            meals = 3;
            status = "Do dachi stuff!";
        }
        public Dachi feed()
        {
            Random rando = new Random();
            int chance = rando.Next(0,100);
            if(chance<25){
                this.meals-=1;
                this.status = "Your dachi wasn't hungry chill!!!";
                return this;
            }
            else{
                this.meals-=1;
                this.fullness+=rando.Next(5,11);
                this.status = $"Your dachi and is {fullness} full!!!";
                return this;
            }
        }
        public Dachi play()
        {
            Random rando = new Random();
            int chance = rando.Next(0,100);
            if(chance<25){
                this.energy-=5;
                this.status = "Your dachi didn't wanna play chill!!!";
                return this;
            }
            else{
                this.energy-=5;
                this.happiness+=rando.Next(5,11);
                this.status = $"Your dachi and is {happiness} happy!!!";
                return this;
            }
        }
        public Dachi work()
        {
            Random rando = new Random();
            this.energy-=5;
            this.meals+=rando.Next(1,4);
            this.status = $"Your dachi and has {meals} meals!!!";
            return this;
        }
        public Dachi sleep()
        {
            this.energy+=15;
            this.happiness-=5;
            this.fullness-=5;
            this.status = $"Your dachi and has {energy} energy!!!";
            return this;
        }
    }
}