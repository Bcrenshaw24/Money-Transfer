from datetime import datetime
import joblib
import numpy as np

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
        self.model = joblib.load("fraud_xgb_model.joblib")

    def checkIP(self): 
        if self.IP in self.knownIp: 
            if self.knownIp[self.IP]["risk_score"] > 82: 
                return True
        return False

    def limit(self, amount, limit): 
        if amount <= limit * 0.5:
            return True
        return False

    def geoCheck(self, geo): 
        if geo < 1200:
            return True
        return False

    def model_predict(self, features_dict):
        feature_order = [
            "amount", "source_balance", "source_monthly_sent", "source_monthly_limit",
            "average_transaction_amount_30d", "transaction_count_24h", "login_count_24h",
            "geo_distance_km", "hour_of_day", "day_of_week", "source_account_age_days",
            "destination_account_age_days", "amount_over_avg_ratio", "amount_pct_of_balance",
            "amount_pct_of_limit", "last_login_ip_same", "known_device"
        ]
        # Convert booleans to int for model input
        features_dict["last_login_ip_same"] = int(features_dict["last_login_ip_same"])
        features_dict["known_device"] = int(features_dict["known_device"])
        features = np.array([features_dict[feat] for feat in feature_order]).reshape(1, -1)
        prediction = self.model.predict(features)
        return int(prediction[0])

    def predict_transaction(self, features_dict):
        # Prechecks
        if not self.checkIP():
            return 1
        if not self.limit(features_dict["amount"], features_dict["source_monthly_limit"]):
            return 1
        if not self.geoCheck(features_dict["geo_distance_km"]):
            return 1
        # Model prediction
        return self.model_predict(features_dict)










