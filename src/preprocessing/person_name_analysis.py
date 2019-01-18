from _config import results_path
from load_file import *
from monophological_analysis import get_person_name
from person_name import PersonName


def judged_as_person_name_from_review(id):
    df = load_book_meter(id)
    name_list = []

    for i in range(len(df)):
        for name in get_person_name(df['text'][i]):
            name_list.append(name)

    name_list = list(set(name_list))
    return name_list


def extract_character_from_judged_person(id, name_list):
    assosiate_character_and_judged_name = []
    character_list = []

    pn = PersonName(id,'train')
    pn.set_reading_name_dict()
    pn.set_fullname_nickname_dict()

    for name in name_list:
        character_name = (name)
        print(character_name)
        character_list.append(character_name)
        if pn.matching_name_to_character(name) != '':
            assosiate_character_and_judged_name.append(name + ':' + pn.matching_name_to_character(name))

    return assosiate_character_and_judged_name


def export_judged_as_person_name():
    df = load_book_list()
    fw_str = ''
    fw_str_charcter = ''
    for i in range(len(df)):
        id = df['id'][i]
        title = df['title'][i]

        name_list = judged_as_person_name_from_review(id)

        fw_str += '"' + title + '","' + ','.join(name_list) + '"\n'

        with open(results_path + '/person_judged_Neologd/' + id + '.txt', 'w')as fw:
            fw.write(','.join(name_list))

    with open(results_path + '/person_judged_Neologd/all.csv', 'w')as fw:
        fw.write(fw_str)


def export_character_from_judged_person():
    df = load_book_list()
    fw_str_charcter = ''
    for i in range(len(df)):
        id = df['id'][i]
        title = df['title'][i]
        name_list = judged_as_person_name_from_review(id)
        matched_list = extract_character_from_judged_person(id, name_list)
        fw_str_charcter += '"' + title + '","' + ','.join(matched_list) + '"\n'

        with open(results_path + '/different_written/' + id + '.txt', 'w')as fw:
            fw.write('\n'.join(matched_list))

    with open(results_path + '/different_written/all.csv', 'w')as fw:
        fw.write(fw_str_charcter)


if __name__ == '__main__':
    # export_judged_as_person_name()

    export_character_from_judged_person()
