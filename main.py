from core import *
from writeDirectoryNames import *

dic = dict()
dic.update({"nameProject": "tese", "version": "2.0.1"})
for i in getDiretoryNameReactjs(dic.get("nameProject")):
    create_files(i, i, dic)