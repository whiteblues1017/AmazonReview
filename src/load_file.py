import os

import pandas as pd

from _config import resources_path, results_path


def load_book_list():
    df = pd.read_csv(resources_path + '/booklist.csv', dtype=str)
    return df


def load_rand_book_list(max, no):
    df = pd.read_csv(resources_path + '/rand_booklist/' + str(max) + '/no_' + str(no) + '.csv', dtype=str)
    return df


def load_answer_book_list():
    df = pd.read_csv(resources_path + '/answerlist.csv', dtype=str)
    return df


def load_book_meter(id):
    df = pd.read_csv(resources_path + '/book_meter/' + id + '.csv', quotechar='"', dtype='str')
    df = df.fillna('')
    return df


def load_character(id):
    df = pd.read_csv(resources_path + '/character/' + id + '.csv', quotechar='"', dtype='str')
    df = df.fillna('')
    return df


def load_amazon_review(id):
    df = pd.read_csv(resources_path + '/book_review_amazon/' + id + '.csv', quotechar='"', dtype='str')
    df = df.fillna('')
    return df


def load_class_result_100():
    df = pd.read_csv(results_path + '/eva_experiment/class_result_100.csv', quotechar='"', dtype='str')
    df = df.fillna('')
    return df


def load_class_result_rand(max, no):
    df = pd.read_csv(results_path + '/eva_experiment/' + str(max) + '/class_result_no' + str(no) + '.csv', quotechar='"',
                     dtype='str')
    df = df.fillna('')
    return df


def load_pre_experiment_0to15():
    df = pd.read_csv(results_path + '/pre_experiment/noun_verb_basic/class_result_use_train_data_verb_basic.csv', dtype='str', quotechar='"')
    df = df.fillna('')
    return df


def load_pre_experiment_amazon():
    df = pd.read_csv(results_path + '/pre_experiment/class_result.csv', dtype='str', quotechar='"')
    df = df.fillna('')
    return df


if __name__ == '__main__':
    df = load_book_list()
    for i in range(len(df)):
        if not os.path.exists(resources_path + '/book_meter/' + df['id'][i] + '.csv'):
            os.rename(resources_path + '/book_meter/' + df['title'][i] + '.csv',
                      resources_path + '/book_meter/' + df['id'][i] + '.csv')
