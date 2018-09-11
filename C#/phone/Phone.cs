using System;

namespace phone
{
    public abstract class Phone
    {
        private string _versionNumber;
        public string _VersionNumber
        {
            get { return _versionNumber; }
        }
        private int _batteryPercentage;
        public int _BatteryPercentage
        {
            get { return _batteryPercentage; }
        }
        private string _carrier;
        public string _Carrier
        {
            get { return _carrier; }
        }
        private string _ringTone;
        public string _RingTone
        {
            get { return _ringTone; }
        }
        public Phone(string versionNumber, int batteryPercentage, string carrier, string ringTone)
        {
            _versionNumber = versionNumber;
            _batteryPercentage = batteryPercentage;
            _carrier = carrier;
            _ringTone = ringTone;
        }
        
        // abstract method. This method will be implemented by the subclasses
        public abstract void DisplayInfo();
        // public getters and setters removed for brevity. Please implement them yourself
    }
}