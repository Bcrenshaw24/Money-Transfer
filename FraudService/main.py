from pydantic import BaseModel
from typing import Optional

class TransactionRequest(BaseModel):
    transaction_id: str
    timestamp: str
    amount: float
    source_balance: float
    source_monthly_sent: float
    source_monthly_limit: float
    average_transaction_amount_30d: float
    transaction_count_24h: int
    login_count_24h: int
    geo_distance_km: float
    hour_of_day: int
    day_of_week: int
    source_account_age_days: int
    destination_account_age_days: int
    amount_over_avg_ratio: float
    amount_pct_of_balance: float
    amount_pct_of_limit: float
    last_login_ip_same: bool
    known_device: bool
    ip_address: str