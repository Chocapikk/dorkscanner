from typing import TypedDict


class SearchEngine(TypedDict):
    base_url: str
    headers: dict[str, str]
    params: dict[str, str|int]
    soup_tag: str
    soup_class: str | dict