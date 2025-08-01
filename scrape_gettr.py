import gogettr
import json
import sys

# add username
TARGET_USERNAME = "gatewaypundit" 
MAX_POSTS = 200 
OUTPUT_FILE = f"gettr_user_{TARGET_USERNAME}.json"

client = gogettr.PublicClient()
print(f"[*] Starting to scrape posts from user: {TARGET_USERNAME}")

scraped_data = []
error_count = 0

try:
    post_generator = client.user_activity(TARGET_USERNAME, max=MAX_POSTS, type="posts")

    for post in post_generator:
        try:
            scraped_data.append(post)
            print(".", end="", flush=True)

        except (TypeError, AttributeError):
            error_count += 1
            print(f"\n[!] Warning: Skipped a post due to malformed data.", file=sys.stderr)
        except Exception as e:
            error_count += 1
            print(f"\n[!] Warning: Skipped a post due to an unexpected error: {e}", file=sys.stderr)

except Exception as e:
    print(f"\n[X] A critical error occurred while fetching the activity feed: {e}", file=sys.stderr)
finally:    
    print(f"\n\n[*] Scraping finished.")
    print(f"[*] Successfully collected {len(scraped_data)} posts.")
    if error_count > 0:
        print(f"[*] Skipped {error_count} posts due to errors.")
    
    if scraped_data:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(scraped_data, f, ensure_ascii=False, indent=4)
        print(f"[*] Data successfully saved to {OUTPUT_FILE}")