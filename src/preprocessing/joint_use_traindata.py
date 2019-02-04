from _config import results_path
from load_file import load_book_list


def joint():
    with open(results_path+'/pre_experiment/class_result_use_train_data.csv','w')as fw:
        with open(results_path+'/pre_experiment/class_result_use_train_data0.csv')as fr:
            for line in fr.readlines():
                if line.split('","')[0].replace('"','') in load_book_list()['id'].tolist()[:15]:
                    fw.write(line)



if __name__ == '__main__':
    joint()
