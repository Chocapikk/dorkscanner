import requests
from random import randint

def connection_test() -> bool:
    if requests.get("http://www.google.com", timeout=5000):
        return True
    else:
        return False

def new_user_agent() -> dict[str, str]:
            """returns a header dictionary with a random User-Agent"""
            user_agents: list[str] = [
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
                "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
                "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/13.2b11866 Mobile/16A366 Safari/605.1.15",
                "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1",
                "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1",
                "Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0",
            ]
            return {"User-Agent": user_agents[randint(0, len(user_agents)-1)]}
        
"""def dork_results(func):
    def validate():
        prelim_results = func()
        blacklist = re.compile("|".join(bad_urls))
        results = [url for url in prelim_results if not re.search(blacklist, link) and re.search(r"\?.+\=", line)]
            return link"""
    
bad_urls: list[str] = [
        "facebook",
        "google",
        "pastebin",
        "gist",
        "github",
        "udemy",
        "jetbrains",
        "youtube",
        "whatsapp",
        "telegram",
        "twitter",
        "vuldb",
        "tenable",
        "exploit-db",
        "stackoverflow",
        "bing",
        "w3schools",
        "wikipedia",
        "cvedetails",
        "exploitdb",
    ]