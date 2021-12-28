from typing import TypedDict

class SearchEngine(TypedDict):
    """
    A custom dict type for DorkScan.\n
    Args:
        - base_url: str - "https://bing.com"
        - headers: 
    """
    base_url: str
    headers: dict[str, str]
    params: dict[str, str|int]
    soup_tag: str
    soup_class: str | dict