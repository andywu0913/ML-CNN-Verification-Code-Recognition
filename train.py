import numpy as np
import os
import random
from PIL import Image
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img

num_img_arrays_loaded = 100
img_rows = None
img_cols = None
img_channels = None
numbers_in_img = 6
random.seed(1)
np.random.seed(1)
x_list = list()
y_list = list()
x_train = list()
y_train = list()
x_test = list()
y_test = list()

def split_numbers_in_img(img_array, x_list, y_list):
    for i in range(numbers_in_img):
        step = img_cols // numbers_in_img
        x_list.append(img_array[:, i * step:(i + 1) * step] / 255)
        y_list.append(img_filename[i])

# load all img filenames
all_img_filenames = os.listdir('data')

# load images as arrays
img_filenames =  np.random.choice(all_img_filenames, num_img_arrays_loaded, replace=False)
for img_filename in img_filenames:
    img = load_img('data/{0}'.format(img_filename), color_mode='grayscale')
    img_array = img_to_array(img)
    img_rows, img_cols, img_channels = img_array.shape
    split_numbers_in_img(img_array, x_list, y_list)
y_list = keras.utils.to_categorical(y_list, num_classes=10)


x_train, x_test, y_train, y_test = train_test_split(x_list, y_list)

print(x_train[0].shape)
print(y_train[0].shape)
print(x_test[0].shape)
print(y_test[0].shape)
print(len(x_train))
print(len(y_train))
print(len(x_test))
print(len(y_test))

# model
if os.path.isfile('model/cnn_model.h5'):
    # recreate the exact same model purely from the file if exist
    model = models.load_model('model/cnn_model.h5')
else:
    # create a new cnn model
    model = models.Sequential()
    model.add(layers.Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(img_rows, img_cols // numbers_in_img, 1)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D(pool_size=(2, 2)))
    model.add(layers.Dropout(rate=0.25))
    model.add(layers.Flatten())
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dropout(rate=0.5))
    model.add(layers.Dense(10, activation='softmax'))

model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adadelta(), metrics=['accuracy'])

model.fit(np.array(x_train), np.array(y_train), batch_size=numbers_in_img, epochs=10, verbose=1, validation_data=(np.array(x_test), np.array(y_test)))
score = model.evaluate(np.array(x_test), np.array(y_test), verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

# save the model
model.save('model/cnn_model.h5')