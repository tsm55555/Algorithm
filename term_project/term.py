# import packages we need
import os
import keras
import cv2
import numpy as np
import time
from PIL import Image
import tensorflow as tf
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
import matplotlib.pyplot as plt
from keras.utils import np_utils

# #---- GPU memory management --------------------------------
os.environ["CUDA_VISIBLE_DEVICES"]="0"
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
  tf.config.experimental.set_memory_growth(gpu, True) 
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

def prepare_data(image_path):
  num_image = 0
  data_label = []
  images = []
  for root, dirs, files in os.walk(image_path):
    # print("root: ", root)
    # print("dirs: ", dirs)
    # print("files:" ,files)
    for file in files:
      num_image +=1
    #   print("file: ", file)
    #   print()
      image_path = os.path.join(root, file) # get image's path
      img = Image.open(image_path)
      img = np.array(img).reshape(1, 28, 28)
    #   img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
      # print(img)
    #   print(img.shape)
    #   img = cv2.resize(img, (28,28))
      images.append(img)
      label = os.path.basename(os.path.normpath(root)) # get the basename of root(label)
      data_label.append(label) # append label
    # print("current_data_label", data_label) 
  images = np.array(images)
  print("image shape: ", images.shape)
  print("num of labels: ", len(data_label))
  return images, data_label

# load data
x_train, y_train = prepare_data("train_image")
x_test, y_test = prepare_data("test_image")

# hyperparameters
batch_size = 128
num_classes = 10
epochs = 800

# normalize images
x_train = x_train.reshape(2450, 28, 28, 1).astype('float32')
x_test = x_test.reshape(1700, 28, 28, 1).astype('float32')
x_train /= 255
x_test /= 255
y_train = keras.utils.np_utils.to_categorical(y_train, num_classes) # one hot encoding
y_test = keras.utils.np_utils.to_categorical(y_test, num_classes) # one hot encoding

# show data's shape
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

# define model
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(28, 28, 1))) # add Conv layer
model.add(Activation('relu'))
model.add(Dropout(0.3))
model.add(MaxPooling2D(pool_size=(2, 2))) # pooling layer improve accuracy significantly

model.add(Conv2D(32, (3, 3))) # add Conv layer
model.add(Activation('relu'))
model.add(Dropout(0.3))
model.add(Conv2D(64, (3, 3))) # add Conv layer
model.add(Activation('relu'))
model.add(Dropout(0.3))
model.add(MaxPooling2D(pool_size=(2, 2))) # pooling layer improve accuracy significantly

model.add(Flatten()) 

model.add(Dense(128)) # add fully connected layer
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(10)) # add fully connected layer
model.add(Activation('softmax'))

# output model summary
# model.summary()

# compile
model.compile(loss='categorical_crossentropy',
       optimizer="adam",
       metrics=['accuracy'])

# uncomment if u want to use EarlyStopping
# es = EarlyStopping(monitor='val_loss', patience=10)

start = time.time()
# start training 
hist = model.fit(x_train, y_train,
          batch_size = batch_size,
          epochs = epochs,
          verbose = 1,
          validation_split = 0.1,
          )
end = time.time()
print("training time: ", end - start)

# show training set accuracy
score = model.evaluate(x_train, y_train, verbose=0)
print('train loss:', score[0])
print('train acc:', score[1])

# show testing set accuracy
score = model.evaluate(x_test, y_test, verbose=0)
print('test loss:', score[0])
print('test acc:', score[1])

# plot loss figure
# loss = hist.history['loss']
# val_loss = hist.history['val_loss']
# epochs = len(loss)
# plt.plot(range(epochs), loss, marker='.', label='loss(training data)')
# plt.plot(range(epochs), val_loss, marker='.', label='val_loss(evaluation data)')
# plt.legend(loc='best')
# plt.grid()
# plt.xlabel('epoch')
# plt.ylabel('loss')
# plt.show()
# plt.savefig("result.jpg")