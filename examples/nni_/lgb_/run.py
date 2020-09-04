#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : tuning.
# @File         : run.py
# @Time         : 2020/9/1 5:54 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  :


#
# MIT#



from nnicli import Experiment

exp = Experiment()
exp.start_experiment('./config.yml')

# exp.update_concurrency(3)

print(exp.get_experiment_status())
print(exp.get_job_statistics())
print(exp.list_trial_jobs())

exp.stop_experiment()
