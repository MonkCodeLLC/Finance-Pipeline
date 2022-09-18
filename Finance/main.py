from module import api
from module import fileCreation
import os

def run():
    data = api.get_data("MSFT")
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data/")
    fileCreation.create_json(data, path)
    
if __name__ == "__main__":
    run()