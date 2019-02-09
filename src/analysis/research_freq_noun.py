from _config import results_path
from analysis.load_corpus import load_noun_corpus


class FreqWord():
    def __init__(self):
        self.word_count = {}

    def sort_freq_word(self):
        fw_str = ''
        for k, v in sorted(self.word_count.items(), key=lambda x: -x[1]):
            fw_str += str(k) + ',' + str(v) + '\n'
        return fw_str

    def export_freq_word(self, cate):
        line_false = load_noun_corpus(cate)
        for word in line_false.split(' '):
            if word not in self.word_count.keys():
                self.word_count[word] = 1
            else:
                self.word_count[word] = self.word_count[word] + 1
        with open(results_path + '/research_freq_word/verb/netabare_' + cate + '.csv', 'w') as fw:
            fw.write(self.sort_freq_word())


if __name__ == '__main__':
    fw = FreqWord()
    fw.export_freq_word('false')
