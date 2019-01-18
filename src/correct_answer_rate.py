from load_file import *


def calculate_all_answer_rate():
    df = load_class_result()

    correct_amount = 0
    false_amount = 0
    for i in range(len(df)):
        if df['answer'][i] != '' and df['nb_answer'][i] == 'true':
            correct_amount += 1
        elif df['answer'][i] == '' and df['nb_answer'][i] == 'false':
            correct_amount += 1
        else:
            false_amount += 1
    print(correct_amount / len(df))
    print(correct_amount)
    print(len(df))


def calculate_nb_true_rate():
    df = load_class_result()
    correct_amount = 0
    false_amount = 0
    for i in range(len(df)):
        if df['nb_answer'][i] == 'true':
            if df['answer'][i] != '' and df['nb_answer'][i] == 'true':
                correct_amount += 1
            elif df['answer'][i] == '' and df['nb_answer'][i] == 'false':
                correct_amount += 1
            else:
                false_amount += 1
    print(correct_amount / df['nb_answer'][df['nb_answer'] == 'true'].count())
    print(correct_amount)
    print(df['nb_answer'][df['nb_answer'] == 'true'].count())


def calculate_nb_false_rate():
    df = load_class_result()
    correct_amount = 0
    false_amount = 0
    for i in range(len(df)):
        if df['nb_answer'][i] == 'false':
            if df['answer'][i] != '' and df['nb_answer'][i] == 'true':
                correct_amount += 1
            elif df['answer'][i] == '' and df['nb_answer'][i] == 'false':
                correct_amount += 1
            else:
                false_amount += 1
    print(correct_amount / df['nb_answer'][df['nb_answer'] == 'false'].count())
    print(correct_amount)
    print(df['nb_answer'][df['nb_answer'] == 'false'].count())


if __name__ == '__main__':
    calculate_all_answer_rate()
    calculate_nb_true_rate()
    calculate_nb_false_rate()
