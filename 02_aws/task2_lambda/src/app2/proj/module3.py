import logging
import requests

logging.basicConfig(level=logging.INFO)
logging.info(f"Using requests version: {requests.__version__}")

def fetch_status_code(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching URL {url}: {e}")
        return None

def is_url_accessible(url):
    return fetch_status_code(url) == 200

def count_valid_urls(urls):
    return sum(1 for url in urls if is_url_accessible(url))

def get_invalid_urls(urls):
    return [url for url in urls if not is_url_accessible(url)]

urls = ["https://www.google.com", "https://www.invalidurl.com", "invalid", "https://www.github.com"]

if __name__ == "__main__":
    valid_count = count_valid_urls(urls)
    invalid_urls = get_invalid_urls(urls)
    logging.info(f"Number of valid URLs: {valid_count}")
    logging.info(f"Invalid URLs: {invalid_urls}")
