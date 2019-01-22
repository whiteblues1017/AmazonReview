import math

import numpy as np

from load_file import *


class CalcRate():
    def __init__(self, max, no):
        self.max = max
        self.no = no

    def calculate_all_answer_rate(self):
        df = load_class_result_rand(self.max, self.no)

        correct_amount = 0
        false_amount = 0
        for i in range(len(df)):
            if df['answer'][i] != '' and df['nb_answer'][i] == 'true':
                correct_amount += 1
            elif df['answer'][i] == '' and df['nb_answer'][i] == 'false':
                correct_amount += 1
            else:
                false_amount += 1
        return correct_amount, len(df), correct_amount / len(df)

    def calculate_nb_true_rate(self):
        df = load_class_result()
        correct_amount = 0
        false_amount = 0
        for i in range(len(df)):
            if df['nb_answer'][i] == 'true':
                if df['answer'][i] != '' and df['nb_answer'][i] == 'true':
                    correct_amount += 1
                elif df['answer'][i] == '' and df['nb_answer'][i] == 'false':
                    correct_amount += 1
                else:
                    false_amount += 1
        return correct_amount, df['nb_answer'][df['nb_answer'] == 'true'].count(), correct_amount / df['nb_answer'][
            df['nb_answer'] == 'true'].count()

    def calculate_nb_false_rate(self):
        df = load_class_result()
        correct_amount = 0
        false_amount = 0
        for i in range(len(df)):
            if df['nb_answer'][i] == 'false':
                if df['answer'][i] != '' and df['nb_answer'][i] == 'true':
                    correct_amount += 1
                elif df['answer'][i] == '' and df['nb_answer'][i] == 'false':
                    correct_amount += 1
                else:
                    false_amount += 1

        return correct_amount, correct_amount / df['nb_answer'][df['nb_answer'] == 'false'].count(), df['nb_answer'][
            df['nb_answer'] == 'false'].count()


def calculate_all_answer_rate():
    df = pd.read_csv(results_path+'/class_result_use_train_data.csv',dtype=str,quotechar='"')

    correct_amount = 0
    false_amount = 0
    for i in range(len(df)):
        if df['answer'][i] != 'false' and df['nb_answer'][i] == 'true':
            correct_amount += 1
        elif df['answer'][i] == 'false' and df['nb_answer'][i] == 'false':
            correct_amount += 1
        else:
            false_amount += 1
    return correct_amount, len(df), correct_amount / len(df)


if __name__ == '__main__':
    print(calculate_all_answer_rate())
    """
    with open(results_path + '/analysis/15.csv', 'w')as fw:
        rates = []
        trues = []
        amounts = []
        for i in range(0, 5):
            cr = CalcRate(15, i)
            true, amount, rate = cr.calculate_all_answer_rate()
            rates.append(rate)
            trues.append(true)
            amounts.append(amount)
            fw.write(str(true) + ',' + str(amount) + ',' + str(rate) + '\n')
        fw.write(str(np.average(trues)) + ',' + str(np.average(amounts)) + ',' + str(np.average(rates)))
    """