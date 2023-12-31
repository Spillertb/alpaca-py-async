import datetime
import os

import asyncio

from alpaca.trading import TradingClient
from alpaca.data.historical.news import NewsClient
from alpaca.data import NewsRequest, StockBarsRequest
from alpaca.data import NewsRequest, StockHistoricalDataClient, TimeFrame, TimeFrameUnit

key = os.getenv("ALPACA_API_KEY", "no_api_key_provided")

secret = os.getenv("ALPACA_API_SECRET", "no_api_secret_provided")


async def test_clients():
    trading_client = TradingClient(
        api_key=key,
        secret_key=secret,
        paper=True,
    )
    news_client = NewsClient(
        api_key=key,
        secret_key=secret,
    )
    stock_client = StockHistoricalDataClient(
        api_key=key,
        secret_key=secret,
    )

    for i in range(10):
        clock = await trading_client.get_clock()
        print(clock)

        news = await news_client.get_news(NewsRequest())
        # print(news)

        bars = await stock_client.get_stock_bars(
            StockBarsRequest(
                symbol_or_symbols="SPY",
                start=datetime.datetime(2023, 12, 26),
                timeframe=TimeFrame(amount=1, unit=TimeFrameUnit.Minute),
            )
        )
        # print(bars)
        await asyncio.sleep(0.001)

    await trading_client.close()
    await news_client.close()
    await stock_client.close()


def run_tests():
    # Run the GET request test
    asyncio.run(test_clients())

    asyncio.run(test_clients())


if __name__ == "__main__":
    run_tests()
