from core import *
from writeDirectoryNames import *

dic = dict()
dic.update({"nameProject": "tese", "version": "2.0.1"})
#create_files("tese/package.json","template-reactjs/package.json",dic)
for i in range(len(getDiretoryTemplatesNameReactjs())):
    create_files(getDiretoryNameReactjs("teste")[i],getDiretoryTemplatesNameReactjs()[i],dic)
    print("Criado "+getDiretoryNameReactjs("teste")[i])
#create_files("teste/.gitignore","template-reactjs/.gitignore",dic)