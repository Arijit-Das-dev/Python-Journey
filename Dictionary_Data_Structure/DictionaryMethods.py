"""
Docstring for Dictionary_Data_Structure.DictionaryMethods

clear()
copy()
fromkeys()
get()
items()
keys()
values()
pop()
popitem()
setdefault()
update()

"""
experiments = {
    "exp_001": {
        "model": {
            "name": "ResNet50",
            "framework": "PyTorch",
            "params": {
                "lr": 0.001,
                "epochs": 20,
                "batch_size": 32
            }
        },
        "metrics": {
            "train": {
                "accuracy": 0.92,
                "loss": 0.35
            },
            "validation": {
                "accuracy": 0.89,
                "loss": 0.42
            }
        },
        "status": "completed"
    },
    "exp_002": {
        "model": {
            "name": "BERT",
            "framework": "TensorFlow",
            "params": {
                "lr": 0.0001,
                "epochs": 10,
                "batch_size": 16
            }
        },
        "metrics": {
            "train": {
                "accuracy": 0.94,
                "loss": 0.28
            },
            "validation": {
                "accuracy": 0.91,
                "loss": 0.33
            }
        },
        "status": "completed"
    },
    "exp_003": {
        "model": {
            "name": "CustomCNN",
            "framework": "PyTorch",
            "params": {
                "lr": 0.002,
                "epochs": 15,
                "batch_size": 64
            }
        },
        "metrics": {
            "train": {
                "accuracy": 0.88,
                "loss": 0.48
            },
            "validation": {
                "accuracy": 0.84,
                "loss": 0.55
            }
        },
        "status": "failed"
    }
}

# shallow copy of the dictionary
copied_dictionary = experiments.copy()

# get the keys and values 
experiments.keys()
experiments.values()

# Update the dictionary
experiments.update({"remark":"okay"})

# remove any key
experiments["exp_003"]["model"]["params"].pop("lr")
print(experiments)


# remove the last key 
experiments.popitem()
print(experiments)