import numpy as np
import os
import sys
from tensorflow.keras import models
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img

img_rows = None
img_cols = None
img_channels = None
numbers_in_img = 6
model = None

def split_numbers_in_img(img_array):
    x_list = list()
    for i in range(numbers_in_img):
        step = img_cols // numbers_in_img
        x_list.append(img_array[:, i * step:(i + 1) * step] / 255)
    return x_list

# load model
if os.path.isfile('model/cnn_model.h5'):
    model = models.load_model('model/cnn_model.h5')
else:
    print('No trained model found.')
    exit(-1)

# load img to predict
if len(sys.argv) > 1:
    img_filename = sys.argv[1]
else:
    img_filename = input('Varification code img filename: ')
img = load_img('{0}'.format(img_filename), color_mode='grayscale')
img_array = img_to_array(img)
img_rows, img_cols, img_channels = img_array.shape
x_list = split_numbers_in_img(img_array)

# predict
y_list = model.predict_classes(np.array(x_list), batch_size=numbers_in_img, verbose=1)
print(y_list)