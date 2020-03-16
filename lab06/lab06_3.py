import numpy as np
from keras.datasets import boston_housing


def print_structures():
    print(
        'training images \
            \n\tcount: {} \
            \n\tdimensions: {} \
            \n\tshape: {} \
            \n\tdata type: {}\n\n'.format(
            len(train_images),
            train_images.ndim,
            train_images.shape,
            train_images.dtype
        ),
        'testing images \
            \n\tcount: {} \
            \n\tdimensions: {} \
            \n\tshape: {} \
            \n\tdata type: {} \
            \n\tvalues: {}\n'.format(
            len(test_labels),
            train_labels.ndim,
            test_labels.shape,
            test_labels.dtype,
            test_labels
        )
    )


print_structures()
