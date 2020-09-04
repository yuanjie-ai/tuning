#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : tuning.
# @File         : nni_lgb
# @Time         : 2020/8/31 7:19 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 

import nni
import lightgbm as lgb
from sklearn.datasets import make_classification

X, y = make_classification(10 ** 4, 100, shift=0.3, random_state=666)
dtrain = lgb.Dataset(X, label=y)

params = {
    'boosting_type': 'gbdt',
    'objective': 'binary',
    'metric': {'auc', 'binary_loss'},
    'num_leaves': 31,
    'learning_rate': 0.05,
    'feature_fraction': 0.9,
    'bagging_fraction': 0.8,
    'bagging_freq': 5,
    'verbosity': -1
}


def run(params):
    r = lgb.cv(
        params, dtrain,
        num_boost_round=1000,
        nfold=5,
        verbose_eval=100,
        early_stopping_rounds=100
    )

    nni.report_final_result(r['auc-mean'][-1])


if __name__ == '__main__':
    RECEIVED_PARAMS = nni.get_next_parameter()
    print(params)
    params.update(RECEIVED_PARAMS)
    print(params)
    run(params)
