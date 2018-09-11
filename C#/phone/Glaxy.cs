using System;

namespace phone
{
    public class Galaxy : Phone, IRingable
    {
        public Galaxy(string versionNumber, int batteryPercentage, string carrier, string ringTone)
           : base(versionNumber, batteryPercentage, carrier, ringTone) 
           { }
        public string Ring()
        {
            return _RingTone;
        }
        public string Unlock()
        {
            return "Galaxy unlocked with face scan BOOM";
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