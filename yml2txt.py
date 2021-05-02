import ruamel.yaml

yaml = ruamel.yaml.YAML()
data = yaml.load(open('/Users/ethan/Documents/NTU/music_entropy/code/DeepBach/environment.yml'))

requirements = []
for dep in data['dependencies']:
    if isinstance(dep, str):
        package, package_version, python_version = dep.split('=')
        if python_version == '0':
            continue
        requirements.append(package + '==' + package_version)
    elif isinstance(dep, dict):
        for preq in dep.get('pip', []):
            requirements.append(preq)

with open('/Users/ethan/Documents/NTU/music_entropy/code/DeepBach/requirements.txt', 'w') as fp:
    for requirement in requirements:
       print(requirement, file=fp)

