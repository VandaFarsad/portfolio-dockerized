from typing import Iterable


def split_into_blocks(iterable: Iterable, sublist_len=3) -> list[list]:
    """Splitting an Iterable into a nested list, where each sub list has a fixed length."""
    return [iterable[i : i + sublist_len] for i in range(0, len(iterable), sublist_len)]  # noqa
