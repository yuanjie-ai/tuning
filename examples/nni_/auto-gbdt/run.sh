#!/usr/bin/env bash
# @Project      : tuning
# @Time         : 2020/8/28 5:21 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : ${DESCRIPTION}

#1. nnictl experiment show        show the information of experiments
#2. nnictl trial ls               list all of trial jobs
#3. nnictl top                    monitor the status of running experiments
#4. nnictl log stderr             show stderr log content
#5. nnictl log stdout             show stdout log content
#6. nnictl stop                   stop an experiment
#7. nnictl trial kill             kill a trial job by id
#8. nnictl --help                 get help information about nnictl

nnictl stop

sleep 3

nnictl create --config config.yml
