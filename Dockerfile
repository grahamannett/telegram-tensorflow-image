# VERSION:        0.1
# REPO/TAG:       grahama/telegram-tensorflow-serving
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

ADD data/inception-v3 serving/inception-v3

ADD src src

RUN cd /serving/ && mkdir inception-export && \
    bazel-bin/tensorflow_serving/example/inception_export --checkpoint_dir=inception-v3 --export_dir=inception-export

# start gRPC server so client can do things
RUN bazel-bin/tensorflow_serving/example/inception_inference --port=9000 inception-export &> inception_log &

WORKDIR /
# use something like below
# ENTRYPOINT ["python", "main.py"]