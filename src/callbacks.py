"""Callbacks used by all the models."""
from tensorflow import keras


def get_callbacks(model_path, patience=10):
    # save the best model, stop when val_loss stops improving
    # and lower the learning rate when it gets stuck
    return [
        keras.callbacks.ModelCheckpoint(model_path, monitor='val_loss', save_best_only=True),
        keras.callbacks.EarlyStopping(monitor='val_loss', patience=patience, restore_best_weights=True),
        keras.callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=3),
    ]
