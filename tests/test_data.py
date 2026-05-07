
import pytest
import pandas as pd
import numpy as np


def test_pandas_import():
    assert pd.__version__ is not None


def test_numpy_import():
    assert np.__version__ is not None


def test_dataframe_creation():
    df = pd.DataFrame({
        'headline': ['test headline'],
        'stock': ['AAPL'],
        'date': ['2020-01-01']
    })
    assert df.shape == (1, 3)
    assert 'headline' in df.columns


def test_headline_length():
    df = pd.DataFrame({'headline': ['Apple hits 52-week high']})
    df['headline_length'] = df['headline'].astype(str).apply(len)
    assert df['headline_length'][0] == 23
