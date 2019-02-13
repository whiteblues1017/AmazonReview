from multiprocessing.pool import Pool

from _config import results_path , resources_path
from naive_bayes import NaiveBayes
from preprocessing.create_train_data import bag_of_noun_verb_person_tag, PersonName
from load_file import  *


class NaiveBayeseReview():
    def __init__(self,no,max):
        self.nb = NaiveBayes()
        self.no = no
        self.max = max

    def train_review(self):
        category = ['true', 'false']
        for cate in category:
            print(cate)
            with open(resources_path + '/corpus/'+str(self.max)+'/netabare_' + cate + '.txt')as fr:
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
        with open(results_path + '/eva_experiment/'+ str(self.max) + '/class_result.csv', 'w')as fw:
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
        answer_list_df = load_book_list()[10:15]
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
        with open(results_path + '/class_result_train_verb_basic10-15.csv', 'w')as fw:
            fw.write('"id","answer","nb_answer","text"\n')
            fw.write(self.train_data_classifier())


if __name__ == '__main__':
    """
    nbr = NaiveBayeseReviewPre()
    nbr.train_review()
    nbr.export_classifier_result()
    """
    nbr = NaiveBayeseReview(0,100)
    nbr.train_review()
    nbr.export_classifier_result()
    """
    for no in range(0, 5):
        nbr = NaiveBayeseReview(no,15)
        nbr.train_review()
        nbr.export_classifier_result()
    """