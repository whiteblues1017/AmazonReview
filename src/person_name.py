#!/usr/bin/env python
# -*- coding: utf-8 -*-

from load_file import *
from monophological_analysis import *


def get_keys_from_value(d, val):
    return [k for k, v in d.items() if v == val]


class PersonName():
    def __init__(self, id):
        self.id = id
        self.fullname_nickname_dict = {}
        self.reading_name_dict = {}

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

    def get_reading_name_dick(self):
        return self.reading_name_dict

    def get_fullname_nickname_dict(self):
        return self.fullname_nickname_dict

    def matching_name_to_character(self,name):
        return_value = ''

        for dict_name ,dict_name_read in self.reading_name_dict.items():
            if get_personname_reading(name) in dict_name_read:
                return_value = get_keys_from_value(self.reading_name_dict,dict_name_read)
                break

        return return_value


if __name__ == '__main__':
    pn = PersonName('552620')
    pn.set_reading_name_dict()

    print(pn.matching_name_to_character('半沢'))