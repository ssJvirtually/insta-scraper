import json
from typing import Dict
from urllib.parse import quote

import httpx

INSTAGRAM_APP_ID = "936619743392459"  # this is the public app id for instagram.com


def scrape_post(url_or_shortcode: str) -> Dict:
    """Scrape single Instagram post data"""
    if "http" in url_or_shortcode:
        shortcode = url_or_shortcode.split("/p/")[-1].split("/")[0]
    else:
        shortcode = url_or_shortcode
    print(f"scraping instagram post: {shortcode}")

    variables = {
        "shortcode": shortcode,
        "child_comment_count": 20,
        "fetch_comment_count": 100,
        "parent_comment_count": 24,
        "has_threaded_comments": True,
    }
    url = "https://www.instagram.com/graphql/query/?query_hash=b3055c01b4b222b8a47dc12b090e4e64&variables="
    result = httpx.get(
        url=url + quote(json.dumps(variables)),
        headers={"x-ig-app-id": INSTAGRAM_APP_ID},
    )
    data = json.loads(result.content)
    return data["data"]["shortcode_media"]

# Example usage:
posts = scrape_post("https://www.instagram.com/p/CqKzGFxDs0i/")
print(json.dumps(posts, indent=2, ensure_ascii=False))