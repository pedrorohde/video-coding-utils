import tensorflow as tf
from tensorflow.keras import Model, Input
from tensorflow.keras.layers import Conv2D, PReLU

class ARCNN(Model):
    def __init__(self):
        super(ARCNN, self).__init__()
        self.conv1 = Conv2D(64, 9, activation='relu', padding='same', input_shape=(64,64,1), name='conv1') # 64 9x9 filters, ReLU activation
        self.conv2 = Conv2D(32, 7, activation='relu', padding='same', name='conv2')                        # 32 7x7 filters, ReLU activation
        self.conv3 = Conv2D(16, 1, activation='relu', padding='same', name='conv3')                        # 16 1x1 filters, ReLU activation
        self.conv4 = Conv2D(1, 5, activation=None, padding='same', name='conv4')                           # 1  5x5 filter,    no activation

    def call(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = self.conv4(x)
        return x

    
# Enhancing Quality for HEVC Compressed Videos (Yang et. al., 2018)
class QECNN_I(Model):
    def __init__(self):
        super(QECNN_I, self).__init__()
        self.conv1 = Conv2D(128, 9)
        self.conv2 = Conv2D(64, 7)
        self.conv3 = Conv2D(64, 3)
        self.conv4 = Conv2D(32, 1)
        self.conv5 = Conv2D(1, 5)
        self.prelu1 = PReLU()
        self.prelu2 = PReLU()
        self.prelu3 = PReLU()
        self.prelu4 = PReLU()
    
    def call(self, x):
        x = self.conv1(x)
        x = self.prelu1(x)
        x = self.conv2(x)
        x = self.prelu2(x)
        x = self.conv3(x)
        x = self.prelu3(x)
        x = self.conv4(x)
        x = self.prelu4(x)
        x = self.conv5(x)
        return x
