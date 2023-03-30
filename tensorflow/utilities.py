import os
import matplotlib.pyplot as plt


def walk_dir(root_dir):
    """
    Prints no of images in each subdirectory starting from root_dir
    :param root_dir:
    :return:
    """
    for dir_path, dir_name, file_name in os.walk(root_dir):
        print(f'there are {len(dir_name)} directories and {len(file_name)} images in path {dir_path}')


def plot_loss_and_accuracy(history):
    """
    plot the loss curve and accuracy curve against each epochs.

    :param history:
    :return:
    """
    fig, axes = plt.subplots(1, 2, figsize=(10, 7))
    epochs = len(history.history['loss'])
    axes[0].plot(epochs, history.history['loss'], label='training loss')
    axes[0].plot(epochs, history.history['val_loss'], label='validation loss')
    axes[0].set_title('Loss Per Epochs')
    axes[0].set(xlabel='epochs', ylabel='loss')

    axes[1].plot(epochs, history.history['accuracy'], label='training accuracy')
    axes[1].plot(epochs, history.history['val_accuracy'], label='validation accuracy')
    axes[1].set_title('Accuracy Per Epochs')
    axes[1].set(xlabel='epochs', ylabel='Accuracy')

    plt.legend()
