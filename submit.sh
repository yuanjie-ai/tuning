#!/usr/bin/env bash
# @Project      : horovod-example
# @Time         : 2020/6/22 5:28 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : ${DESCRIPTION}

if [ -n "$1" ];
then cfg=$1
else cfg="cfg"
fi;

#DATA=`date +%s`
DATA=`date +'%Y%m%d-%H-%M-%S'`

cloudml jobs submit \
--priority_class best-effort \
-hka h_browser@XIAOMI.HADOOP -hkt tql -he hdfs://zjyprc-hadoop \
-pc "pip install -r /fds/requires_train.txt -i https://pypi.tuna.tsinghua.edu.cn/simple" \
-n "tf2hvd---$DATA" \
-f $cfg \

rm -rf ./dist ./horovod_distributed_example.egg-info

# http://docs.api.xiaomi.net/cloud-ml/client/sdk.html
