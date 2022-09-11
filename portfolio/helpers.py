from typing import Iterable

from django.db.models.query import QuerySet


def split_into_blocks(iterable: Iterable, sublist_len=3) -> list[list]:
    """Splitting an Iterable into a nested list, where each sub list has a fixed length."""
    return [iterable[i : i + sublist_len] for i in range(0, len(iterable), sublist_len)]


def split_paragraphs(content: str) -> list[str]:
    """Use this method and a for loop to add paragraphs in the template when using constance text fields."""
    return content.split(r"\p")
