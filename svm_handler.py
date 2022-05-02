from sklearn import svm
import min_max_normalization
from parse_data import parse_data
from tkinter import *
from tkinter import messagebox
from calc_error_pct import calculate_error_percentage


class SVMHandler:
    """ In this class you will implement the classifier and it's methods. """
    train_model_data = []
    test_model_data = []
    svc = 0  # just to initialize
    error_pct = 0
    coefficients = []
    normalizer = min_max_normalization.ZScoreNormalizationStrategy()

    def __init__(self):
        self.svc = svm.SVC()
        train_data_x, train_data_y = parse_data("C:\\Users\\roiya\\Downloads\\rnd_velis_ml_test (1)\\data\\adult.data")
        test_data_x, test_data_y = parse_data("C:\\Users\\roiya\\Downloads\\rnd_velis_ml_test (1)\\data\\adult.test")
        train_data_x = self.normalizer.one_hot_encode(train_data_x)
        test_data_x = self.normalizer.one_hot_encode(test_data_x)
        self.train_model_data = [train_data_x, train_data_y]
        self.test_model_data = [test_data_x, test_data_y]

    def train(self):
        svc_mod = self.svc.fit(self.train_model_data[0], self.train_model_data[1])
        self.coefficients = svc_mod.dual_coef_
        print(self.coefficients)
        print("finish training")

    def test(self):
        y_pred = self.svc.predict(self.test_model_data[0])
        self.error_pct = calculate_error_percentage(self.test_model_data[1], y_pred)
        print("finish testing")

    def get_result(self):
        return self.error_pct
