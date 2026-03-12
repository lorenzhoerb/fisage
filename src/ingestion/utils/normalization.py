import re

import pandas as pd

LEGAL_SUFFIXES = [
    "inc",
    "inc.",
    "corp",
    "corp.",
    "corporation",
    "ltd",
    "ltd.",
    "limited",
    "co",
    "co.",
    "company",
    "plc",
    "holdings",
    "holding",
    "group",
]


def normalize_company_name(name: str) -> str:
    """
    Normalize a company name: lowercase, remove punctuation and common legal suffixes.

    Args:
        name (str): Company name, can be None or NaN.

    Returns:
        str: Cleaned name, empty string if input is None/NaN.
    """
    if pd.isna(name):
        return ""

    name = name.lower()

    # remove punctuation
    name = re.sub(r"[^\w\s]", " ", name)

    # remove legal suffixes
    words = name.split()
    words = [w for w in words if w not in LEGAL_SUFFIXES]

    name = " ".join(words)

    # collapse multiple spaces
    name = re.sub(r"\s+", " ", name)

    return name


def normalize_text_field(value: str) -> str:
    """
    Normalize a text field like sector or industry: lowercase, remove punctuation,
    and collapse multiple spaces.

    Args:
        value (str): Input string, can be None or NaN.

    Returns:
        str: Cleaned string, empty if input is None/NaN.
    """
    if pd.isna(value):
        return ""

    value = value.lower()
    value = re.sub(r"[^\w\s]", " ", value)  # remove punctuation
    value = re.sub(r"\s+", " ", value)  # collapse multiple spaces
    return value.strip()
