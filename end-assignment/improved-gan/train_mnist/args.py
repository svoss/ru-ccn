# -*- coding: utf-8 -*-
import argparse

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument("-g", "--gpu_device", type=int, default=0)
parser.add_argument("-m", "--model_dir", type=str, default="model")
parser.add_argument("-p", "--plot_dir", type=str, default="plot")
parser.add_argument("-l", "--num_labeled", type=int, default=100)
# seed
parser.add_argument("-s", "--seed", type=int, default=None)

#Added for ability to continue training later on
parser.add_argument("-e", "--start-epoch", type=int, default=1)
#This makes it work in notebooks
parser.add_argument("-f","--file",type=str)

args = parser.parse_args()