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

FROM grahama/tensorflow:serving-slim

MAINTAINER grahama <graham.annett@gmail.com>

WORKDIR /root/

ADD data .