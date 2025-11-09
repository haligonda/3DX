import os 
import asyncio
from crawl4ai import AsyncWebCrawler

# define directory, file name and file path
directory = 'data/2025'
file_name = '11.markdown'
file_path = os.path.join(directory, file_name)

# Create the directory and necessary parent directory
os.makedirs(directory, exist_ok=True)

async def main(year, month):
    # Create an instance of AsyncWebCrawler
    async with AsyncWebCrawler() as crawler:
        # Run the crawler on a URL
        result = await crawler.arun(url=f"https://huggingface.co/papers/month/{year}-{month}")

        # Print the extracted content
        try: 
            with open(file=file_path, mode='w', encoding='utf-8') as markdown_file:
                markdown_file.write(result.markdown)
                markdown_file.close()
            print(f"File Written Sucessfully: {file_path}")
        except Exception as e:
            print(f"Error occured writing file:\n {e}")

# Run the async main function
asyncio.run(main(year=2025, month=11))
