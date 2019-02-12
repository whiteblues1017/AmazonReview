from multiprocessing.pool import Pool

from naive_bayes.load_file import  *
from naive_bayes.naive_bayes import NaiveBayes
from naive_bayes.person_name import PersonName
from naive_bayes.preprocessing.create_train_data import bag_of_noun_verb_person_tag


class NaiveBayeseReview():
    def __init__(self):
        self.nb = NaiveBayes()
        # self.no = no

    def train_review(self):
        category = ['true', 'false']
        for cate in category:
            print(cate)
            with open(resources_path + '/corpus/pre_experiment/noun_verb/netabare_' + cate + '.txt')as fr:
                self.nb.train(fr.readline(), cate)

    def classifier_review(self):
        fw_str = ''
        answer_list_df = load_answer_book_list()
        for id in answer_list_df['id'].tolist():
            pn = PersonName(id, 'test')
            amazon_df = load_amazon_review(id)
            print(amazon_df)
            for i in range(len(amazon_df)):

                text = amazon_df['レビュー全文'][i].replace('"', '').replace('\n', '')
                if text != '':
                    print(self.nb.classifier(bag_of_noun_verb_person_tag(text, pn)))
                    fw_str += '"' + id + '","' + amazon_df['ネタバレ該当部分'][i].replace('\n', ',') + '","' \
                              + self.nb.classifier(bag_of_noun_verb_person_tag(text, pn)) + '","' \
                              + ' '.join(bag_of_noun_verb_person_tag(text, pn)) + '"\n'
        return fw_str

    def export_classifier_result(self):
        with open(results_path + 'class_result_amazon_verb.csv', 'w')as fw:
            fw.write('"id","answer","nb_answer","text"\n')
            fw.write(self.classifier_review())


class NaiveBayeseReviewPre():
    def __init__(self):
        self.nb = NaiveBayes()

    def train_review(self):
        category = ['true', 'false']
        for cate in category:
            print(cate)
            with open(resources_path + '/corpus/pre_experiment/noun_verb_basic/netabare_' + cate + '.txt')as fr:
                self.nb.train(fr.readline(), cate)

    def train_data_classifier(self):
        fw_str = ''
        answer_list_df = load_book_list()[:15]
        print(answer_list_df)
        for id in answer_list_df['id'].tolist():
            pn = PersonName(id, 'test')
            book_meter_df = load_book_meter(id)

            for i in range(len(book_meter_df)):
                text = book_meter_df['text'][i].replace('"', '').replace('\n', '')
                if text != '':
                    print(self.nb.classifier(bag_of_noun_verb_person_tag(text, pn)))
                    fw_str += '"' + id + '","' + book_meter_df['netabare'][i] + '","' \
                              + self.nb.classifier(bag_of_noun_verb_person_tag(text, pn)) + '","' \
                              + ' '.join(bag_of_noun_verb_person_tag(text, pn)) + '"\n'
        return fw_str

    def classifier_review(self):
        fw_str = ''
        answer_list_df = load_answer_book_list()
        for id in answer_list_df['id'].tolist():
            pn = PersonName(id, 'test')
            amazon_df = load_amazon_review(id)
            print(amazon_df)
            for i in range(len(amazon_df)):

                text = amazon_df['レビュー全文'][i].replace('"', '').replace('\n', '')
                if text != '':
                    print(self.nb.classifier(bag_of_noun_verb_person_tag(text, pn)))
                    fw_str += '"' + id + '","' + amazon_df['ネタバレ該当部分'][i].replace('\n', ',') + '","' \
                              + self.nb.classifier(bag_of_noun_verb_person_tag(text, pn)) + '","' \
                              + ' '.join(bag_of_noun_verb_person_tag(text, pn)) + '"\n'
        return fw_str

    def export_classifier_result(self):
        with open(results_path + '/class_result_use_train_data_verb_basic.csv', 'w')as fw:
            fw.write('"id","answer","nb_answer","text"\n')
            fw.write(self.train_data_classifier())

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
    nbr = NaiveBayeseReviewPre()
    nbr.train_review()
    nbr.export_classifier_result()
    """
    for no in range(0, 5):
        nbr = NaiveBayeseReview(str(no))
        nbr.train_review()
        nbr.export_classifier_result()
    """