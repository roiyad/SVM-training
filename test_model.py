from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.svm import LinearSVC

import svm_handler
from calc_error_pct import calculate_error_percentage


def optimize_svm():
    """ I used this function to find the best hyper parameters for the model
    """
    param_grid = {'C': [0.01, 0.1, 1, 10, 100], 'max_iter': [1000, 10000, 100000],\
                  'loss': ['squared_hinge', 'hinge'], 'penalty': ['l1', 'l2'],\
                  'dual': ['True', 'False']}
    svm = svm_handler.SVMHandler()
    grid = GridSearchCV(LinearSVC(), param_grid, refit=True, verbose=3)
    x, y = svm.train_data
    grid.fit(x, y)
    print(grid.best_params_)
    print(grid.best_estimator_)
    print(grid.best_score_)
    x_test , y_test = svm.test_data
    grid_predictions = grid.predict(x_test)
    print(confusion_matrix(y_test, grid_predictions))
    print(classification_report(y_test, grid_predictions))
    print(calculate_error_percentage(grid_predictions, y_test))


optimize_svm()



