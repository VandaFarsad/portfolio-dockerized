from django.db.models.query import QuerySet


def split_into_blocks(objects: QuerySet, sublist_len: int = 3) -> list:
    """Splitting a list into a nested list, where each sub list has a fixed length."""
    return [objects[i : i + sublist_len] for i in range(0, len(objects), sublist_len)]


def split_paragraphs(content: str) -> list[str]:
    """Use this method and a for loop to add paragraphs in the template when using constance text fields."""
    return content.split(r"\p")
