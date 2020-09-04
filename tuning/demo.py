#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : tuning.
# @File         : demo
# @Time         : 2020/9/4 4:01 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 

# "RandomForestClassifier", "RandomForestRegressor",
# "RandomTreesEmbedding", "ExtraTreesClassifier",
# "ExtraTreesRegressor", "BaggingClassifier",
# "BaggingRegressor", "IsolationForest", "GradientBoostingClassifier",
# "GradientBoostingRegressor", "AdaBoostClassifier",
# "AdaBoostRegressor", "VotingClassifier", "VotingRegressor",
# "StackingClassifier", "StackingRegressor"

from sklearn.ensemble import RandomForestClassifier

RandomForestClassifier(n_estimators=100,
                       criterion="gini",
                       max_depth=None,
                       min_samples_split=2,
                       min_samples_leaf=1,
                       min_weight_fraction_leaf=0.,
                       max_features="auto",
                       max_leaf_nodes=None,
                       min_impurity_decrease=0.,
                       min_impurity_split=None,
                       bootstrap=True,
                       oob_score=False,
                       n_jobs=None,
                       random_state=None,
                       verbose=0,
                       warm_start=False,
                       class_weight=None,
                       ccp_alpha=0.0,
                       max_samples=None)
