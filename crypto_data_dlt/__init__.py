import dlt
from typing import Iterator
from dlt.common.typing import TAnyDateTime
from dlt.common.time import ensure_pendulum_datetime
from .helpers import AlpacaCryptoApi
from .schemas import MetaData
from .settings import DEFAULT_START_DATE, DEFAULT_END_DATE, DEFAULT_TIMEFRAME, DEFAULT_SYMBOLS

# Initialize the API client globally
api_client = AlpacaCryptoApi()

@dlt.resource(name="crypto_data", write_disposition="replace")
def crypto_data_generator(start_date: TAnyDateTime, end_date: TAnyDateTime, timeframe: str, symbols: str):
    for item in api_client.fetch_crypto_data(
        start_date=ensure_pendulum_datetime(start_date).isoformat(),
        end_date=ensure_pendulum_datetime(end_date).isoformat(),
        timeframe=timeframe,
        symbols=symbols
    ):
        yield item  # Yield the raw item directly to let dlt handle the unnesting

@dlt.resource(name="metadata", write_disposition="replace")
def metadata_generator(start_date: TAnyDateTime, end_date: TAnyDateTime, symbols: str, timeframe: str):
    metadata = MetaData(
        start_date=start_date,
        end_date=end_date,
        symbols=symbols.split(","),
        timeframe=timeframe
    )
    yield metadata.dict()

@dlt.source(name="alpaca_crypto")
def alpaca_crypto_source(
    start_date: TAnyDateTime = DEFAULT_START_DATE,
    end_date: TAnyDateTime = DEFAULT_END_DATE,
    timeframe: str = DEFAULT_TIMEFRAME,
    symbols: str = DEFAULT_SYMBOLS,
) -> Iterator[dlt.resource]:
    yield crypto_data_generator(start_date, end_date, timeframe, symbols)
    yield metadata_generator(start_date, end_date, symbols, timeframe)
