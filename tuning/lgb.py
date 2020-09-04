from sklearn.datasets import make_classification
from sklearn.model_selection import StratifiedKFold
import optuna.integration.lightgbm as lgb

X, y = make_classification(10 ** 4, 100, shift=0.3, random_state=666)
dtrain = lgb.Dataset(X, label=y)

params = {
    "objective": "binary",
    "boosting_type": "gbdt",
    "metric": "auc",
    "n_jobs": 16,
    "verbosity": -1,
}

tuner = lgb.LightGBMTunerCV(
    params,
    dtrain,
    verbose_eval=100,
    early_stopping_rounds=100,
    folds=StratifiedKFold(5),
    show_progress_bar=False
)

tuner.run()

tuner.best_score
tuner.best_params
