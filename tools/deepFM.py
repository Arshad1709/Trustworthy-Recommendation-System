import os
import sys
import torch.nn as nn
from torch.utils.data import DataLoader, SubsetRandomSampler
from sklearn.metrics import confusion_matrix, accuracy_score
from dataset_class import *
from metric import metric
from utils import *
import numpy as np
from plotting import storing,plotting

curPath = os.path.abspath(os.path.dirname('__file__'))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

class DeepFMConfig(object):
    def __init__(self, ds_config):
        self.model_name = 'DeepFM'
        self.embed_dim = ds_config.embed_dim
        self.num_heads = ds_config.num_heads
        self.num_api = ds_config.num_api
        self.num_mashup = ds_config.num_mashup
        self.vocab_size = ds_config.vocab_size
        self.hidden_units = ds_config.hidden_units
        self.dropout = 0.2