# Excavator&Dumper
Collect all top AI Research paper and notify to my Whatsapp Chat.

<!-- Scrape Hugging Face Daily Research Paper site -->
<!-- Or find do they provide any service related like direct API -->

<!-- Classify each research paper and store it in seperate folder -->
<!-- Send Notification and researh summery to Whatsapp Chat -->

<!-- Store Each research paper efficiently in disk and find easy way to access it -->

I am taking AI help to build this project.

Features: 

Progress: todo list updated (previous tasks marked complete, new feature-suggestion task added/completed). Below are simple feature ideas you can add to the scraper — each is small, practical, and quick to implement.

CLI flags for year/month and base directory
What: Allow running the scraper with arguments like --year 2025 --month 11 --out data/.
Why: Makes testing and automation easy.
Complexity: very small
Files to change: scrap.py (add argparse) and optionally main.py.
Notes: Use argparse; call asyncio.run(Month(year, month, base_dir).crawl()).
"Dry run" / preview mode
What: Add --dry-run to fetch the page but not write the file; print summary instead.
Why: Quickly verify the crawler and URL formation without disk writes.
Complexity: very small
Files to change: scrap.py and CLI/main.
Notes: Skip file write when flag is present; still validate result.
Verbose logging / structured logging
What: Use Python logging with levels; add --verbose to set debug output.
Why: Better diagnostics than prints; handy in CI.
Complexity: small
Files to change: scrap.py, main.py.
Notes: Replace prints with logger.info/debug/error.
Safe/atomic write (temp-then-rename)
What: Write to a temp file then rename into place to avoid partial files.
Why: Prevents corrupted files on interruption.
Complexity: small
Files to change: scrap.py
Notes: Use tempfile.NamedTemporaryFile(delete=False) or write to file_path + ".tmp" then os.replace().

Retry with backoff for crawler errors
What: Retry the crawl N times with exponential backoff on network errors.
Why: More robust against transient failures.
Complexity: small–medium
Files to change: scrap.py
Notes: Implement simple loop with asyncio.sleep(2 ** retry).
Month range runner (batch mode)
What: Add ability to run for a range of months (e.g., --from 2025-01 --to 2025-06) and save each file.
Why: Useful to backfill months in one run.
Complexity: small–medium
Files to change: main.py or CLI wrapper + scrap.py (no large changes).
Notes: Parse ranges and iterate, reusing Month class.
Skip existing files (idempotence)
What: If the target file already exists, skip unless --force is set.
Why: Avoid redundant downloads and overwriting.
Complexity: very small
Files to change: scrap.py
Notes: Check os.path.exists(file_path) before writing.
Quick suggested priorities (if you want to add a single thing now)

Easiest + most useful: (1) CLI flags and (8) Skip existing files. Combine them in one small edit.
Next: (3) add logging and (2) dry-run.
Later: (6) retry/backoff and (7) month-range runner.