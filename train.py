from __future__ import division
import os,time,cv2,scipy.io
import tensorflow as tf
import tensorflow.contrib.slim as slim
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import argparse
import subprocess
from scipy.misc import imread,imsave
import utils.utils as utils
from model.network import UNet as UNet
from model.network import UNet_SE as UNet_SE
import math
from glob import glob
from loss.losses import *
import random

seed = 2020#2019
np.random.seed(seed)
tf.set_random_seed(seed)
random.seed(seed)

parser = argparse.ArgumentParser()
parser.add_argument("--loss", default="lp", help="choose the loss type")
parser.add_argument("--is_test", default=0,type=int, help="choose the loss type")
parser.add_argument("--model", default="pre-trained",help="path to folder containing the model")
parser.add_argument("--debug", default=0, type=int, help="DEBUG or not")
parser.add_argument("--use_gpu", default=1, type=int, help="DEBUG or not")
parser.add_argument("--save_model_freq", default=10, type=int, help="frequency to save model")

ARGS = parser.parse_args()
DEBUG = ARGS.debug 
save_model_freq = ARGS.save_model_freq 
model=ARGS.model
is_test = ARGS.is_test


def calculate_psnr(img1, img2):
    # update learning rates at the end of every epoch.
    pass
