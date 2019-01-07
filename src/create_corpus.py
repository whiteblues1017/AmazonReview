from _config import resources_path
from person_name import PersonName, load_book_review, bag_of_noun_person_tag

from sklearn.model_selection import train_test_split


def data_split(df):
    netabare_true_df = df[df['ネタバレに該当する部分'] is not '']
    netabare_false_df = df[df['ネタバレに該当する部分'] is '']

    true_train, true_test = train_test_split(netabare_true_df, test_size=0.1, shuffle=True)
    false_train, false_test = train_test_split(netabare_false_df,test_size=0.1,shuffle=True)

    return true_train+false_train, true_test+false_test

if __name__ == '__main__':
    pn = PersonName()
    df = load_book_review()

    train_df,test_df=data_split(df)

    print(len(train_df))
    print(len(test_df))

    netabare_true_fw = ''
    netabare_false_fw = ''
    for i in range(len(df)):
        if type(df['ネタバレに該当する部分'][i]) == str:
            netabare_true_fw += ' '.join(bag_of_noun_person_tag(df['レビュー全文'][i], pn))
        if type(df['ネタバレに該当する部分'][i]) != str:
            netabare_false_fw += ' '.join(bag_of_noun_person_tag(df['レビュー全文'][i], pn))

    with open(resources_path + '/corpus/netabare_true.txt', 'w')as fw:
        fw.write(netabare_true_fw)
    with open(resources_path + '/corpus/netabare_false.txt', 'w')as fw:
        fw.write(netabare_false_fw)
