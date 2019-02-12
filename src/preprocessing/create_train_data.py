from multiprocessing.dummy import Pool

from load_file import *
from person_name import *


def bag_of_noun_person_tag(text, pn):
    m = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
    m.parse('')
    text = shaping_text(text)
    node = m.parseToNode(text)
    # node = m.parseToNode(text.encode('utf-8'))
    keywords = []
    while node:
        if node.feature.split(",")[1] == "固有名詞" and node.feature.split(",")[2] == "人名":
            if node.next.feature.split(",")[2] == "人名" and node.next.feature.split(",")[1] != "接尾":
                keywords.append(pn.return_tag_from_review(node.surface + node.next.surface))
                node = node.next
            else:
                keywords.append(pn.return_tag_from_review(node.surface))

        elif node.feature.split(",")[0] == "名詞":
            # else:
            keywords.append(node.surface)
        node = node.next
    return keywords


def bag_of_noun_verb_person_tag(text, pn):
    m = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
    m.parse('')
    text = shaping_text(text)
    node = m.parseToNode(text)
    # node = m.parseToNode(text.encode('utf-8'))
    keywords = []
    while node:
        if node.feature.split(",")[1] == "固有名詞" and node.feature.split(",")[2] == "人名":
            if node.next.feature.split(",")[2] == "人名" and node.next.feature.split(",")[1] != "接尾":
                keywords.append(pn.return_tag_from_review(node.surface + node.next.surface))
                node = node.next
            else:
                keywords.append(pn.return_tag_from_review(node.surface))

        elif node.feature.split(",")[0] == "名詞" :
            keywords.append(node.surface)
        elif node.feature.split(",")[0] == '動詞':
            if node.feature.split(',')[6]=='*':
                print(node.feature.split(',')[6])
            keywords.append(node.feature.split(",")[6])
        node = node.next
    return keywords


def export_corpus_rand(max, no):
    if not os.path.exists(resources_path + '/corpus/' + str(max) + '/no_' + str(no)):
        os.mkdir(resources_path + '/corpus/' + str(max) + '/no_' + str(no))

    # 学習作品数15/50の場合
    book_list_df = load_rand_book_list(max, no)

    with open(resources_path + '/corpus/' + str(max) + '/no_' + str(no) + '/netabare_true.txt', 'w')as fw_true:
        for id in book_list_df['id'].tolist():
            with open(resources_path + '/corpus/book_meter/' + str(id) + '/netabare_true.txt', 'r')as fr:
                fw_true.write(fr.readline())

    with open(resources_path + '/corpus/' + str(max) + '/no_' + str(no) + '/netabare_false.txt', 'w')as fw_false:
        for id in book_list_df['id'].tolist():
            with open(resources_path + '/corpus/book_meter/' + str(id) + '/netabare_false.txt', 'r')as fr:
                fw_false.write(fr.readline())


def export_corpus_all():
    # 学習作品数100の場合
    book_list_df = load_book_list()

    with open(resources_path + '/corpus/100/netabare_true.txt', 'w')as fw_true:
        for id in book_list_df['id'].tolist():
            with open(resources_path + '/corpus/book_meter/' + str(id) + '/netabare_true.txt', 'r')as fr:
                fw_true.write(fr.readline())

    with open(resources_path + '/corpus/100/netabare_false.txt', 'w')as fw_false:
        for id in book_list_df['id'].tolist():
            with open(resources_path + '/corpus/book_meter/' + str(id) + '/netabare_false.txt', 'r')as fr:
                fw_false.write(fr.readline())


def export_corpus_the_work(id_list):
    for id in id_list:
        if not os.path.exists(resources_path + '/corpus/book_meter/noun_verb_basic/' + id):
            os.mkdir(resources_path + '/corpus/book_meter/noun_verb_basic/' + id)

        fw_true_str = ''
        fw_false_str = ''

        book_meter_df = load_book_meter(id)

        print(id)
        pn = PersonName(id, 'train')
        for text in book_meter_df['text'][book_meter_df['netabare'] == 'true'].tolist():
            fw_true_str += ' '.join(bag_of_noun_verb_person_tag(text, pn))
        for text in book_meter_df['text'][book_meter_df['netabare'] == 'false'].tolist():
            fw_false_str += ' '.join(bag_of_noun_verb_person_tag(text, pn))

        with open(resources_path + '/corpus/book_meter/noun_verb_basic/' + id + '/netabare_true.txt', 'w')as fw_true:
            with open(resources_path + '/corpus/book_meter/noun_verb_basic/' + id + '/netabare_false.txt', 'w')as fw_false:
                fw_true.write(fw_true_str)
                fw_false.write(fw_false_str)


def multiprocess_export_coupus():
    old_id_list = load_book_list()['id'].tolist()[:15]
    id_list = []
    for id in old_id_list:
        if not os.path.exists(resources_path + '/corpus/book_meter/noun_verb_basic/' + id + '/netabare_false.txt'):
            id_list.append(id)

    print(id_list)
    split_list = [id_list[i:i + int(len(id_list) / 3)] for i in
                  range(0, len(id_list), int(len(id_list) / 3))]

    print(split_list)
    # 並列数を決めて、Poolを用意
    pool = Pool(4)

    # 並列処理実行
    pool.map(export_corpus_the_work, split_list)


if __name__ == '__main__':
    multiprocess_export_coupus()
    # export_corpus_all()
    # for i in range(0,5):
    #    export_corpus_rand(50, i)
