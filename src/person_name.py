import neologdn

import MeCab
import pandas as pd

from _config import resources_path
from monophological_analysis import get_person_name, get_personname_reading, shaping_text


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
        dict[df['character'][i]] = ''.join(get_personname_reading(df['character'][i])).replace('*', '')
        if df['other_name1'][i] is not '':
            dict[df['other_name1'][i]] = ''.join(get_personname_reading(df['other_name1'][i])).replace('*', '')
    return dict


def num_character_name_dict():
    num_name_dict = {}
    df = load_character_list()
    for i in range(len(df)):
        one_character = []
        for j in range(len(df.columns)):
            if df.iat[i, j] != '':
                one_character.append(df.iat[i, j])
        num_name_dict[i] = one_character
    return num_name_dict


def author_reading_dict():
    return {'乾くるみ': ''.join(get_personname_reading('乾くるみ')).replace('*', '')}


def get_keys_from_value(d, val):
    return [k for k, v in d.items() if v == val]


def get_number_from_kanji_name(kanji_name):
    for one_chara_list in num_character_name_dict().values():
        if kanji_name in one_chara_list:
            chara_code = get_keys_from_value(num_character_name_dict(), one_chara_list)[0]
            return chara_code


class PersonName():
    def __init__(self):
        self.chara_name_reading = character_fullname_nickname_dict()
        self.author_name_reading = author_reading_dict()

    def extract_character_from_review(self, name_from_text):
        return_value =''
        for chara_name in self.chara_name_reading.keys():
            if name_from_text in chara_name:
                # chara_code = get_number_from_kanji_name(name_from_text)
                code = get_number_from_kanji_name(chara_name)
                return_value ='【charaname' + str(code) + '】'
                return return_value

        for chara_name_read in self.chara_name_reading.values():
            if ''.join(get_personname_reading(name_from_text)).replace('*', '') in chara_name_read:
                kanji_name = get_keys_from_value(self.chara_name_reading, chara_name_read)[0]
                code=get_number_from_kanji_name(kanji_name)
                return_value='【charaname' + str(code) + '】'
                return return_value
        if return_value=='':
            return name_from_text

        # chara_name = [chara_name for chara_name in self.chara_name_reading.keys() if name in chara_name]
        # print(chara_name[0])

    def print_person_name(self):
        df = load_book_review()
        for text in df['レビュー全文'].tolist():
            if type(text) == str:
                text = text.replace('\n', '')
                # print(neologdn.normalize(text))
                person_name_list = get_person_name(text)
                # print(person_name_list)
                if person_name_list != []:
                    print(person_name_list)
                    for name in person_name_list:
                        print(self.extract_character_from_review(name))


def bag_of_noun_person_tag(text):
    pn=PersonName()
    m = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
    m.parse('')
    text = shaping_text(text)
    node = m.parseToNode(text)
    # node = m.parseToNode(text.encode('utf-8'))
    keywords = []
    while node:
        if node.feature.split(",")[1] == "固有名詞" and node.feature.split(",")[2] == "人名":
            if node.next.feature.split(",")[2] == "人名" and node.next.feature.split(",")[1] != "接尾":
                keywords.append(pn.extract_character_from_review(node.surface+node.next.surface))
                node = node.next
            else:
                keywords.append(pn.extract_character_from_review(node.surface))

        elif node.feature.split(",")[0] == "名詞":
            keywords.append(node.surface)
        node = node.next
    return keywords

if __name__ == '__main__':
    num_character_name_dict()
    #pn = PersonName()
    #pn.print_person_name()
    df = load_book_review()
    for text in df['レビュー全文'].tolist():
        if type(text) == str:
            text = text.replace('\n', '')
            print(bag_of_noun_person_tag(text))

    # print_person_name()
