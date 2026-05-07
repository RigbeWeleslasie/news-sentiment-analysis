import pytest
import pandas as pd
import os

def test_raw_data_exists():
    assert os.path.exists('data/raw/raw_analyst_ratings.csv')

def test_data_loads():
    df = pd.read_csv('data/raw/raw_analyst_ratings.csv')
    assert df.shape[0] > 0
    assert 'headline' in df.columns
    assert 'stock' in df.columns
    assert 'date' in df.columns
