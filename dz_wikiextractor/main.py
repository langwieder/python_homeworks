import os
import re
from operator import itemgetter

# Функция запускает WikiExtractor только если нет уже обработанного файла wiki.txt
def run_extractor_if_needs(dump_path):
    wikiextractor_path = os.getcwd() + "/WikiExtractor.py"
    result_dir = os.getcwd() + "/ignored/"
    result_path = result_dir + "wiki.txt"

    if not os.path.exists(result_path):
        cmd_string = "cd " + result_dir + ";python3 " + wikiextractor_path + " --infn " + dump_path
        os.system(cmd_string)

    return result_path


# Путь к файлу с дампом
dump_path = os.getcwd() + "/ignored/bgwiki-20160305-pages-articles.xml"

# Запустить экстрактор
file_path = run_extractor_if_needs(dump_path)

# 2. Прочитать обработанный файл

# Создать словарик для слов
words_dic = {}
total_words_count = 0

f = open(file_path, 'r', encoding = 'utf-8')
for line in f.readlines():

    # Считаем сколько раз слово встретилось в тексте
    words = re.findall('\w+', line)
    for word in words:
        total_words_count += 1
        word = word.lower()
        if word in words_dic:
            words_dic[word] = words_dic[word] + 1
        else:
            words_dic[word] = 1
f.close()

# Считаем частотность слов
for word in words_dic:
    words_dic[word] = words_dic[word] / total_words_count

# 3. Составить частотный список
frequency_list = []
for word in words_dic:
    dic = {}
    dic["word"] = word
    dic["freq"] = words_dic[word]
    frequency_list.append(dic)
sorted_frequency_list = sorted(frequency_list, key=itemgetter('freq'), reverse=True)

# 4. Сохранить результат в csv
f = open('frequency_list.csv', 'w', encoding= 'utf-8')
for item in sorted_frequency_list:
    string = item['word']+"\t" + str(item['freq']) + '\n'
    f.write(string)
f.close()