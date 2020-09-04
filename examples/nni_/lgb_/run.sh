#!/usr/bin/env bash
# @Project      : tuning
# @Time         : 2020/8/31 8:38 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : ${DESCRIPTION}


nnictl stop --all
sleep 3

nnictl create --config config.yml