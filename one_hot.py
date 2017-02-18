# encoding:utf-8
import numpy as np
def _dense_to_one_hot(labels_dense, num_classes):
  """Convert class labels from scalars to one-hot vectors."""
  num_labels = labels_dense.shape[0]
  index_offset = np.arange(num_labels) * num_classes
  labels_one_hot = np.zeros((num_labels, num_classes))
  labels_one_hot.flat[index_offset + labels_dense.ravel()] = 1
  return labels_one_hot



def dense_to_one_hott(labels_dense, num_classes):
    labels_dim = len(labels_dense.shape)
    if labels_dim == 1:  # 1表示exclusive classification
        num_labels = 1
    elif labels_dim == 2:  # 2表示多label分类问题
        num_labels = labels_dense.shape[1]
    else:
        raise Exception("labels_dense has an invalid dimension %d" % labels_dim)

    # if num_labels != NUM_OF_LABELS:
    #     raise ValueError('The num of data labels %d does not match global param NUM_OF_LABELS %d.' %
    #                      (num_labels, NUM_OF_LABELS))

    num_data = labels_dense.shape[0]
    index_offset = np.arange(num_data * num_labels) * num_classes
    labels_one_hot = np.zeros((num_data, num_labels * num_classes), dtype=np.int64)
    labels_offset = index_offset + labels_dense.ravel()
    labels_one_hot.flat[labels_offset] = 1
    return labels_one_hot


label=np.array([0,1,2,1,1,3])
print dense_to_one_hott(label,4)
print _dense_to_one_hot(label,4)