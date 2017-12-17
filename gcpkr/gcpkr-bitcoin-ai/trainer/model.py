
# coding: utf-8

# In[ ]:

import tensorflow as tf
import shutil
import tensorflow.contrib.learn as tflearn
import tensorflow.contrib.layers as tflayers
from tensorflow.contrib.learn.python.learn import learn_runner
import tensorflow.contrib.metrics as metrics
import tensorflow.contrib.rnn as rnn
from tensorflow.contrib.learn.python.learn.utils import saved_model_export_utils


# In[ ]:

print('tf.__version__', tf.__version__)


# In[ ]:

SEQ_LEN = 5
DEFAULTS = [[0.0] for x in range(SEQ_LEN)]
BATCH_SIZE = 20
EPOCH_SIZE = 100
TIMESERIES_COL = 'rawdata'
NUM_LABELS = 1
NUM_FEATURES = SEQ_LEN - NUM_LABELS
TRAIN_GCS_PATH = 'gs://gcpkr-bitcoin-ml/preprocessing/train/kaggle_sample_train.csv'
EVAL_GCS_PATH = 'gs://gcpkr-bitcoin-ml/preprocessing/eval/kaggle_sample_eval.csv'
LSTM_SIZE = 5

LEARNING_RATE = 0.01
OPTIMIZER = 'SGD'


# In[ ]:

def read_dataset(filename, mode=tf.contrib.learn.ModeKeys.TRAIN):  
    def _input_fn():
        num_epochs = EPOCH_SIZE if mode == tf.contrib.learn.ModeKeys.TRAIN else 1
        input_file_names = tf.train.match_filenames_once(filename)
        filename_queue = tf.train.string_input_producer(
            input_file_names, num_epochs=num_epochs, shuffle=False)
        reader = tf.TextLineReader()
        _, value = reader.read_up_to(filename_queue, num_records=BATCH_SIZE)
        value_column = tf.expand_dims(value, -1)
        all_data = tf.decode_csv(value_column, record_defaults=DEFAULTS)
        inputs = all_data[:len(all_data)-NUM_LABELS]
        label = all_data[len(all_data)-NUM_LABELS : ]
        inputs = tf.concat(inputs, axis=1)
        label = tf.concat(label, axis=1)
        return {TIMESERIES_COL: inputs}, label
    return _input_fn


# In[ ]:

def model(features, targets, mode):
    x = tf.split(features[TIMESERIES_COL], NUM_FEATURES, 1) # sequence 형태로 변이
    lstm_cell = rnn.BasicLSTMCell(LSTM_SIZE, forget_bias=1.0)
    outputs, _ = rnn.static_rnn(lstm_cell, x, dtype=tf.float32)
    outputs = outputs[-1]
    weight = tf.Variable(tf.random_normal([LSTM_SIZE, NUM_LABELS]))
    bias = tf.Variable(tf.random_normal([NUM_LABELS]))
    predictions = tf.matmul(outputs, weight) + bias
    
    if mode == tf.contrib.learn.ModeKeys.TRAIN or mode == tf.contrib.learn.ModeKeys.EVAL:
        loss = tf.losses.mean_squared_error(targets, predictions)
        train_op = tf.contrib.layers.optimize_loss(
            loss=loss,
            global_step=tf.contrib.framework.get_global_step(),
            learning_rate=LEARNING_RATE,
            optimizer=OPTIMIZER)
        eval_metric_ops = {
            "rmse": tf.metrics.root_mean_squared_error(targets, predictions)
            }
    else:
        loss = None
        train_op = None
        eval_metric_ops = None
  
    predictions_dict = {"predicted": predictions}
  
    return tflearn.ModelFnOps(
        mode=mode,
        predictions=predictions_dict,
        loss=loss,
        train_op=train_op,
        eval_metric_ops=eval_metric_ops)


# In[ ]:

def get_train():
    return read_dataset(TRAIN_GCS_PATH, mode=tf.contrib.learn.ModeKeys.TRAIN)


# In[ ]:

def get_valid():
    return read_dataset(EVAL_GCS_PATH, mode=tf.contrib.learn.ModeKeys.EVAL)


# In[ ]:

def serving_input_fn():
    feature_placeholders = {
        TIMESERIES_COL: tf.placeholder(tf.float32, [None, NUM_FEATURES])
    }
    features = {
      key: tf.expand_dims(tensor, -1)
      for key, tensor in feature_placeholders.items()
    }
    features[TIMESERIES_COL] = tf.squeeze(features[TIMESERIES_COL], axis=[2])
    
    return tflearn.utils.input_fn_utils.InputFnOps(
      features,
      None,
      feature_placeholders
    )


# In[ ]:




# In[ ]:

def experiment_fn(output_dir):
    return tflearn.Experiment(
        tflearn.Estimator(model_fn=model, model_dir=output_dir),
        train_input_fn=get_train(),
        eval_input_fn=get_valid(),
        eval_metrics={
            'rmse': tflearn.MetricSpec(
                metric_fn=metrics.streaming_root_mean_squared_error
            )
        },
        export_strategies=[saved_model_export_utils.make_export_strategy(
            serving_input_fn,
            default_output_alternative_key=None,
            exports_to_keep=1
        )]
    )


# In[ ]:

shutil.rmtree('output', ignore_errors=True)


# In[ ]:

learn_runner.run(experiment_fn, 'output')

