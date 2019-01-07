from load_file import *
from monophological_analysis import get_person_name


def export_character_name_from_review(id):
    df = load_book_meter(id)
    name_list = []

    for i in range(len(df)):
        for name in get_person_name(df['text'][i]):
            name_list.append(name)

    print(list(set(name_list)))


if __name__ == '__main__':
    export_character_name_from_review('552620')
