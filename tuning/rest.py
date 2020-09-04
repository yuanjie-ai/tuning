#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : tuning.
# @File         : rest
# @Time         : 2020/9/1 7:45 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 


from nnicli import Experiment

exp = Experiment()
# exp.start_experiment('./config.yml')

exp.connect_experiment('http://10.241.141.162:8080/') # 远程分析

# exp.update_concurrency(16)
# exp.stop_experiment()

print(exp.get_experiment_status())
print(exp.get_job_statistics())
print(exp.list_trial_jobs())