import tensorflow as tf
import numpy as np
import os

def bytes_feature(value):
    """Returns a bytes_list from a string / byte."""
    if isinstance(value, type(tf.constant(0))):
        value = value.numpy() # BytesList won't unpack a string from an EagerTensor.
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

def float_feature(value):
    """Returns a float_list from a float / double."""
    return tf.train.Feature(float_list=tf.train.FloatList(value=[value]))

def float_feature_list(value):
    """Returns an int64_list from a bool / enum / int / uint."""
    v = tf.train.FloatList(value=value)
    return tf.train.Feature(float_list=v)

def int64_feature(value):
    """Returns a single element int64_list from a bool / enum / int / uint."""
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))

def int64_feature_list(value):
    """Returns an int64_list from a bool / enum / int / uint."""
    v = tf.train.Int64List(value=value)
    return tf.train.Feature(int64_list=v)

def serialize_example(data, label):
    """
    Creates a tf.Example message ready to be written to a file.

    Parameters
    ----------
    data : ndarray
        sample in numpy format
    label : int or float
        label of the sample
    """
    # Create a dictionary mapping the feature name to the tf.Example-compatible data type.
    feature = {
      'x': bytes_feature(data.tobytes()),  # x file to bytes
      'y': int64_feature(label),  # target
    }

    # Create a Features message using tf.train.Example.
    example_proto = tf.train.Example(features=tf.train.Features(feature=feature))
    return example_proto.SerializeToString()

def _write_tfrec_file(file_list,
                      label_list,
                      folder,
                      file_index,
                      serialize_fn,
                      max_bytes=200*1024*1024,
                      loader_fn=np.load,
                      file_prefix='file_',
                      dtype=np.int8,
                      zfill=5,
                      verbose=False):
    """
    Converts a list of files to TfRecords, and then writes them into a tfrec file.
    The file name will be: <folder>/<file_prefix><file_index>_<n_files>.tfrec

    Parameters
    ----------
    file_list : list
        A list of paths to be encoded into the tfrec file
    labels : list
        A list of labels
    folder : str
        Folder to store the tf record
    file_index : int
        Sequential number to name the file
    serialize_fn : function
        Function to convert a single file into a tf.Example. Signature is (data, label)
    max_bytes : int
        Maximum size in bytes
    loader_fn : function, Optional
        Function to load a file. Could be np.load if format is npy
    file_prefix : str, Optional
        Prefix to include to the file name
    dtype : dtype, Optional
        Data type to convert loaded data before serializing. For images, np.int8
    zfill : int, Optional
        Number of characters to zero pad the file name index
    verbose : bool
        Whether to output messages or not
    """
    assert len(file_list) == len(label_list); "file_list and label_list must be the same length"

    n_bytes, n_files = 0, 0
    tmp = folder + '/tmp.tfrec'
    with tf.io.TFRecordWriter(tmp) as writer:
        for d in list(zip(file_list, label_list)):
            data = loader_fn(d[0]).astype(dtype)
            label = d[1]
            example = serialize_fn(data, label)
            writer.write(example)

            n_bytes += data.nbytes
            n_files += 1

            # break execution if files surpasses max number of bytes
            if n_bytes > max_bytes:
                break

    # rename tmp file
    if os.path.exists(tmp):
        filename = folder + '/' + file_prefix + str(file_index).zfill(zfill) + '_' + str(n_files) + '.tfrec'
        os.rename(tmp, filename)
        if verbose:
            print(f'File saved to {filename}')

    return n_files

def convert(file_list,
            label_list,
            folder='tfrecords',
            file_prefix='file_',
            serialize_fn=serialize_example,
            max_mb=200,
            loader_fn=np.load,
            dtype=np.int8,
            zfill=5,
            verbose=True
            ):
    """
    Converts a list of files into a set of tfrec files

    Parameters
    ----------
    file_list : list
        A list of paths to be encoded into the tfrec file
    label_list : list
        A list of labels
    folder : str
        Folder to store the tf record
    file_prefix : str, Optional
        Prefix to include to the file name
    serialize_fn : function
        Function to convert a single file into a tf.Example. Signature is (data, label)
    max_mb : int
        Maximum size in MB
    loader_fn : function, Optional
        Function to load a file. Could be np.load if format is npy
    dtype : dtype, Optional
        Data type to convert loaded data before serializing. For images, np.int8
    zfill : int, Optional
        Number of characters to zero pad the file name index
    verbose : bool
        Whether to output messages or not

    """
    assert len(file_list) == len(label_list); "file_list and label_list must be the same length"

    # Create folder
    path = os.path.join(folder)
    if not os.path.exists(path):
        os.mkdir(path)

    max_output_filesize = max_mb * 1024 * 1024  # max file size in bytes

    files = file_list.copy()
    labels = label_list.copy()
    file_index=0
    while True:
        n = _write_tfrec_file(files,
                              labels,
                              folder=folder,
                              file_index=file_index,
                              file_prefix=file_prefix,
                              serialize_fn=serialize_fn,
                              max_bytes=max_output_filesize,
                              loader_fn=loader_fn,
                              dtype=dtype,
                              zfill=zfill,
                              verbose=verbose)
        file_index += 1
        files = files[n:]
        labels = labels[n:]


def read_labeled_tfrecord(ex):
    """
    This is an example function to decode a tf record

    Note
    ----
    This is an example of decoding a tf record. You should know before hand the tf record format, and
    define it in a dictionary. More parameters, inputs or outputs, can be added to this function.

    Parameters
    ----------
    ex : tf.data.Example
        TF example object, provided by the TFRecordDataset

    Returns
    -------
    data :
        The decoded data
    label : int
        The label of this example

    """
    labeled_tfrec_format = {
        'x': tf.io.FixedLenFeature([], tf.string),  # data
        'y': tf.io.FixedLenFeature([], tf.int64),  # label
    }
    example = tf.io.parse_single_example(ex, labeled_tfrec_format)
    x = tf.io.decode_raw(example['x'], out_type=tf.int8)
    x = tf.cast(x, tf.float32) / 255.0

    # Labels
    y = tf.cast(example['y'], tf.float32)

    return x, y