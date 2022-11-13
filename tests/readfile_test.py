from __future__ import annotations

from pathlib import Path
from string import punctuation

import pytest
from wordthumbnail import readfile

FIXTURE_PATH = "tests/fixture.txt"
FIXTURE_TEXT = Path(FIXTURE_PATH).read_text()


def test_read() -> None:
    text = readfile.read(FIXTURE_PATH)

    assert text == FIXTURE_TEXT


@pytest.mark.parametrize(
    ("text", "expected"),
    (
        ("this\t", "this"),
        ("this \n that", "thisthat"),
        ("\t\n \t\n   ", ""),
    ),
)
def test_remove_whitespace(text: str, expected: str) -> None:
    cleaned = readfile.remove_whitespace(text)

    assert cleaned == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    (
        ("this\t", "this"),
        ("this \n that", "this that"),
        ("\t\n \t\n   ", ""),
    ),
)
def test_unify_whitespace(text: str, expected: str) -> None:
    cleaned = readfile.unify_whitespace(text)

    assert cleaned == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    (
        ("this\t", 4),
        ("this \n that", 8),
        (punctuation, 0),
        (FIXTURE_TEXT, 4058),
    ),
)
def test_count_characters(text: str, expected: int) -> None:
    count = readfile.count_characters(text)

    assert count == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    (
        ("Two   words", 2),
        ("a four \tword test", 4),
        (FIXTURE_TEXT, 817),
    ),
)
def test_count_words(text: str, expected: int) -> None:
    count = readfile.count_words(text)

    assert count == expected
