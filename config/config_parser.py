from os import environ, path
from pathlib import Path
from json import load
import yaml


def config(filename='settings.yml'):
    try:
        cwd = Path.cwd()
        path_str = "{}/{}".format(cwd, filename)
        return load(open(path_str))
    except Exception as e:
        print(e)


def config_yaml(filename='settings.yml'):
    try:
        p = path.dirname(__file__)
        path_file = f"{filename}"
        file = open(path_file, 'r')
        settings = yaml.load(file)
        file.close()

        return settings
    except Exception as e:
        raise e
        print(e)


settings = config_yaml()

if environ.get('TESTMODE'):
    settings = settings['test']
