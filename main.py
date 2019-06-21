from core import *
from writeDirectoryNames import *

dic = dict()
dic.update({"nameProject": "react-saga-lab", "version": "0.0.1"})
#create_files("tese/package.json","template-reactjs/package.json",dic)
for i in range(len(getDiretoryTemplatesNameReactjs())):
    create_files(getDiretoryNameReactjs(dic.get("nameProject"))[i],getDiretoryTemplatesNameReactjs()[i],dic)
    print("Criado "+getDiretoryNameReactjs(dic.get("nameProject"))[i])
#create_files("teste/.gitignore","template-reactjs/.gitignore",dic)