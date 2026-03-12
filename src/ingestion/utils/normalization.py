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
