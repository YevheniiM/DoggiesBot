import io
import os.path

import torch
import torch.nn as nn
import torchvision.models as models
from django.apps import AppConfig
from django.conf import settings
from django.core.files.storage import default_storage
from torch import optim

from dtb.custom_storages import media_storage


class AiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ai'

    model = models.vgg16()

    if settings.DEBUG:
        with open(os.path.join(settings.MODELS_PATH, 'breeds.txt'), 'r') as f:
            class_names = [n.strip() for n in f.readlines()]
    else:
        with media_storage.open(os.path.join(settings.MODELS_PATH, 'breeds.txt'), "r") as f:
            class_names = [n.decode("utf-8").strip() for n in f.readlines()]

    for param in model.features.parameters():
        param.requires_grad = False

    n_inputs = model.classifier[6].in_features

    last_layer = nn.Linear(n_inputs, 133)

    model.classifier[6] = last_layer
    criterion_transfer = nn.CrossEntropyLoss()
    optimizer_transfer = optim.SGD(model.classifier.parameters(), lr=0.001)

    if settings.DEBUG:
        print(f"DEBUG: Initializing model [{os.path.join(settings.MODELS_PATH, 'breed_prediction.pt')}]")
        with default_storage.open(os.path.join(settings.MODELS_PATH, 'breed_prediction.pt'), "rb") as f:
            model.load_state_dict(torch.load(io.BytesIO(f.read())))
    else:
        print(f"INFO: Initializing model [{os.path.join(settings.MODELS_PATH, 'breed_prediction.pt')}]")
        with media_storage.open(os.path.join(settings.MODELS_PATH, 'breed_prediction.pt'), "rb") as f:
            model.load_state_dict(torch.load(io.BytesIO(f.read())))
