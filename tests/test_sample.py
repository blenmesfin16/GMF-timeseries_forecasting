import pytest
import pandas as pd
import numpy as np

def test_pandas_import():
    """Test that pandas can be imported"""
    import pandas as pd
    assert pd.__version__ is not None

def test_numpy_import():
    """Test that numpy can be imported"""
    import numpy as np
    assert np.__version__ is not None

def test_data_loading():
    """Test that data files can be loaded"""
    try:
        df = pd.read_csv('data/processed/combined_adj_close_clean.csv')
        assert len(df) > 0
    except FileNotFoundError:
        pytest.skip("Data file not found - skipping test")

def test_data_columns():
    """Test that data has expected columns"""
    try:
        df = pd.read_csv('data/processed/combined_adj_close_clean.csv')
        expected_columns = ['TSLA', 'BND', 'SPY']
        for col in expected_columns:
            assert col in df.columns
    except FileNotFoundError:
        pytest.skip("Data file not found - skipping test")