# Purpose

Using Docker and TensorFlow we will show how one would theoretically go about serving a seq2seq or similar model.

# Prerequisites

I have previously written about setting up a [containerized bot](telegram-bot) so follow that for the basics.  A Dockerfile for all this will be used so make sure you are using a recent build since TensorFlow Serving requires Bazel >2.0

Since I have a custom base cuda tensorflow image, I use that but it is very similar to the base Dockerfile provided by official tensorflow project.  Mine looks like this:

```
FROM grahama/tensorflow:serving-slim

MAINTAINER grahama <graham.annett@gmail.com>

WORKDIR /root/

ADD data/inception-v3 inception-v3
```
and grahama/tensorflow:slim-serving looks like [link to slim-serving](link-to-slim-serving.md)


# Configuring with python-telegram-bot

# Pushing to IBM BlueMix