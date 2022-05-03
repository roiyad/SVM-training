from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from single_point import values


class OneHotEncode:
    one_hot_encoders = []

    def __init__(self):
        for i in range(len(values)):
            if values[i] is not None:
                label_encoder = LabelEncoder()
                integer_encoded = label_encoder.fit_transform(values[i])
                integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
                one_hot_encoder = OneHotEncoder(sparse=False)
                one_hot_encoded = one_hot_encoder.fit_transform(integer_encoded)
                self.one_hot_encoders.append(one_hot_encoded)
            else:
                self.one_hot_encoders.append([])

    def one_hot_encode(self, data):
        """Encode the data by the OneHotEncoder"""
        modified_data = []
        for row in data:
            modified_data.append(self.one_hot_for_row(row))
        return modified_data

    def one_hot_for_row(self, row):
        """Encode data of a row """
        for i in range(len(row)):
            if i == 0:
                row[i] = self.find_value_boundaries(self, row[i], [17, 22, 40, 51, 59, 68])
            elif i == 2 or i == 3:
                continue
            elif i == 8:
                row[i] = self.find_value_boundaries(self, row[i], [600, 1500, 4000, 7000])
            elif i == 9:
                row[i] = self.find_value_boundaries(self, row[i], [500, 1000, 2000, 3100])
            elif i == 10:
                row[i] = self.find_value_boundaries(self, row[i], [6, 40, 60, 80])
            else:
                row[i] = self.categorical_hot_encode(i, row[i])
        flat_row = []
        for sublist in row:
            if type(sublist) != int:
                for i in range(len(sublist)):
                    flat_row.append(sublist[i])
            else:
                flat_row.append(sublist)
        return flat_row

    @staticmethod
    def find_value_boundaries(self, data, boundaries):
        """find the boundaries of the value for the OneHot Encoder"""
        dimension = len(boundaries)
        for i in range(dimension):
            if data <= boundaries[i]:
                return self.encode_continuous(i, dimension + 1)
        return self.encode_continuous(dimension, dimension + 1)

    @staticmethod
    def encode_continuous(index, dimension):
        """OneHot Encoder for continuous values"""
        result = [0] * dimension
        result[index] = 1
        return result

    def categorical_hot_encode(self, index, value):
        """Encode the categorical data by the OneHotEncoder"""
        return self.one_hot_encoders[index][value]
