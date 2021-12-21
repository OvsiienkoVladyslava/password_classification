import argparse
import pandas as pd
import numpy as np
import pickle
import xgboost

from data_preprocessing import extract_characters


def process_input(options: argparse.Namespace):
    data = pd.read_csv(options.source, names=['password'])

    data['password'] = data['password'].astype(str)
    X = data['password'].apply(extract_characters)

    predictions = predict(X.to_numpy())

    predictions_frame = data.copy()
    predictions_frame['strength'] = predictions
    predictions_frame['strength'] = predictions_frame['strength'].map({
        0: 'weak',
        1: 'medium',
        2: 'strong'
    })

    if options.save_file:
        predictions_frame.to_csv(options.save_path + '/predictions.csv', index=False)
    else:
        pd.set_option('display.max_rows', None)
        print(predictions_frame)


def predict(input_data: np.ndarray):
    xgb_model_loaded = xgboost.XGBClassifier()
    xgb_model_loaded.load_model('./xgbclassifier')
    predictions = xgb_model_loaded.predict(input_data)

    return predictions


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, default='', help='file with passwords which start from new line')
    parser.add_argument('--save-file', type=int, default=0,
                        help='to save or not to save predictions in .csv (1 - yes, 0 - no)')
    parser.add_argument('--save-path', type=str, default='.', help='path where to save predicted classes file '
                                                                  'predictions.csv')
    opt = parser.parse_args()
    process_input(opt)
