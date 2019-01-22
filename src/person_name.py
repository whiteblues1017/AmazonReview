#!/usr/bin/env python
# -*- coding: utf-8 -*-

from load_file import *
from monophological_analysis import *


def get_keys_from_value(d, val):
    return [k for k, v in d.items() if v == val]


class PersonName():
    def __init__(self, id,test_train_flg):
        self.id = id
        self.fullname_nickname_dict = {}
        self.reading_name_dict = {}
        self.reading_author_name = {}

        if test_train_flg is 'train':
            self.book_list_df = load_book_list()
        else:
            self.book_list_df = load_answer_book_list()

        self.set_reading_name_dict()
        self.set_reading_atuhor_name()

    # ex {'半沢直樹': ['課長'], '半沢花': ['']}
    def set_fullname_nickname_dict(self):
        df = load_character(self.id)

        for i in range(len(df)):
            if ',' in df['other_name'][i]:
                nickname_list = df['other_name'][i].split(',')
            else:
                nickname_list = [df['other_name'][i]]
            self.fullname_nickname_dict[df['character'][i]] = nickname_list

    # ex {'半沢直樹': 'ハンザワナオキ', '課長': 'カチョウ',}
    def set_reading_name_dict(self):
        self.set_fullname_nickname_dict()
        for full, nick_list in self.fullname_nickname_dict.items():
            self.reading_name_dict[full] = get_personname_reading(full)
            for nick in nick_list:
                if not nick == '':
                    self.reading_name_dict[nick] = get_personname_reading(nick)

    # ex {'池井戸潤': 'イケイドジュン'}
    def set_reading_atuhor_name(self):
        author_name = self.book_list_df['author'][self.book_list_df['id'] == self.id]
        author_names = author_name.to_string(index=None)
        for author_name in author_names.split(','):
            self.reading_author_name[author_name] = get_personname_reading(author_name)

    def get_reading_name_dick(self):
        return self.reading_name_dict

    def get_fullname_nickname_dict(self):
        return self.fullname_nickname_dict

    def matching_name_to_character(self, name):
        return_value = ''

        for dict_name, dict_name_read in self.reading_name_dict.items():
            if get_personname_reading(name) in dict_name_read:
                return_value = get_keys_from_value(self.reading_name_dict, dict_name_read)[0]
                break
        return return_value

    def return_tag_from_review(self, name_from_text):
        return_value = self.extract_author_tag_from_review(name_from_text)
        if return_value != name_from_text:
            return return_value

        return_value = self.extract_character_tag_from_review(name_from_text)
        if return_value != name_from_text:
            return return_value
        else:
            return name_from_text

    def extract_character_tag_from_review(self, name_from_text):
        return_value = ''
        for chara_name in self.reading_name_dict.keys():
            if name_from_text in chara_name:
                return_value = '【charaname】'
                return return_value
        for chara_name_read in self.reading_name_dict.values():
            if get_personname_reading(name_from_text) in chara_name_read:
                return_value = '【charaname】'
                return return_value
        if return_value == '':
            return name_from_text

    def extract_author_tag_from_review(self, name_from_text):
        return_value = ''
        for chara_name in self.reading_author_name.keys():
            if name_from_text in chara_name:
                return_value = '【authorname】'
                return return_value
        for chara_name_read in self.reading_author_name.values():
            if get_personname_reading(name_from_text) in chara_name_read:
                return_value = '【authorname】'
                return return_value
        if return_value == '':
            return name_from_text


if __name__ == '__main__':
    load_character('569615')
