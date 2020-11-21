# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/05_utils.ipynb (unless otherwise specified).

__all__ = ['limit_gpu']

# Cell
import tensorflow as tf
import os

# Cell
def limit_gpu(gpu_id: str, memory_limit:int):
    """
    limit the selected gpu [gpu_id] by [memory_limit] MB
    """
    os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
    os.environ["CUDA_VISIBLE_DEVICES"] = str(gpu_id)
    gpus = tf.config.list_physical_devices('GPU')

    if gpus:
        # Restrict TensorFlow to only allocate [memory MB] of memory on the first GPU
        try:
            tf.config.experimental.set_virtual_device_configuration(
                gpus[0], [
                    tf.config.experimental.VirtualDeviceConfiguration(
                        memory_limit=memory_limit)
                ])
            logical_gpus = tf.config.list_logical_devices('GPU')
            print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
        except RuntimeError as e:
            # Virtual devices must be set before GPUs have been initialized
            print(e)
    else:
        print(f'No GPU found in your system!')