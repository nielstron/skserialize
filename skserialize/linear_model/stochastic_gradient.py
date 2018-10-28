"""
Serializing and deserializing for all stochastic gradient versions of scikit-learn
"""

import tables
from sklearn.linear_model import SGDClassifier


def save(path: str, data: SGDClassifier):
    """
    Store a SGDClassifier in HDF5
    :param path: str or Path
        Path to filename
    :param data:
    :return:
    """
    hdf5file = tables.open_file(path, 'w', title="SGDClassifier")

    hdf5file.create_array(hdf5file.root, 'intercept_', data.intercept_, 'intercept')
    hdf5file.create_array(hdf5file.root, 'classes_', data.classes_, 'class labels')
    hdf5file.create_array(hdf5file.root, 'coef_', data.coef_, 'coefficients')

    hdf5file.close()


