# Instagram Scraper

This project contains Python scripts to scrape data from Instagram posts. It provides tools to fetch post details either directly via a script or through a simple web server.

## `instascrape.py`

This script scrapes data from a single Instagram post using its URL or shortcode.

### Dependencies
- `httpx`

### Usage
1.  **Install dependencies:**
    ```bash
    pip install httpx
    ```
2.  **Modify the script:**
    Open `instascrape.py` and change the `url_or_shortcode` variable in the example usage section at the bottom of the file to the URL or shortcode of the Instagram post you want to scrape.
    ```python
    # Example usage:
    posts = scrape_post("YOUR_INSTAGRAM_POST_URL_OR_SHORTCODE_HERE") # <-- Change this line
    print(json.dumps(posts, indent=2, ensure_ascii=False))
    ```
3.  **Run the script:**
    ```bash
    python instascrape.py
    ```
    The script will print the scraped post data in JSON format to the console.

## `instascrape_with_server.py`

This script runs a simple HTTP server that allows you to scrape Instagram post data by making a GET request.

### Dependencies
- `httpx`

### Usage
1.  **Install dependencies (if not already installed):**
    ```bash
    pip install httpx
    ```
2.  **Run the server:**
    ```bash
    python instascrape_with_server.py
    ```
    The server will start and listen on port 9129 by default.
3.  **Scrape a post:**
    Open your web browser or use a tool like `curl` to make a GET request to the server:
    ```bash
    curl "http://localhost:9129/scrape_post?url=YOUR_INSTAGRAM_POST_URL_OR_SHORTCODE_HERE"
    ```
    Replace `YOUR_INSTAGRAM_POST_URL_OR_SHORTCODE_HERE` with the actual URL or shortcode of the Instagram post. The server will return the scraped post data in JSON format.

## `repy.py`

This script appears to be an alternative or experimental method for interacting with Instagram's GraphQL API. It contains many hardcoded headers and request parameters. 

**Note:** This script might require significant modification (e.g., updating tokens, headers, and request details) to work correctly and is likely not suitable for general use in its current state.

## Disclaimer

Scraping data from websites like Instagram can be against their Terms of Service. Users of this project should be aware of Instagram's policies and use these scripts responsibly. The authors of this project are not responsible for any misuse or consequences of using these scripts.

## Dependencies

The primary dependency for these scripts is `httpx`.

You can install it using pip:
```bash
pip install httpx
```
