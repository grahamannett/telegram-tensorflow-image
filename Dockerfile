# VERSION:        0.1
# REPO/TAG:       grahama/telegram-tensorflow-image
# DESCRIPTION:    serves imagenet predictions
# AUTHOR:         graham annett
# COMMENTS:
#    changed name
# SETUP:
#
#   UBUNTU:
#   MAC:
#
# USAGE:
#

FROM grahama/tensorflow:slim-serving

MAINTAINER grahama <graham.annett@gmail.com>

WORKDIR /root/

ADD data/inception-v3 inception-v3