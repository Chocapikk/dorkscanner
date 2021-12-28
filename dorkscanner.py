#!/usr/bin/python3
""" DorkScanner
    - An atypical search engine scanner that scans search engines with queries you provide to find vulnerable URLs.
"""
import os
from dorkscan.dorkscan import DorkScan
from rich.console import Console
from utils import (fix_name, load_dorks)


class DorkScanner:

    banner: str = """
        ░█▀▄░█▀█░█▀▄░█░█░█▀▀░█▀▀░█▀█░█▀█░█▀█░█▀▀░█▀▄
        ░█░█░█░█░█▀▄░█▀▄░▀▀█░█░░░█▀█░█░█░█░█░█▀▀░█▀▄
        ░▀▀░░▀▀▀░▀░▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀░▀░▀░▀░▀▀▀░▀░▀
            ___________________________
    """

    def __init__(
        self,
        engine: str = "BING",
        pages: int = 1,
        query: str | None = None,
        dorks: str | None = None,
        outfile: str | None = None,
    ) -> None:
        self.console = Console()
        self.pages = pages
        self.engine = engine
        if dorks is not None:
            self.search = load_dorks(fix_name(dorks))
        elif query is not None:
            self.search = [query]
        else:
            raise ValueError("No<dorks> or <query> argument detected!")
        if outfile is not None:
            self.outfile = fix_name(outfile)
        self.console.print(DorkScanner.banner, style="bold white")

    def run(self):
        self.results = DorkScan(self.engine, self.pages, self.search)
        self.console.print(
            self.results,
            style="bold green",
        )

    def export(self):
        pass
            


if __name__ == "__main__":
    scan = DorkScanner(dorks="tests/dorks/dorks.txt", pages=1)
    scan.run()
