import numpy as np
from sklearn.preprocessing import OneHotEncoder



class ZScoreNormalizationStrategy:

    def __init__(self):
        pass

    """
    Normalize features.

    @return:  (normalized_train_x, normalized_test_x)
    """
    def normalize(self, train_x: np.ndarray, test_x: np.ndarray):
        all_x = np.concatenate((train_x, test_x))
        mean_ = np.mean(all_x, axis=0)
        std_ = np.std(all_x, axis=0)

        normalized_train_x = np.apply_along_axis(self._normalize_vector, 1, train_x, mean_, std_)
        normalized_test_x = np.apply_along_axis(self._normalize_vector, 1, test_x, mean_, std_)

        return normalized_train_x, normalized_test_x

    @staticmethod
    def _normalize_vector(vector: np.ndarray, mean_: np.ndarray, std_: np.ndarray):
        with np.errstate(divide='ignore', invalid='ignore'):
            normalized = (vector - mean_) / std_

        # set features where std==0 (meaningless features) as 0s, so they'll have no effect.
        normalized[np.isnan(normalized)] = 0

        return normalized

    @staticmethod
    def one_hot_encode_age(data):
        if data <= 17:
            return [1, 0, 0, 0, 0, 0, 0]
        elif data <= 22:
            return [0, 1, 0, 0, 0, 0, 0]
        elif data <= 40:
            return [0, 0, 1, 0, 0, 0, 0]
        elif data <= 51:
            return [0, 0, 0, 1, 0, 0, 0]
        elif data <= 59:
            return [0, 0, 0, 0, 1, 0, 0]
        elif data <= 68:
            return [0, 0, 0, 0, 0, 1, 0]
        else:
            return [0, 0, 0, 0, 0, 0, 1]
        return data
    @staticmethod
    def one_hot_encode_5(data, boundaries):
            if data <= boundaries[0]:
                return [1, 0, 0, 0, 0]
            elif data <= boundaries[1]:
                return [0, 1, 0, 0, 0]
            elif data <= boundaries[2]:
                return [0, 0, 1, 0, 0]
            elif data <= boundaries[3]:
                return [0, 0, 0, 1, 0]
            else :
                return [0, 0, 0, 0, 1]

    def one_hot_normilize_for_row(self, row):
            for i in range(14):
                if i == 0:
                    row[i] = self.one_hot_encode_age(row[i])
                elif i == 2:
                    row[i] = self.one_hot_encode_5(row[i], [110000, 159999, 196335, 259865])
                elif i == 10:
                    row[i] = self.one_hot_encode_5(row[i], [600, 1500, 4000, 7000])
                elif i == 11:
                    row[i] = self.one_hot_encode_5(row[i], [500, 1000, 2000, 3100])
                elif i == 12:
                    row[i] = self.one_hot_encode_5(row[i], [6, 40, 60, 80])
            flat_row = []
            for sublist in row:
                if type(sublist) != int:
                    for i in range(len(sublist)):
                        flat_row.append(sublist[i])
                else:
                    flat_row.append(sublist)
            return flat_row

    def one_hot_encode(self, data):
        modified_data = []
        for row in data:
            modified_data.append(self.one_hot_normilize_for_row(row))


        return modified_data




