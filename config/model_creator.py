import json


# This class is responsible for creating the model
class ModelCreator:
    def __init__(self, model_name):
        self.model_name = model_name

    def create_model(self):
        return json.dumps({"model_name": self.model_name, "status": "created"})
    def model_controller(self):
        return json.dumps({"model_name": self.model_name, "status": "controller"})
    def model_service(self):
        return json.dumps({"model_name": self.model_name, "status": "service"})
    def model_repository(self):
        return json.dumps({"model_name": self.model_name, "status": "repository"})
    