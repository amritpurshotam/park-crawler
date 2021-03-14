import random
import time

import requests


def get(url: str):

    dummy_user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",  # noqa: B950
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",  # noqa: B950
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0",  # noqa: B950
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/605.1 Edge/19.17763",  # noqa: B950
    ]

    proxies = [
        "http://105.247.67.35:8080",
        "http://105.255.223.2:8080",
        "http://178.62.29.166:8080",
        "http://138.68.165.154:8080",
    ]

    req = requests.get(
        url,
        headers={"user-agent": random.choice(dummy_user_agents)},  # noqa: S311
        proxies={"http": random.choice(proxies)},  # noqa: S311
    )

    result = req.text
    time.sleep(4)
    return result
