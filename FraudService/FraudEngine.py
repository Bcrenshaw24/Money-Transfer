from datetime import datetime

KNOWN_VPN_IPS = {
    "192.0.2.1": {
        "location": "Netherlands",
        "provider": "NordVPN",
        "risk_score": 85
    },
    "203.0.113.5": {
        "location": "Panama",
        "provider": "ExpressVPN",
        "risk_score": 90
    },
    "45.123.88.99": {
        "location": "Switzerland",
        "provider": "Private Internet Access",
        "risk_score": 80
    },
    "185.12.45.67": {
        "location": "Russia",
        "provider": "UnknownVPN",
        "risk_score": 95
    },
    "103.21.244.1": {
        "location": "India",
        "provider": "Surfshark",
        "risk_score": 88
    },
    "77.88.55.77": {
        "location": "Germany",
        "provider": "CyberGhost",
        "risk_score": 83
    },
    "154.16.202.22": {
        "location": "Singapore",
        "provider": "ProtonVPN",
        "risk_score": 89
    }
}

class FraudEngine: 

    def __init__(self, IP): 
        self.IP = IP 
        self.knownIp = KNOWN_VPN_IPS
        
        
    #Checks user IP against known VPN IP addresses
    def checkIP(self): 
        if self.ip in self.knownIp: 
            if self.knownIp[self.ip]["risk_score"] > 82: 
                return False 
        return True 
    
    def checkTime(self, time, amount): 
        dt = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")

        now = datetime.now() 
        delta = now - dt 

        if delta.days < 7 and amount >= 1000: 
            return False 
        return True 
    

    
    



        