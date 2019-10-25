from os import path
import yaml


yaml_file_path = path.join(path.dirname(path.abspath(__file__)), 'yqzd_caps.yaml')
with open(yaml_file_path, 'r', encoding='UTF-8') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)