import asyncio
from crawl import Month

async def main():
    month = Month(year=2025, month=10)
    await month.crawl()

if __name__ == "__main__":
    asyncio.run(main())

