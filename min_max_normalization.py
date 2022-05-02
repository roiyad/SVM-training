import numpy as np



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
