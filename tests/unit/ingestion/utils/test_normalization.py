import pytest
from ingestion.utils.normalization import normalize_company_name, normalize_text_field


@pytest.mark.unit
@pytest.mark.parametrize(
    "input_name, expected",
    [
        # Basic companies
        ("Microsoft Corporation", "microsoft"),
        ("Apple Inc.", "apple"),
        ("Tesla, Inc.", "tesla"),
        ("Johnson & Johnson", "johnson johnson"),
        (None, ""),  # None input
        # Punctuation and multiple spaces
        ("ACME, Inc.", "acme"),
        ("Foo-Bar Ltd.", "foo bar"),
        ("  Leading and trailing spaces Inc.  ", "leading and trailing spaces"),
        # Legal suffix variations
        ("Global Holdings LLC", "global llc"),  # note: LLC not in suffix list
        ("MegaCorp plc", "megacorp"),
        ("Example Co.", "example"),
        # Complex names
        (
            "Microsoft Global Finance Unlimited Company",
            "microsoft global finance unlimited",
        ),
        (
            "Kurv Yield Premium Strategy Microsoft (MSFT) ETF",
            "kurv yield premium strategy microsoft msft etf",
        ),
    ],
)
def test_normalize_company(input_name, expected):
    assert normalize_company_name(input_name) == expected


@pytest.mark.unit
@pytest.mark.parametrize(
    "input_value, expected",
    [
        ("Information Technology ", "information technology"),
        ("Software—Application", "software application"),
        ("Health Care", "health care"),
        ("  Consumer  Discretionary  ", "consumer discretionary"),
        (None, ""),
        ("", ""),
    ],
)
def test_normalize_text_field(input_value, expected):
    """
    Test normalization of sector/industry text fields.
    """
    assert normalize_text_field(input_value) == expected
