# tuning

 nnictl experiment save mmTt074m -s # -s是否保存代码

 # -c解压代码到指定目录
 nnictl experiment load -p nni_experiment_mmTt074m.zip -c ./

https://nni.readthedocs.io/en/latest/Tutorial/ExperimentConfig.html#logdir
https://github.com/microsoft/nni/blob/v1.8/examples/notebooks/retrieve_nni_info_with_python.ipynb
- xgb
- lgb
- catboost

https://github.com/optuna/optuna/tree/master/examples
---
https://www.kaggle.com/corochann/optuna-tutorial-for-hyperparameter-optimization
https://optuna.readthedocs.io/en/latest/faq.html#how-to-define-objective-functions-that-have-own-arguments
https://github.com/optuna/optuna/blob/master/examples/pruning/xgboost_integration.py