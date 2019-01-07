import os

import pandas as pd

from _config import resources_path


def load_book_list():
    df = pd.read_csv(resources_path + '/booklist.csv', dtype=str)
    return df


def load_book_meter(id):
    df = pd.read_csv(resources_path + '/book_meter/' + id + '.csv', quotechar='"',dtype='str')
    df = df.fillna('')
    return df


def load_character(id):
    df = pd.read_csv(resources_path + '/character/' + id + '.csv', quotechar='"',dtype='str')
    df = df.fillna('')
    return df


if __name__ == '__main__':
    df = load_book_list()
    for i in range(len(df)):
        if not os.path.exists(resources_path + '/book_meter/' + df['id'][i] + '.csv'):
            os.rename(resources_path + '/book_meter/' + df['title'][i] + '.csv',
                     resources_path + '/book_meter/' + df['id'][i] + '.csv')
