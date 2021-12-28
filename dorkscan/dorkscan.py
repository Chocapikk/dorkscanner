#!/usr/bin/python3
""" DorkScanner
    - An atypical search engine scanner that scans search engines with queries you provide to find vulnerable URLs.
"""
from requests.models import HTTPError
from dorkscan.network import (
    connection_test,
    load_engine,
    fetch
)
import concurrent.futures
from rich.progress import Progress

# TODO: add console arg - default to new gen
def DorkScan(search_engine: str="BING", pages: int=1, dorks: list = []) -> list[dict]:
    """
        Scrape a search engine result page for (potentially) vulnerably sites.\n
        Args:
            - search_engine: str - Bing / Ask/ Wow
            
        Notes\n
            - Add a search_engine by adding a SearchEngine type dict to load_engine()
        Defaults:
            DorkScan(search_engine: str="BING", pages: int=1, dorks: list = [])
    """

    if not connection_test():
        raise HTTPError("Failed to ping google.com")


    # TODO: add clean decorator scan for list or strs

    """
        scan fetches and parses the search engine pages.\n
        The main loop revolves around threading multiple dorks.\n
        Each iteration create a new SearchEngine object which is passed to fetch().
        - fetch_filter() will validate SERP links to make sure they contain query parameters. It will return a dict[dork, valid_urls]
    """
    final = []
    # TODO: overall progress
    for page in range(1, pages+1):
        results = []
        with Progress() as progress:
            task = progress.add_task(f"Dorking {search_engine} page {page}: ", total=len(dorks))
            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = []
                for dork in dorks:
                    engine = load_engine(search_engine, dork, page)
                    futures.append(executor.submit(fetch, engine=engine))
                for future in concurrent.futures.as_completed(futures):
                    results.append(future.result())
                    progress.advance(task)
    
        final.append({"page": page, "results": [result for result in results if len(result["urls"]) > 0]})
    return final
