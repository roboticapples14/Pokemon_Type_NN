import torch 
import torchvision
import torch.nn as nn
import numpy as np
import torchvision.transforms as transforms
from torch.utils.data import Dataset
from csv import reader


class CSVDataset(Dataset):
    # load the dataset
    def __init__(self, path):
        # store the inputs and outputs
        self.dataset = self.load_csv(path)
        self.rows = len(self.dataset)
        self.cols = len(self.dataset[0])
 
    # Load a CSV file
    def load_csv(self, filename):
        file = open(filename, "r")
        lines = reader(file)
        dataset = list(lines)
        return dataset

    # number of rows in the dataset
    def __len__(self):
        return len(self.X)
 
    # get a row at an index
    def __getitem__(self, idx):
        return [self.X[idx], self.y[idx]]

# Load dataset
path = './Pokemon_DB/pokemon.csv'
data = CSVDataset(path)
print(data.rows)