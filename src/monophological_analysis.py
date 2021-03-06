import MeCab
import re
import emoji


def remove_emoji(src_str):
    return ''.join(c for c in src_str if c not in emoji.UNICODE_EMOJI)

def remove_kaomoji(node):
    if node.feature.split(",")[7]=='カオモジ' and node.feature.split(",")[0] == "記号":
        return ''

def bag_of_noun(text):
    # m = MeCab.Tagger("mecabrc")
    m = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
    m.parse('')
    text = shaping_text(text)
    node = m.parseToNode(text)
    # node = m.parseToNode(text.encode('utf-8'))
    keywords = []
    while node:
        if node.feature.split(",")[0] == "名詞":
            keywords.append(node.surface)
        node = node.next
    return keywords


def get_person_name(text):
    # m = MeCab.Tagger("mecabrc")
    try:
        m = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
        m.parse('')
        text = shaping_text(text)
        node = m.parseToNode(text)
        keywords = []

        while node:

            if node.feature.split(",")[1] == "固有名詞" and node.feature.split(",")[2] == "人名":
                if node.next.feature.split(",")[2] == "人名" and node.next.feature.split(",")[1] != "接尾":
                    keywords.append(node.surface + node.next.surface)
                    node = node.next
                else:
                    keywords.append(node.surface)

            node = node.next
        return keywords
    except:
        return []


def get_personname_reading(text):
    m = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
    m.parse('')
    text = shaping_text(text)
    node = m.parseToNode(text)
    keywords = []

    while node:
        if len(node.feature.split(",")) > 7:
            keywords.append(node.feature.split(",")[7])
        node = node.next

    reading = ''.join(keywords).replace('*', '')
    return reading


def shaping_text(text):
    # text = re.sub('【.+?】', "", text)
    text = re.sub('\d+', '0', text)
    text = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", text)
    text = re.sub('\[.+?\]', "", text)
    text = re.sub('\n', '', text)
    text = re.sub('\r', '', text)
    text = remove_emoji(text)

    return text
