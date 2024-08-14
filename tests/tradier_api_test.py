import os

import pandas as pd
import pytest

from pytradier import TradierAPI
from pytradier.models import *


@pytest.fixture
def t():
    token = os.environ["TRADIER_TOKEN_SANDBOX"]
    account_id = os.environ.get("TRADIER_ACCOUNT_ID1")
    return TradierAPI(token=token, default_account_id=account_id, endpoint="sandbox")


@pytest.mark.parametrize(
    ("symbols", "greeks", "output_format"),
    (
        ("AAPL", False, "list"),
        (("AAPL", "MSFT", "NASYMBOL"), True, "df"),
    ),
)
def test_get_quotes(t: TradierAPI, symbols, greeks, output_format):
    quotes = t.get_quotes(symbols, greeks, output_format)
    if output_format == "df":
        assert isinstance(quotes, pd.DataFrame)
    else:
        assert isinstance(quotes, list)


@pytest.mark.parametrize(
    ("symbols", "interval", "start", "end", "output_format"),
    (
        (["AAPL", "MSFT"], "daily", None, None, "df"),
        (["AAPL", "MSFT"], "weekly", "2021-01-01", "2021-11-30", "dict"),
        ("AAPL", "weekly", "2020-10-20", "2021-11-28", "df"),
        ("AAPL", "monthly", "2020-01-01", None, "cls"),
    ),
)
def test_get_historical_quotes(
    t: TradierAPI, symbols, interval, start, end, output_format
):
    data = t.get_historical_quotes(symbols, interval, start, end, output_format)
    match output_format:
        case "df":
            assert isinstance(data, pd.DataFrame)
        case "dict":
            assert isinstance(data, dict)
        case "cls":
            assert isinstance(next(iter(data.values())), MarketsAPIResponse)
