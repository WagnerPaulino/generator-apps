import os

def applyParams(keyArgs: dict, template: str):
    d = open(template,'r').read()
    for i in keyArgs.keys():
        if(d.find('{{') > -1):
            p = keyArgs.get(d[d.index('{{') + 2:d.index('}}')])
            d = d.replace(d[d.index('{{'):d.index('}}')+2],str(p))
            print(d)
    return d

def create_files(pathToFile: str,template: str, variables: dict):
    file_path = pathToFile
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    f = open(file_path, 'w+')
    f.write(applyParams(variables,template))
    f.close


""" como usar
dic = dict()
dic.update({"nameProject": "tese", "version": "2.0.1"})

create_files('teste/teste.json', 'template/package.json', dic)
"""