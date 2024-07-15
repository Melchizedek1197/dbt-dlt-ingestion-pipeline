import dlt
from typing import Iterator
from dlt.common.typing import TAnyDateTime
from dlt.common.time import ensure_pendulum_datetime
from .helpers import AlpacaCryptoApi
from .schemas import CryptoData, MetaData
from .settings import DEFAULT_START_DATE, DEFAULT_END_DATE, DEFAULT_TIMEFRAME, DEFAULT_SYMBOLS

@dlt.source(name="alpaca_crypto")
def alpaca_crypto_source(
    start_date: TAnyDateTime = DEFAULT_START_DATE,
    end_date: TAnyDateTime = DEFAULT_END_DATE,
    timeframe: str = DEFAULT_TIMEFRAME,
    symbols: str = DEFAULT_SYMBOLS,
) -> Iterator[dlt.resource]:
    """
    The source for fetching Alpaca crypto data.

    Args:
        start_date: The start date for fetching data.
        end_date: The end date for fetching data.
        timeframe: The timeframe for the data (e.g., 1Day).
        symbols: The symbols to fetch (e.g., "BTC/USD").

    Yields:
        dlt.resource: A data resource representing each fetched item.
    """
    api_client = AlpacaCryptoApi()

    @dlt.resource(name="crypto_data", write_disposition="replace")
    def crypto_data_generator():
        for item in api_client.fetch_crypto_data(
            start_date=ensure_pendulum_datetime(start_date).isoformat(),
            end_date=ensure_pendulum_datetime(end_date).isoformat(),
            timeframe=timeframe,
            symbols=symbols
        ):
            # Handling nested structure
            if isinstance(item, dict):
                for symbol, data_list in item.items():
                    for data in data_list:
                        if isinstance(data, dict):
                            try:
                                crypto_data = CryptoData(
                                    symbol=symbol,
                                    timestamp=ensure_pendulum_datetime(data["t"]),
                                    open=data["o"],
                                    high=data["h"],
                                    low=data["l"],
                                    close=data["c"],
                                    volume=data["v"]
                                )
                                yield crypto_data.dict()
                            except KeyError as e:
                                print(f"KeyError encountered: {e}. Skipping data: {data}")
                        else:
                            print(f"Warning: Skipping item due to unexpected format: {data}")
            else:
                print(f"Warning: Skipping item due to unexpected format: {item}")

    @dlt.resource(name="metadata", write_disposition="replace")
    def metadata_generator():
        metadata = MetaData(
            start_date=start_date,
            end_date=end_date,
            symbols=symbols.split(","),
            timeframe=timeframe
        )
        yield metadata.dict()

    yield crypto_data_generator
    yield metadata_generator
