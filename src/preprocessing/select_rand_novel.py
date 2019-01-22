import random
from load_file import *


def make_rand_list(max):
    df = load_book_list()
    use_index_list = []
    while len(use_index_list) <= max:
        index = random.randint(0, len(df)-1)
        if index not in use_index_list:
            use_index_list.append(index)
            list(set(use_index_list))
            if len(use_index_list)==max:
                break
    use_index_list=sorted(use_index_list)

    return use_index_list


def export_random_book_list():
    for j in range(5):
        df = load_book_list()
        # print(df)
        use_index_list = make_rand_list(15)
        print(len(use_index_list))
        print(use_index_list)
        for i in range(len(df)):
            if i not in use_index_list:
                df = df.drop(index=i)
        df.to_csv(resources_path + '/rand_booklist/15/no_' + str(j) + '.csv', sep=',',index=None)


if __name__ == '__main__':
    export_random_book_list()
