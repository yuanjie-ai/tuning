#!/usr/bin/env bash
DATA=`date +'%Y%m%d-%H-%M-%S'`

project_name=$1 # 主程序命名项目名
#if cloudml jobs delete $project_name | grep "Successfully";
#then echo "删除 ..." && sleep 18s;
#fi;

cloudml jobs submit \
-n "lr$DATA" \
-m "trainer.$project_name" \
-u ./ \
-c 32 -M 32G \
-d cr.d.xiaomi.net/cloud-ml/tensorflow-gpu:33103tql2dev \
-pc "pip install -r /fds/requires_train.txt -i https://pypi.tuna.tsinghua.edu.cn/simple" \
-fc "ls" \
--priority_class "preferred" \
#--priority_class "preferred" \
#--priority_class "best-effort"
#-g 1 \
#-gt v100 \

#-a "--data-dir=/fds/cifar-10-data --job-dir=/tmp/cifar10 --num-gpus=1 --train-steps=1000"

rm -rf ./build/ ./*.egg-info/ ./dist/;
mv ./*.yaml ./checkpoints
# cloudml jobs list
#cloudml quota_v2 update -g 4 -M 256 -c 95 -p guaranteed -e yuanjie@xiaomi.com
