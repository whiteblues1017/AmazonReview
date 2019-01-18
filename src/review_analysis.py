from _config import results_path
from naive_bayes import NaiveBayes
from preprocessing.create_train_data import *


class NaiveBayeseReview():
    def __init__(self):
        self.nb = NaiveBayes()

    def train_review(self):
        category = ['true', 'false']
        for cate in category:
            print(cate)
            with open(resources_path + '/corpus/netabare_' + cate + '.txt')as fr:
                self.nb.train(fr.readline(), cate)

    def classifier_review(self):
        fw_str = ''
        answer_list_df = load_answer_book_list()
        for id in answer_list_df['id'].tolist():
            pn = PersonName(id, 'test')
            amazon_df = load_amazon_review(id)
            print(amazon_df)
            for i in range(len(amazon_df)):

                text =amazon_df['レビュー全文'][i].replace('"','').replace('\n', '')
                if text!='':
                    print(self.nb.classifier(bag_of_noun_person_tag(text,pn)))
                    fw_str += '"' + id + '","' + amazon_df['ネタバレ該当部分'][i].replace('\n',',') + '","' \
                              + self.nb.classifier(bag_of_noun_person_tag(text,pn)) + '","' \
                              + ' '.join(bag_of_noun_person_tag(text,pn)) + '"\n'
        return fw_str

    def export_classifier_result(self):
        with open(results_path + '/class_result.csv', 'w')as fw:
            fw.write(self.classifier_review())


if __name__ == '__main__':
    nbr = NaiveBayeseReview()
    nbr.train_review()
    nbr.export_classifier_result()
