def split_into_blocks(iterable: list, sublist_len=3) -> list[list]:
    """Return a new list of sublists, where each sublist contains <sublist_len> number of elements from the original
    iterable list. The sublists are created by splitting the iterable list into chunks of <sublist_len> elements.

    If the length of the iterable list is not divisible by <sublist_len>, the last sublist will contain the remaining
    elements.
    """
    return [iterable[i : i + sublist_len] for i in range(0, len(iterable), sublist_len)]
