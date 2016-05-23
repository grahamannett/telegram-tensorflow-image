import sys
import threading

from grpc.beta import implementations
import tensorflow as tf

from tensorflow_serving.example import inception_inference_pb2


tf.app.flags.DEFINE_string('server', 'localhost:9000',
                           'inception_inference service host:port')
tf.app.flags.DEFINE_string('image', '', 'path to image in JPEG format')
FLAGS = tf.app.flags.FLAGS


NUM_CLASSES = 5


def main(_):
    host, port = FLAGS.server.split(':')
    channel = implementations.insecure_channel(host, int(port))
    stub = inception_inference_pb2.beta_create_InceptionService_stub(channel)
    # Send request
    with open(FLAGS.image, 'rb') as f:
        # See inception_inference.proto for gRPC request/response details.
        data = f.read()
        request = inception_inference_pb2.InceptionRequest()
        request.jpeg_encoded = data
        result = stub.Classify(request, 10.0)  # 10 secs timeout
        print result


if __name__ == '__main__':
    tf.app.run()
