#!/usr/bin/python3
""" DorkScanner
    - An atypical search engine scanner that scans search engines with queries you provide to find vulnerable URLs.
"""
import requests
from bs4 import BeautifulSoup as bsoup
from requests.models import HTTPError
from utils.network import (
    connection_test,
    new_user_agent,
    bad_urls
    )
from utils.typings import SearchEngine
from utils.files import load_dorks
import concurrent.futures
import re

class DorkScan():
    """ Scrape a search engine result page for (potentially) vulnerably sites.\n
    Notes\n
        - DorkScan can be imported and used on it's own or with the accompanying CLI child class DorkScanner.\n
        - DorkScan requires a list of dork strings. Even a list of 1.
        - Please refer to utils.typing.SearchEngine to make customizations.\n
    Defaults:
        DorkScan(search_engine: str="BING", pages: int=1, dorks: list = [])
    """
    def __init__(self, search_engine: str="BING", pages: int=1, dorks: list = []) -> None:
        self.engine_name = search_engine
        self.serp_pages = pages
        self.dorks = dorks
        if not connection_test():
            raise HTTPError("Failed to ping google.com")
        # HACK: remove printout debug
        print(self.scan())

    def scan(self):
        """ scan fetches and parses the search engine pages.\n
        The main loop revolves around threading multiple dorks.\n
        Each iteration create a new SearchEngine object which is passed to fetch().
            - fetch() is includes a decorator for verify / clean results.
        """
        results = []
        @self.dork_results
        def fetch(engine: SearchEngine):
            """ Fetch is a function within scan() GET's and parses SERPs.\n
                Args:
                    - engine: just use DorkScan.load_engine()
            """
            try:
                resp = requests.get(engine["base_url"], params=engine["params"], headers=engine["headers"])
                soup = bsoup(resp.text, "html.parser")
                links = soup.findAll(engine["soup_tag"],engine["soup_class"])
                return  [link.text for link in links]
            except:
                pass

        for page in range(self.serp_pages, self.serp_pages+1):
            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = []
                for dork in self.dorks:
                    engine = DorkScan.load_engine(self.engine_name, dork, page)
                    futures.append(executor.submit(fetch, engine=engine))
                for future in concurrent.futures.as_completed(futures):
                    results.append(future.result())

            return [result for result in results if len(result) >= 1]

    @staticmethod
    def load_engine(engine: str, dork: str, page: int) -> SearchEngine|ValueError:
        """ load_engine() returns a SearchEngine type for the dork iteration. Currently supported engines are (Bing, Wow, Ask). \nPlease see utils.typings for further details.
        """
        search_engines: dict[str, SearchEngine] = {
            "ASK": {
                "base_url": "https://www.ask.com/web",
                "headers": new_user_agent(),
                "params": {"q": dork, "page": page},
                "soup_tag": "div",
                "soup_class": {
                    "class": "PartialSearchResults-item-url PartialSearchResults-item-top-url"
                },

            },
            "BING": {
                "base_url": "https://www.bing.com/search",
                "headers": new_user_agent(),
                "params": {"q": dork, "first": page * 10 + 1},
                "soup_tag": "cite",
                "soup_class": "",

            },
            "WOW": {
                "base_url": "https://www.wow.com/search",
                "headers": new_user_agent(),
                "params": {"q": dork, "b": page * 8},
                "soup_tag": "span",
                "soup_class": {"class": "fz-ms fw-m fc-12th wr-bw lh-17"},

            },
        }
        match engine.upper():
            case "BING":
                return search_engines["BING"]
            case "ASK":
                return search_engines["ASK"]
            case "WOW":
                return search_engines["WOW"]
            case _:
                return ValueError(f"{engine} is not supported")

    @staticmethod
    #TODO: return a dict{dork: urls}
    def dork_results(func):
        def validate(*args, **kwargs):
            prelim_results = func(*args, **kwargs)
            blacklist = re.compile("|".join(bad_urls))
            return [url for url in prelim_results if not re.search(blacklist, url) and re.search(r"\?.+\=", url)]
        return validate


class DorkScanner(DorkScan):
    """ DorkScanner is a tool used to dork & scrape search engines. DorkScanner is the CLI tool. DorkScan is a the tool that handles the search and parsing.

        TODO: CLI Example
        TODO: Import DorkScan usage()
    """

    banner: str = """
            ·▄▄▄▄        ▄▄▄  ▄ •▄     .▄▄ ·  ▄▄·  ▄▄▄·  ▐ ▄  ▐ ▄ ▄▄▄ .▄▄▄  
            ██▪ ██ ▪     ▀▄ █·█▌▄▌▪    ▐█ ▀. ▐█ ▌▪▐█ ▀█ •█▌▐█•█▌▐█▀▄.▀·▀▄ █·
            ▐█· ▐█▌ ▄█▀▄ ▐▀▀▄ ▐▀▀▄·    ▄▀▀▀█▄██ ▄▄▄█▀▀█ ▐█▐▐▌▐█▐▐▌▐▀▀▪▄▐▀▀▄ 
            ██. ██ ▐█▌.▐▌▐█•█▌▐█.█▌    ▐█▄▪▐█▐███▌▐█ ▪▐▌██▐█▌██▐█▌▐█▄▄▌▐█•█▌
            ▀▀▀▀▀•  ▀█▄▀▪.▀  ▀·▀  ▀     ▀▀▀▀ ·▀▀▀  ▀  ▀ ▀▀ █▪▀▀ █▪ ▀▀▀ .▀  ▀

                        Made By : Balgogan (https://github.com/Balgogan)
                        *** *  * ** * ** * *** *  * ** * ** * *** ** * *
                        *    *      * *  *  *    *      * *  * *    * *
                        *   *   *        *   *   *       *   *   *
                        *         *    *        *         *    *
                            *    *   *     *    *   * *  *    *   *
                                    *      *     *       *       *
        """

    def __init__(self, search_engine: str="BING", pages: int=1, query: str|None=None, dorks: str|None=None, outfile: str|None = None) -> None:
        self.pages = pages
        if dorks is not None:
            self.search = load_dorks(dorks)
        elif query is not None:
            self.search = [query]
        else:
            self.search = load_dorks("dorks.txt")
        if outfile is not None:
            self.outfile = outfile

    def run(self):
        pass


if __name__ == "__main__":
    scan = DorkScan(dorks=load_dorks("tests/dorks/dorks.txt"))
