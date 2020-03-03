from torchvision import models
import torch.nn as nn

def VggNet_downloaded(num_classes=100, input_channels=3,pretrained=True):
    model_vgg = models.vgg16(pretrained=pretrained) ### Downloading the original VGG 16, with an output vector of 1000
    for param in model_vgg.parameters():
        param.requires_grad = False
    model_vgg.classifier._modules['6'] = nn.Linear(4096, num_classes)  ### changing the output from 0 to 99
    model_vgg.classifier._modules['7'] = nn.LogSoftmax(dim = 1)  ### probability output vector
    return model_vgg


def vggnet(model_name, num_classes, input_channels, pretrained=True):
    return{
        'vggnet': VggNet_downloaded(num_classes=num_classes, input_channels=input_channels,pretrained=True),
    }[model_name]





















