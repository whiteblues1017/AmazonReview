import math

import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, f1_score, recall_score

from load_file import *


class CalcRate():
    def __init__(self, max, no):
        self.max = max
        self.no = no
        self.df = load_class_result_rand(self.max, self.no) if max != 100 else load_class_result_100()

    def load_answer(self):
        answer = [1 if x is not '' else 0 for x in self.df['answer'].tolist()]
        nb_answer = [1 if x != 'false' else 0 for x in self.df['nb_answer'].tolist()]
        tp, fn, fp, tn = confusion_matrix(answer, nb_answer).ravel()

        return answer, nb_answer


def export_f1_pre_recall_accu_rate():
    with open(results_path + '/eva_experiment/analysis/100_score.csv', 'w')as fw:
        fw.write('precision,recall,f_measure,accuracy\n')
        cr = CalcRate(100, 0)
        y_true, y_predict = cr.load_answer()

        fw.write(str(precision_score(y_true, y_predict)) + ',' +
                 str(recall_score(y_true, y_predict)) + ',' +
                 str(f1_score(y_true, y_predict)) + ',' +
                 str(accuracy_score(y_true, y_predict)) + '\n')


def export_rand_f1_pre_recall_accu_rate():
    with open(results_path + '/eva_experiment/analysis/15_score.csv', 'w')as fw:
        fw.write('precision,recall,f_measure,accuracy\n')
        for i in range(5):
            cr = CalcRate(15, i)
            y_true, y_predict = cr.load_answer()

            fw.write(str(precision_score(y_true, y_predict)) + ',' +
                     str(recall_score(y_true, y_predict)) + ',' +
                     str(f1_score(y_true, y_predict)) + ',' +
                     str(accuracy_score(y_true, y_predict)) + '\n')


class CalcRatePre():
    def __init__(self):
        # self.df_amazon = load_pre_experiment_amazon()
        self.df_0to15 = load_pre_experiment_0to15()

    def load_answer_0to15(self):
        print(len(self.df_0to15))
        answer = [1 if x != 'false' else 0 for x in self.df_0to15['answer'].tolist()]
        nb_answer = [1 if x != 'false' else 0 for x in self.df_0to15['nb_answer'].tolist()]
        tp, fn, fp, tn = confusion_matrix(answer, nb_answer).ravel()

        return answer, nb_answer

    def load_answer_amazon(self):
        answer = [1 if x is not '' else 0 for x in self.df_amazon['answer'].tolist()]
        nb_answer = [1 if x != 'false' else 0 for x in self.df_amazon['nb_answer'].tolist()]
        tp, fn, fp, tn = confusion_matrix(answer, nb_answer).ravel()

        return answer, nb_answer


def export_pre_f1_pre_recall_accu_rate():
    crp = CalcRatePre()
    with open(results_path + '/pre_experiment/noun_verb_basic/analysis/0to15_score.csv', 'w')as fw:
        fw.write('precision,recall,f_measure,accuracy\n')
        y_true, y_predict = crp.load_answer_0to15()
        fw.write(str(precision_score(y_true, y_predict)) + ',' +
                 str(recall_score(y_true, y_predict)) + ',' +
                 str(f1_score(y_true, y_predict)) + ',' +
                 str(accuracy_score(y_true, y_predict)) + '\n')


if __name__ == '__main__':
    export_rand_f1_pre_recall_accu_rate()
    #export_f1_pre_recall_accu_rate()
    # export_pre_f1_pre_recall_accu_rate()
