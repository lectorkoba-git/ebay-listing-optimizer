# 🏷️ eBay AI Listing Optimizer: SEO Titles, Specifics & HTML Descriptions

[![eBay AI Listing Optimizer](https://apify.com/actor-badge?actor=magic-scraper/ebay-listing-optimizer)](https://apify.com/magic-scraper/ebay-listing-optimizer)
![Free Tier](https://img.shields.io/badge/Apify%20Free%20Tier-$5%20Monthly%20Credit-blue?style=flat-square)
![Pay-Per-Result](https://img.shields.io/badge/Pricing-$0.10%20%2F%20listing-blue?style=flat-square)
![No Cookies Required](https://img.shields.io/badge/Cookies-Not%20Required-success?style=flat-square)
![Export](https://img.shields.io/badge/Export-JSON%20|%20CSV%20|%20HTML-orange?style=flat-square)

Python, Node.js and REST examples for the **[eBay AI Listing Optimizer](https://apify.com/magic-scraper/ebay-listing-optimizer)** on Apify: optimize any eBay listing with AI. Enter one listing ID and get ten 78–80 character keyword titles, official category Item Specifics mapped from eBay's taxonomy, up to 5 photos analyzed via Vision AI, and a responsive HTML description ready to paste into eBay.

> ⚡ **No code needed:** 👉 **[Run it in your browser on Apify (free $5 monthly credit)](https://apify.com/magic-scraper/ebay-listing-optimizer)**

---

## 🎯 Who is this for?

- **eBay Sellers & Resellers:** Boost Cassini SEO ranking and search visibility with keyword-dense 78–80 character titles.
- **Listing Agencies & Virtual Assistants:** Automate listing optimization and copywriting across any eBay category.
- **Dropshippers:** Upgrade supplier descriptions into professional, branded HTML templates with verified specifics.
- **E-Commerce Automation:** Integrate listing optimization directly into your inventory software via REST API.

---

## 📌 Key Facts

| Feature | Details |
| :--- | :--- |
| **Pricing** | $0.10 per optimized listing + $0.00005 start fee; **50 free listing optimizations/month** with Apify's $5 free tier |
| **Ten 78–80 Chars Titles** | Generates 10 full-length candidate titles strictly adhering to eBay's 80-character maximum without cutting words |
| **Vision AI (up to 5 photos)** | Reads labels, OEM/MPN codes, barcodes, condition notes and materials directly from product images |
| **Official Taxonomy** | Automatically queries eBay's official Taxonomy API to extract required, recommended and allowed aspect values |
| **HTML Templates** | 4 customizable responsive layouts: `clean`, `technical`, `catalog`, and `premium` |
| **No API Key Required** | Built-in AI model, proxy rotation and eBay API handling are included in the price |
| **Fast Execution** | ~60–140 seconds per listing |

---

## 🚀 Quickstart

### Python

```bash
pip install apify-client
export APIFY_TOKEN="YOUR_APIFY_TOKEN"  # Get from https://console.apify.com/settings/integrations
python example.py
```

```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_TOKEN")

# Run the actor on a listing ID
run = client.actor("magic-scraper/ebay-listing-optimizer").call(run_input={
    "itemId": "168820368378",
    "descriptionTemplate": "clean",
    "analyzeImages": True
})

# Print results
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    opt = item["optimized_listing"]
    print("Optimized Title:", opt["optimized_title"])
    print("Length:", opt["title_length"])
    print("HTML Description:", opt["html_description"][:200], "...")
```

### Node.js / JavaScript

```bash
npm install apify-client
```

```javascript
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({
    token: process.env.APIFY_TOKEN || 'YOUR_APIFY_TOKEN',
});

const run = await client.actor('magic-scraper/ebay-listing-optimizer').call({
    itemId: '168820368378',
    descriptionTemplate: 'clean',
    analyzeImages: true,
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items[0].optimized_listing);
```

### cURL / REST API

```bash
curl "https://api.apify.com/v2/acts/magic-scraper~ebay-listing-optimizer/runs?token=YOUR_APIFY_TOKEN" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"itemId": "168820368378", "descriptionTemplate": "clean"}'
```

---

## 📥 Input Parameters

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `itemId` | String | *prefilled* | **Required.** 10–14 digit eBay item ID or `ebay.com/itm/...` listing URL. |
| `descriptionTemplate` | String | `"clean"` | HTML description style: `"clean"`, `"technical"`, `"catalog"`, `"premium"`. |
| `analyzeImages` | Boolean | `true` | Analyze up to 5 source photos using Vision AI for label and detail OCR. |
| `maxCompetitors` | Integer | `8` | Number of top competitor reference titles to analyze (3–10). |
| `itemTimeoutSecs` | Integer | `300` | Maximum execution time in seconds. |

---

## 📤 Sample Output

```json
{
  "item_id": "168820368378",
  "url": "https://www.ebay.com/itm/168820368378",
  "category": {
    "id": "176985",
    "name": "Vinyl Records"
  },
  "original_listing": {
    "title": "R.E.M. - The Best Of REM In Time 1988-2003, 2-LP 180-gram Vinyl, NEW",
    "title_length": 68,
    "price": 30.0,
    "condition": "New"
  },
  "optimized_listing": {
    "optimized_title": "R.E.M. - The Best Of R.E.M. In Time 1988-2003 2 LP 180g Vinyl Record New Sealed",
    "title_length": 79,
    "selected_title_index": 0,
    "title_candidates": [
      "R.E.M. - The Best Of R.E.M. In Time 1988-2003 2 LP 180g Vinyl Record New Sealed",
      "R.E.M. The Best Of R.E.M. In Time 1988-2003 2LP 180 Gram Vinyl Record New Sealed",
      "R.E.M. In Time: The Best of R.E.M. 1988-2003 2-LP 180g Vinyl Record New Sealed",
      "R.E.M. In Time: The Best of R.E.M. 1988-2003 2-LP 180g Vinyl Records New Sealed",
      "R.E.M. - The Best Of R.E.M. In Time 1988-2003 2-LP 180g Vinyl Record New Sealed",
      "R.E.M. - The Best Of R.E.M. In Time 1988-2003 2-LP 180g Vinyl Records New Sealed",
      "R.E.M. In Time: The Best of R.E.M. 1988-2003 2 LP 180g Vinyl Records New Sealed",
      "R.E.M. The Best Of R.E.M. In Time 1988-2003 2 LP Vinyl Record CR00188 New Sealed",
      "R.E.M. In Time 1988-2003 Greatest Hits 2 LP 180g Vinyl Record Album New Sealed",
      "R.E.M. In Time 1988-2003 Best Of 2 LP 180 Gram Vinyl Record Craft Recordings New"
    ],
    "clean_specifics": {
      "Artist": "R.E.M.",
      "Release Title": "In Time: The Best of R.E.M. 1988-2003",
      "Format": "Record",
      "Type": "Double LP",
      "Record Size": "12\"",
      "Speed": "33 RPM",
      "Record Label": "Craft Recordings",
      "Release Year": "2003",
      "Genre": "Rock",
      "Material": "Vinyl"
    },
    "html_description": "<!DOCTYPE html><html>...</html>",
    "audit_report_md": "# Listing Optimization Audit Report..."
  },
  "image_analysis": {
    "status": "analysed",
    "images": [
      "https://i.ebayimg.com/images/g/9hEAAOSw.../s-l1600.webp",
      "https://i.ebayimg.com/images/g/V~AAAOSw.../s-l1600.webp"
    ],
    "summary": "This item is a factory-sealed two-LP vinyl record album titled 'THE BEST OF R.E.M. IN TIME 1988-2003' by R.E.M., issued by Craft Recordings."
  },
  "processing_seconds": 71.9
}
```

---

## 🔗 Related E-Commerce Scrapers

- 📇 [eBay Seller Contact Scraper](https://apify.com/magic-scraper/ebay-seller-contact-scraper) — Extract business seller emails, phones, and company addresses from eBay items.
- 🏷️ [Etsy Bestsellers & Tags Scraper](https://apify.com/magic-scraper/etsy-bestsellers-tags-scraper) — Scrape trending Etsy items, prices, and SEO tags.
- 🛍️ [TikTok Shop Product Scraper](https://apify.com/magic-scraper/tiktok-shop-product-scraper) — Extract complete product data, variations, and seller details.

---

## 📜 License

MIT License. See [LICENSE](LICENSE) for details.
