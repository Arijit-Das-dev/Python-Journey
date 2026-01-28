data = {
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

"""
Print the model name and framework for each experiment.

Find the experiment ID with the highest validation accuracy.

Create a list of experiments that use PyTorch.

Print the learning rate of exp_002.

Ignore failed experiments and compute the average validation accuracy.

Update exp_003 status to "completed" and add a new key "remarks".
"""


# Print the model name and framework for each experiment.
for exp_id, modelDetails in data.items():

    modelName = modelDetails["model"]["name"]
    modelFramework = modelDetails["model"]["framework"]

    print(f"{exp_id} | Model Name : {modelName}")
    print(f"{exp_id} | Model Framework : {modelFramework} \n")


# Find the experiment ID with the highest validation accuracy.
highest_validation_model_id = None
max_model_Accuracy = 0

for exp_id, modelDetails in data.items():

    valueAccuracy = modelDetails["metrics"]["validation"]["accuracy"]

    if valueAccuracy > max_model_Accuracy:

        max_model_Accuracy = valueAccuracy
        highest_validation_model_id = exp_id

print(f"Highest model accuracy : {highest_validation_model_id}")


# Create a list of experiments that use PyTorch.
PyTorchList = []
for exp_id, modelDetails in data.items():

    if modelDetails["model"]["framework"] == "PyTorch":

        PyTorchList.append(exp_id)

print(PyTorchList)