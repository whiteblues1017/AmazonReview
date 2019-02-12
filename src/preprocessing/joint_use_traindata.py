from _config import results_path, resources_path
from load_file import load_book_list


def joint():
    with open(results_path + '/pre_experiment/class_result_use_train_data.csv', 'w')as fw:
        with open(results_path + '/pre_experiment/class_result_use_train_data0.csv')as fr:
            for line in fr.readlines():
                if line.split('","')[0].replace('"', '') in load_book_list()['id'].tolist()[:15]:
                    fw.write(line)


def joint_corpus():
    df = load_book_list()[:15]
    with open(resources_path + '/corpus/pre_experiment/noun_verb_basic/netabare_true.txt', 'w')as fw_true:
        with open(resources_path + '/corpus/pre_experiment/noun_verb_basic/netabare_false.txt', 'w')as fw_false:
            for id in df['id'].tolist():
                with open(resources_path + '/corpus/book_meter/noun_verb_basic/' + id + '/netabare_true.txt')as fr:
                    fw_true.write(fr.readline()+' ')
                with open(resources_path + '/corpus/book_meter/noun_verb_basic/' + id + '/netabare_false.txt')as fr:
                    fw_false.write(fr.readline()+' ')


if __name__ == '__main__':
    joint_corpus()
