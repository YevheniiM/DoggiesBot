import io
import os.path

import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
from django.conf import settings
from torch import optim

from ai.apps import AiConfig
from dtb.custom_storages import media_storage

# transform = transforms.Compose([transforms.Resize(size=224),
#                                 transforms.CenterCrop((224, 224)),
#                                 transforms.RandomHorizontalFlip(),
#                                 transforms.RandomRotation(10),
#                                 transforms.ToTensor(),
#                                 transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])])

# train_data = datasets.ImageFolder('', transform)
# VGG16 = models.vgg16()

# media_storage = MediaStorage() if not settings.DEBUG else default_storage

# def VGG16_predict(img_path):
#     """
#     Use pre-trained VGG-16 model to obtain index corresponding to
#     predicted ImageNet class for image at specified path
#
#     Args:
#         img_path: path to an image
#
#     Returns:
#         Index corresponding to VGG-16 model's prediction
#     """
#     image = Image.open(img_path).convert('RGB')
#     transform = transforms.Compose([transforms.Resize(size=224), transforms.CenterCrop((224, 224)),
#                                     transforms.ToTensor(), transforms.Normalize(mean=[0.485, 0.456, 0.406],
#                                                                                 std=[0.229, 0.224, 0.225])])
#
#     image = transform(image)[:3, :, :].unsqueeze(0)
#
#     output = VGG16(image)
#     _, preds_tensor = torch.max(output, 1)
#     pred = np.squeeze(preds_tensor.numpy())
#
#     return int(pred)


# def dog_detector(img_path):
#     if 151 <= VGG16_predict(img_path) <= 268:
#         return True


def run_app(img_path):
    predicted_breed = predict_breed_transfer(img_path)
    # if dog_detector(img_path):
    return print('the predicted breed is:', predicted_breed)
    # else:
    #     print('error: it\'s not a dog')


def load_image(img_path=None, image=None):
    if img_path:
        image = Image.open(img_path).convert('RGB')
    else:
        image = Image.open(io.BytesIO(image)).convert('RGB')

    image_transform = transforms.Compose([
        transforms.Resize(224),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize((0.485, 0.456, 0.406),
                             (0.229, 0.224, 0.225))])
    image = image_transform(image)[:3, :, :].unsqueeze(0)

    return image


def predict_breed_transfer(img_path=None, image=None, top=2):
    # load the image and return the predicted breed
    if img_path:
        image = load_image(img_path=img_path)
    else:
        image = load_image(image=image)

    predict = AiConfig.model(image)
    values, indices = torch.topk(predict.data.cpu(), top, sorted=True)
    # predict = predict.data.cpu().argmax()
    return [AiConfig.class_names[i] for i in indices.tolist()[0][:top]]

# with open("/tmp/husky-10.jpeg", 'rb') as f:
#     print(predict_breed_transfer(image=f.read()))
