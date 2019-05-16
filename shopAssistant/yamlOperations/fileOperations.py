import yaml


def open_yaml(file):
    with open(file, 'r') as stream:
        try:
            data = yaml.load(stream, Loader=yaml.Loader)
        except yaml.YAMLError as exc:
            print(exc)
        return data


def save_yaml(data, file):
    with open(file, 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)
