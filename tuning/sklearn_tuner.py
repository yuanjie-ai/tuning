import sklearn
import sklearn.datasets
from sklearn import ensemble
from sklearn.ensemble import *

from sklearn.model_selection import cross_val_score
import sklearn.svm
import optuna

# TODO
"""
sklearn classifier models
# 设置模型对应的参数集合
model_name: params

"""


class Objective(object):
    def __init__(self, X, y, cv=3):
        self.X, self.y = X, y
        self.cv = cv

    def __call__(self, trial: optuna.trial.Trial):

        classifier_name = trial.suggest_categorical("classifier", ["SVC", "RandomForest"])
        if classifier_name == "SVC":
            svc_c = trial.suggest_float("svc_c", 1e-10, 1e10, log=True)
            classifier_obj = sklearn.svm.SVC(C=svc_c, gamma="auto")
        else:
            rf_max_depth = trial.suggest_int("rf_max_depth", 2, 32, log=True)
            classifier_obj = ensemble.RandomForestClassifier(
                max_depth=rf_max_depth, n_estimators=10
            )

        score = cross_val_score(classifier_obj, self.X, self.y, n_jobs=1, cv=self.cv)
        accuracy = score.mean()
        return accuracy

    def create_model(self, trial):
        rf_max_depth = trial.suggest_int("rf_max_depth", 2, 32, log=True)
        model = ensemble.RandomForestClassifier(
            max_depth=rf_max_depth, n_estimators=10
        )
        return model


max_depth = trial.suggest_int("max_depth", 2, 32)
n_estimators = trial.suggest_int("n_estimators", 2, 500)
min_samples_leaf = trial.suggest_int("min_samples_leaf", 1, 10)
model = RandomForestClassifier(
    min_samples_leaf=min_samples_leaf, n_estimators=n_estimators, max_depth=max_depth, random_state=0
)

if __name__ == "__main__":
    # Load the dataset in advance for reusing it each trial execution.
    iris = sklearn.datasets.load_iris()
    objective = Objective(iris)

    study = optuna.create_study(direction="maximize")
    study.optimize(objective, n_trials=100)
    print(study.best_trial)
