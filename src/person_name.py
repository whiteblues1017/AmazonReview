import pandas as pd

from _config import resources_path
from monophological_analysis import get_person_name, get_personname_reading
import neologdn


def load_book_review():
    df = pd.read_csv(resources_path + '/book_review/initiation_Love.csv', quotechar='"')
    return df


def load_character_list():
    df = pd.read_csv(resources_path + '/character/initiation_Love.csv')
    df = df.fillna('')
    return df


def character_fullname_nickname_dict():
    dict = {}
    df = load_character_list()
    for i in range(len(df)):
        print(get_personname_reading(df['character'][i]))
        dict[df['character'][i]] = df['other_name'][i]
    return dict


def print_person_name():
    df = load_book_review()
    print(character_fullname_nickname_dict())
    for text in df['レビュー全文'].tolist():
        if type(text) == str:
            text = text.replace('\n', '')
            # print(text)
            # print(neologdn.normalize(text))
            person_name_list = get_person_name(text)


if __name__ == '__main__':
    print_person_name()
    # print_person_name()
