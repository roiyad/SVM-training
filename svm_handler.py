from sklearn import svm
import onehotencode
from parse_data import parse_data
from calc_error_pct import calculate_error_percentage
import os
# model parameters
C_VALUE = 0.01


class SVMHandler:
    """ In this class you will implement the classifier and it's methods. """
    train_data = []
    test_data = []
    svc = 0  # just to initialize
    error_pct = 0
    coefficients = []

    def __init__(self):
        self.svc = svm.LinearSVC(C=C_VALUE, penalty='l2', loss='squared_hinge')
        onehot = onehotencode.OneHotEncode()
        self.train_data, self.test_data = self.read_data(onehot)

    @staticmethod
    def read_data(onehot):
        file = os.path.dirname(__file__)

        train_data_x, train_data_y = parse_data("C:\\Users\\roiya\\Downloads\\rnd_velis_ml_test (1)\\data\\adult.data")
        test_data_x, test_data_y = parse_data("C:\\Users\\roiya\\Downloads\\rnd_velis_ml_test (1)\\data\\adult.test")
        train_data_x = onehot.one_hot_encode(train_data_x)
        test_data_x = onehot.one_hot_encode(test_data_x)
        return [train_data_x, train_data_y], [test_data_x, test_data_y]

    def train(self):
        svc_mod = self.svc.fit(self.train_data[0], self.train_data[1])
        self.coefficients = svc_mod.coef_
        print("Coefficients: ", self.coefficients)
        print("Finished training")

    def test(self):
        y_vector = self.svc.predict(self.test_data[0])
        self.error_pct = calculate_error_percentage(y_vector, self.test_data[1])
        print("Finished testing")
        print(self.error_pct)

    def get_result(self):
        return self.error_pct
