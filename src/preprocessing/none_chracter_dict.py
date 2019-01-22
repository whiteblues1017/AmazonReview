from load_file import *
if __name__ == '__main__':
    id_list=load_book_list()['id'].tolist()
    for id in id_list:
        if not os.path.exists(resources_path+'/character/'+id+'.csv'):
            print(id)