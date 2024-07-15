from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class CryptoData(BaseModel):
    symbol: str
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float


class MetaData(BaseModel):
    start_date: datetime
    end_date: datetime
    symbols: List[str]
    timeframe: str
