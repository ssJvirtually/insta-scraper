import json
from typing import Dict
from urllib.parse import quote
import httpx
from http.server import BaseHTTPRequestHandler, HTTPServer

INSTAGRAM_APP_ID = "936619743392459"  # this is the public app id for instagram.com

class InstagramPostHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/scrape_post?url='):
            url_or_shortcode = self.path[len('/scrape_post?url='):]
            posts = self.scrape_post(url_or_shortcode)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(posts, indent=2, ensure_ascii=False).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found')

    def scrape_post(self, url_or_shortcode: str) -> Dict:
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

def run():
    print('Starting server...')
    server_address = ('', 9129)
    httpd = HTTPServer(server_address, InstagramPostHandler)
    print('Server running on port 9129')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
