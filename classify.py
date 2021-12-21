import argparse
import pandas as pd
import numpy as np

from data_preprocessing import extract_characters


def process_input(options: argparse.Namespace):
    data = pd.read_csv(options.source, names=['password'])

    data['password'] = data['password'].astype(str)
    X = data['password'].apply(extract_characters)

    predictions = predict(X.to_numpy())

    predictions_frame = data.copy()
    predictions_frame['strength'] = predictions

    if options.save_txt:
        predictions_frame.to_csv(options.save_path, index=False)
    else:
        pd.set_option('display.max_rows', None)
        print(predictions_frame)


def predict(input_data: np.ndarray):
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, default='', help='file with passwords which start from new line')
    parser.add_argument('--save-txt', type=bool, default=False,
                        help='to save or not to save predictions in .csv (bool)')
    parser.add_argument('--save-path', type=str, default='', help='path where to save predicted classes')
    opt = parser.parse_args()

    process_input(opt)
