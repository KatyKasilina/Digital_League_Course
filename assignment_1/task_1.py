import re
import os


def clean_dir(name_dir):
    if os.path.exists(name_dir):
        del_files = []
        for dirpath, dirnames, files in os.walk(name_dir):
            for fl in files:
                del_files.append(os.path.join(name_dir, fl))
        if len(del_files) > 0:
            for fi in del_files:
                os.remove(fi)
            print('done')
    else:
        os.makedirs(name_dir)


def tokenize_string_task1(orig_str):
    tokenized_str = " ".join(re.findall(r'\d{2}\:\d{2}|\d+|]+|[.,!?;:-]|[а-яА-Яa-zA-Z]+', orig_str))
    return tokenized_str


def digit_index_task2(orig_str):
    tokenized_list = (re.findall(r'\d{2}\:\d{2}|\d+|]+|[.,!?;:-]|[а-яА-Яa-zA-Z]+', orig_str))
    index_list = []
    for i, token in enumerate(tokenized_list):
        if token.isdigit():
            index_list.extend([i])
    return str(index_list).strip('[]')


def eng_letters_task3(orig_str):
    tokenized_list = (re.findall(r'\d{2}\:\d{2}|\d+|]+|[.,!?;:-]|[а-яА-Яa-zA-Z]+-[а-яА-Яa-zA-Z]+|[а-яА-Яa-zA-Z]+', orig_str))
    index_list = []
    for i, token in enumerate(tokenized_list):
        if re.search(r'[a-zA-Z]+', token):
            index_list.extend([i])
    return str(index_list).strip('[]')

def find_dates_task4(orig_str):
    tokenized_list = re.findall(
        r'\d\d\s(?:январ\w|феврал\w|март\w|апрел\w|май\w|июн\w|июл\w|август\w|сентрябр\w|октябр\w|ноябр\w|декабр\w)|\d{4}\sгод\w',
        orig_str)
    return str(tokenized_list).strip('[]')


def run_tasks(task_num, source_dir='lenta_sample', dist_dir='lenta_result_task1'):

    clean_dir(dist_dir)

    for dirpath, dirnames, files in os.walk(source_dir):
        for file_name in files:
            if file_name.endswith('.txt'):
                full_f_name_r = os.path.join(dirpath, file_name)
                full_f_name_w = os.path.join(dist_dir, file_name)

                with open(full_f_name_r, 'r') as fr:
                    data = fr.read()

                if task_num == 1:
                    data_2_save = tokenize_string_task1(data)
                elif task_num == 2:
                    data_2_save = digit_index_task2(data)
                elif task_num == 3:
                    data_2_save = eng_letters_task3(data)
                elif task_num == 4:
                    data_2_save = find_dates_task4(data)
                elif task_num == 5:
                    pass
                else:
                    print('This task number does not exist!')
                with open(full_f_name_w, 'w') as f:
                    f.write(data_2_save)
                    print(full_f_name_w + ' saved')

def main():
    run_tasks(1, 'lenta_sample', 'lenta_result_task1')
    run_tasks(2, 'lenta_sample', 'lenta_result_task2')
    run_tasks(3, 'lenta_sample', 'lenta_result_task3')
    run_tasks(4, 'lenta_sample', 'lenta_result_task4')

if __name__ == "__main__":
    main()


