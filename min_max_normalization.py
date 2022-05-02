from typing import Tuple
import numpy as np


class MinMaxNormalizationStrategy():

    def __init__(self, min_, max_):
        self._min = min_
        self._max = max_

    def normalize(self, train_x, test_x):
        all_x = np.concatenate((train_x, test_x))
        current_min = np.amin(all_x, axis=0)
        current_max = np.amax(all_x, axis=0)
        new_min = np.tile(self._min, len(current_min))
        new_max = np.tile(self._max, len(current_min))

        normalized_train_x = np.apply_along_axis(self._normalize_vector, 1, train_x,
                                                 current_min, current_max, new_min, new_max)
        normalized_test_x = np.apply_along_axis(self._normalize_vector, 1, test_x,
                                                current_min, current_max, new_min, new_max)

        return normalized_train_x, normalized_test_x

    @staticmethod
    def _normalize_vector(vector: np.ndarray, current_min: np.ndarray, current_max: np.ndarray,
                          new_min: np.ndarray, new_max: np.ndarray):
        with np.errstate(divide='ignore', invalid='ignore'):
            normalized = ((vector - current_min) / (current_max - current_min)) * (new_max - new_min) + new_min

        # set features where current_min == current_max (meaningless features) as 0s, so they'll have no effect.
        normalized[np.isnan(normalized)] = 0

        return normalized