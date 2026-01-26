model_config = {
    "model_name": "ResNet50",
    "framework": "PyTorch",
    "task": "image_classification",
    "input_size": (224, 224, 3),
    "num_classes": 1000,
    "batch_size": 32,
    "epochs": 20,
    "learning_rate": 0.001,
    "optimizer": "Adam",
    "loss_function": "CrossEntropyLoss",
    "use_gpu": True,
    "device": "cuda",
    "early_stopping": True,
    "patience": 5,
    "augmentation": True,
    "shuffle_data": True,
    "validation_split": 0.2,
    "random_seed": 42,
    "save_best_model": True,
    "checkpoint_path": "./checkpoints/",
    "log_metrics": True
}

# printing all the keys
# x is the key 
for x in model_config:
    print(x)

# printing all the values
for x in model_config:
    print(model_config[x])

# printing both => keys and values 

for x, y in model_config.items():
    print(x, y)