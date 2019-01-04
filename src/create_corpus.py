from _config import resources_path
from person_name import PersonName, load_book_review, bag_of_noun_person_tag

if __name__ == '__main__':
    pn = PersonName()
    df = load_book_review()

    netabare_true_fw=''
    netabare_false_fw = ''
    for i in range(len(df)):
        if type(df['ネタバレに該当する部分'][i])==str and type(df['レビュー全文'][i])==str:
            netabare_true_fw+=' '.join(bag_of_noun_person_tag(df['レビュー全文'][i],pn))
        if type(df['ネタバレに該当する部分'][i])!=str and type(df['レビュー全文'][i])==str:
            netabare_false_fw+=' '.join(bag_of_noun_person_tag(df['レビュー全文'][i],pn))

    with open(resources_path+'/corpus/netabare_true.txt','w')as fw:
        fw.write(netabare_true_fw)
    with open(resources_path+'/corpus/netabare_false.txt','w')as fw:
        fw.write(netabare_false_fw)
