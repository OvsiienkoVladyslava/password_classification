import re
import pandas as pd


def extract_characters(input_data: str) -> pd.Series:
    """
    Extracting features from password:
     - its length;
     - number of digits;
     - number of uppercase letters;
     - number of lower case letters;
     - number of other symbols.

    :param input_data: password in string format.
    :return: pandas Series with generated features.
    """
    length = len(input_data)

    numbers = len(re.findall('[0-9]', input_data))
    upper = len(re.findall('[A-Z]', input_data))
    lower = len(re.findall('[a-z]', input_data))

    return pd.Series({
        'length': length,
        'numbers': numbers,
        'uppers': upper,
        'lowers': lower,
        'symbols': (length - numbers - upper - lower)
    })

