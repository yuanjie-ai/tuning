#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : horovod-example.
# @File         : submit.py
# @Time         : 2020/7/3 10:50 上午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 


from cloud_ml_sdk.client import CloudMlClient
from cloud_ml_sdk.models.train_job import TrainJob

client = CloudMlClient()

# client.submit_train_job(open('hvd_tf2keras_mnist.json').read())


train_job = TrainJob(
    job_name='xx',
    trainer_uri='./',
    module_name='trainer.tf2keras_mnist',
    framework='horovod',
    framework_version='0.19.3-tf2.1.0-torch-mxnet1.6.0-xm1.0.0-py3',  # 不支持最新版本
    cpu_limit='4',
    memory_limit='4G',
    priority_class='best-effort'  # guaranteed or best-effort
)

client.submit_train_job(train_job.get_json_data())
