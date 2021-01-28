import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F


class abbdNet(nn.Module):

    def __init__():
        super(abbdNet, self).__init__()

        self.conv1 = nn.Conv2d(in_channels = 1, out_channels=10, kernel_size=3, stride=2)
        self.conv2 = nn.Conv2d(in_channels = 10, out_channels=10, kernel_size=3, stride=2)

        

        