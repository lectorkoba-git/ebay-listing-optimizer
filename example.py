"""
Example: Optimize an eBay listing with AI via Apify Python Client.
Requires: pip install apify-client
"""
import os
from apify_client import ApifyClient

# Replace with your Apify API Token or set APIFY_TOKEN environment variable
APIFY_TOKEN = os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN")

client = ApifyClient(APIFY_TOKEN)

run_input = {
    # Provide 1 to 10 eBay Item IDs or full listing URLs (processed in parallel)
    "itemIds": [
        "168820368378",
        "227470769942",
    ],
    "descriptionTemplate": "clean",
    "analyzeImages": True,
}

print("🚀 Launching eBay AI Listing Optimizer on Apify Cloud...")
run = client.actor("magic-scraper/ebay-listing-optimizer").call(run_input=run_input)

print(f"✅ Run finished with status: {run.get('status')}")
print("📊 Generated Listing Optimization:\n")

dataset_id = run["defaultDatasetId"]
for item in client.dataset(dataset_id).iterate_items():
    orig = item.get("original_listing", {})
    opt = item.get("optimized_listing", {})

    print(f"Item ID: {item.get('item_id')}")
    print(f"  Original Title ({len(orig.get('title', ''))} chars):  {orig.get('title')}")
    print(f"  Optimized Title ({opt.get('title_length')} chars): {opt.get('optimized_title')}")
    print("\n  Top Title Candidates (78-80 chars):")
    for idx, c in enumerate(opt.get("title_candidates", [])[:5]):
        print(f"    [{idx + 1}] ({len(c)} chars): {c}")

    print(f"\n  Official Item Specifics ({len(opt.get('clean_specifics', {}))} fields):")
    for k, v in list(opt.get("clean_specifics", {}).items())[:8]:
        print(f"    • {k}: {v}")

    html = opt.get("html_description", "")
    print(f"\n  HTML Description: {len(html)} characters (ready to copy into eBay)")
    print(f"  Processing Time: {item.get('processing_seconds', 0):.1f}s\n")
