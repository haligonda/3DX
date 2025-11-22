import os 
from crawl4ai import AsyncWebCrawler
import aiofiles

class Month:
    def __init__(self, year, month, base_dir="data"):
        self.year = str(year) 
        # keep provided month formatting, or pad if numeric and you want two digits:
        try:
            self.month = str(int(month)).zfill()
        except Exception:
            # if month is already a string like "W46" just use it
            self.month = str(month)
        self.base_dir = base_dir

    def get_file_path(self) -> str:
        """Join and Check file and return filepath"""
        directory = os.path.join(self.base_dir, self.year)
        file_name = f"{self.month}.markdown"
        os.makedirs(directory, exist_ok=True)
        return os.path.join(directory, file_name)
    
    async def crawl(self):
        file_path = self.get_file_path()

        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun(url=f"https://huggingface.co/papers/month/{self.year}-{self.month}")
            if not result:
                print("Crawler returned no result; nothing to write.")
                return
            
            markdown = getattr(result, "markdown", None)
            if not markdown:
                print("Crawler result has no 'markdown' attribute or it is empty.")
                return 
            
            # Save raw markdown
            try: 
                async with aiofiles.open(file=file_path, mode='w', encoding='utf-8') as f:
                    await f.write(result.markdown)
                print(f"File Written Successfully: {file_path}")
            except (OSError, IOError) as e:
                print(f"Error writing file {file_path}: {e}")
