import argparse
import pandas as pd
import numpy as np
import xgboost

from data_preprocessing import extract_characters


def process_input(options: argparse.Namespace):
    """
    Processes parsed arguments, prepare data for predicting, predict password strength,
    save predictions in file/print predictions in terminal

    :param options: options consists of source filepath, results filepath
    and label to save file with predictions (0 or 1) in format argparse Namespace
    """
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


def predict(input_data: np.ndarray) -> np.ndarray:
    """
    Predicts password strength by loaded model 'xgbclassifier'

    :param input_data: passwords features(length, number of digits, uppercase and lowercase letters, other symbols)
     in numpy array format
    :return: array of predicted password strength (0 - weak, 1 - medium, 2 - strong)
    """
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
