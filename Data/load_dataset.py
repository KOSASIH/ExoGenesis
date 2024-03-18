import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical

def load_dataset(data_dir, batch_size, dim, n_channels, n_classes, shuffle):
    """
    Loads a dataset into memory for use in training machine learning models.

    :param data_dir: Directory containing the dataset.
    :param batch_size: Number of samples per batch.
    :param dim: Dimension sizes of the data (e.g., a volume of length 32 will have dim=(32,32,32)).
    :param n_channels: Number of channels in the data.
    :param n_classes: Number of classes in the dataset.
    :param shuffle: Whether to shuffle the data at each epoch.

    :return: A tuple containing the training and testing datasets, and the corresponding labels.
    """

    # Load the data and labels
    data = []
    labels = []

    for folder in os.listdir(data_dir):
        if os.path.isdir(os.path.join(data_dir, folder)):
            for file in os.listdir(os.path.join(data_dir, folder)):
                if file.endswith('.npy'):
                    data.append(np.load(os.path.join(data_dir, folder, file)))
                    labels.append(folder)

    # Convert labels to numerical values
    le = LabelEncoder()
    labels = le.fit_transform(labels)

    # Convert labels to one-hot encoding
    labels = to_categorical(labels, num_classes=n_classes)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42, shuffle=shuffle)

    # Reshape the data to match the expected input shape of themodel
    X_train = np.reshape(X_train, (X_train.shape[0], dim[0], dim[1], dim[2], n_channels))
    X_test = np.reshape(X_test, (X_test.shape[0], dim[0], dim[1], dim[2], n_channels))

    # Normalize the data
    X_train = X_train / 255.0
    X_test = X_test / 255.0

    # Create a data generator for loading the data in batches
    datagen = ImageDataGenerator(
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True
    )

    # Return the training and testing datasets, and the corresponding labels
    return (datagen.flow(X_train, y_train, batch_size=batch_size),
            datagen.flow(X_test, y_test, batch_size=batch_size),
            le)
