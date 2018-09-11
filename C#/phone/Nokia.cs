using System;

namespace phone
{
    public class Nokia : Phone, IRingable
    {
        public Nokia(string versionNumber, int batteryPercentage, string carrier, string ringTone)
           : base(versionNumber, batteryPercentage, carrier, ringTone) 
           { }
        public string Ring()
        {
            return _RingTone;
        }
        public string Unlock()
        {
            return "Nokia unlocked with face scan BOOM";
        }
        public override void DisplayInfo()
        {
            Console.WriteLine(_VersionNumber);
            Console.WriteLine(_BatteryPercentage); 
            Console.WriteLine(_Carrier);
            Console.WriteLine(_RingTone);         
        }
    }
}