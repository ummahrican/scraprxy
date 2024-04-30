import requests
import random
from scraprxy.proxy_scraper import scrape
from scraprxy.proxy_checker import check


def get(url, method="http", proxy=None):
    session = requests.Session()
    if not proxy:
        proxy = rotate_proxy(url, method)
    try:
        response = session.get(url, proxies={"http": f"{method}://{proxy}"}, timeout=30)
    except Exception as e:
        raise e
    return response


def rotate_proxy(url, method="http"):
    # create a tuple from unchecked and working sets
    available_proxies = check(scrape(method), method, url)
    if not available_proxies:
        raise Exception("no proxies available")
    return random.choice(available_proxies)


def main():
    result = get("http://ident.me/")
    print(result.status_code)  # 200
    print(result.text)  # 152.0.209.175


main()
