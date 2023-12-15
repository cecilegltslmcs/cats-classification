#!/usr/bin/python3
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing import image_dataset_from_directory
from tensorflow.keras.preprocessing.image import ImageDataGenerator


def generateDataSet(IMG_HEIGHT, IMG_WIDTH, BATCH_SIZE):
    img_gen = ImageDataGenerator(
        preprocessing_function=preprocess_input,
        rotation_range=50,
        width_shift_range=0.1,
        height_shift_range=0.1,
        zoom_range=0.1,
        horizontal_flip=True,
        validation_split=0.2,
        fill_mode="nearest",
    )

    train_set = img_gen.flow_from_directory(
        path,
        class_mode="sparse",
        subset="training",
        target_size=(IMG_HEIGHT, IMG_WIDTH),
        batch_size=BATCH_SIZE,
    )

    val_set = img_gen.flow_from_directory(
        path,
        class_mode="sparse",
        subset="validation",
        target_size=(IMG_HEIGHT, IMG_WIDTH),
        batch_size=BATCH_SIZE,
        shuffle=False,
    )
    return train_set, val_set


def define_checkpoint(path):
    checkpoint = keras.callbacks.ModelCheckpoint(
        f"{path}/resnet50_{epoch:02d}_{val_accuracy:.3f}.h5",
        save_best_only=True,
        monitor="val_accuracy",
        mode="max",
    )
    return checkpoint


def make_model(model, learning_rate, droprate, size_inner):
    base_model = model(weights="imagenet", include_top=False, input_shape=(224, 224, 3))

    base_model.trainable = False

    #####################################################

    inputs = keras.Input(shape=(224, 224, 3))
    base = base_model(inputs, training=False)

    vectors = keras.layers.GlobalAveragePooling2D()(base)
    inner = keras.layers.Dense(size_inner, activation="relu")(vectors)

    drop = keras.layers.Dropout(droprate)(inner)

    outputs = keras.layers.Dense(20, activation="softmax")(drop)
    model = keras.Model(inputs, outputs)

    #####################################################

    optimizer = keras.optimizers.Adam(learning_rate=learning_rate)
    loss = keras.losses.sparse_categorical_crossentropy

    model.compile(optimizer=optimizer, loss=loss, metrics=["accuracy"])

    return model


path = "models"
IMG_WIDTH = 224
IMG_HEIGHT = 224
CHANNEL = 3
train_set, val_set = generateDataSet(IMG_WIDTH, IMG_HEIGHT, CHANNEL)
checkpoint = define_checkpoint(path)

model = make_model(model=ResNet50, learning_rate=0.001, size_inner=1000, droprate=0.0)
history = model.fit(
    train_set, epochs=30, validation_data=val_set, callbacks=[checkpoint]
)
