import pandas as pd

from _config import resources_path


def load_noun_corpus(cate):
    line = ''
    with open (resources_path+'/corpus/pre_experiment/verb/netabare_'+cate+'.txt')as fr:
        line=fr.readline()
    return line
