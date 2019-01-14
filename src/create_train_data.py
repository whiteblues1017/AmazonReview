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
            keywords.append(node.surface)
        node = node.next
    return keywords


def export_corpus():
    fw_true_str = ''
    fw_false_str = ''
    for id in load_book_list()['id'].tolist():
        book_meter_df = load_book_meter(id)
        print(id)
        pn = PersonName(id)
        for text in book_meter_df['text'][book_meter_df['netabare'] == 'true'].tolist():
            fw_true_str += ' '.join(bag_of_noun_person_tag(text, pn))
        for text in book_meter_df['text'][book_meter_df['netabare'] == 'false'].tolist():
            fw_false_str += ' '.join(bag_of_noun_person_tag(text, pn))

    with open(resources_path + '/corpus/netabare_true.txt', 'w')as fw:
        fw.write(fw_true_str)

    with open(resources_path + '/corpus/netabare_false.txt', 'w')as fw:
        fw.write(fw_false_str)


if __name__ == '__main__':
    export_corpus()
