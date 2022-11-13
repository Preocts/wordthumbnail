from __future__ import annotations

import re
from pathlib import Path
from string import punctuation


def read(filepath: str) -> str:
    """Read a given file in as a string."""
    return Path(filepath).read_text()


def remove_whitespace(text: str) -> str:
    """Remove all whitespace from text."""
    return re.sub(r"\s+", "", text)


def unify_whitespace(text: str) -> str:
    """All whitespace to a single space, trim leading and trailing."""
    return re.sub(r"\s+", " ", text).strip()


def count_characters(text: str) -> int:
    """Count all characters excluding punctuation."""
    match_group = re.escape("|".join(punctuation))
    no_punc = re.sub("[" + match_group + "]", "", text)
    return len(remove_whitespace(no_punc))


def count_words(text: str) -> int:
    """Count all words, regardless of length."""
    cleaned = unify_whitespace(text)
    return len(cleaned.split())
