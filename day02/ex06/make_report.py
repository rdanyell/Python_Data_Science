from config import *
from analytics import Research
import logging
import json
import requests

    # Отправим сообщение в телеграмм
def send_in_telegramm(text):
    token = "5682219488:AAHx6aPi5qsMEQCMBuxbTPPJUr6OXKr5K64"
    chat_id = "735891644"
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text 
    results = requests.get(url_req)
    if results.status_code != 200:
        raise Exception(f'Error server {results.status_code}')

def check_arg(file_name):
    logging.info("Check arguments")
    try:
        with open(file_name, 'r') as filename:
            line = filename.readlines()
    except Exception as e:
        raise Exception("FILE OPEN ERROR")
    # print(line)
    # читает файловый объект file построчно до EOF и возвращает список
    else: 
        if not line:
            raise Exception("File is empty")
        if len(line) < 2 or len(line[0].split(',')) !=2:
        # len() возвращает длину (количество элементов) в объекте.
        # проверяем по сабджу, что строк не меньше 2 и в первой строке 2 элемента, разделенных запятыми
            raise Exception("Wrong header")
        for i in range(1, len(line)):
            if line[i][0:4] != '0,1\n' and line[i][0:4] != '1,0\n' and line[i][0:4] != '1,0' and line[i][0:4] != '1,0':
                raise Exception("Wrong data")
            #проверяем по сабджу, что вторая и последующие строки имеют только указанный вид

def main():
    logging.basicConfig(filename=f'{LOG_FILE}.{EXTENSION_LOG}', 
                        format='%(asctime)s %(message)s',
                        datefmt='%y-%d-%m %H:%M:%S',
                        filemode='w',
                        level=logging.DEBUG)
    if check_arg(FILEPATH):
        send_in_telegramm('The report hasn’t been created due to an error')
        raise Exception("Error argument")
    output = Research(FILEPATH).file_reader()
    rsch = Research(FILEPATH)
    element = Research.Calculations(output)
    observations = len(output)
    heads_count = element.count[0]
    tails_count = element.count[1]
    heads_fractions = round(element.fractions[0], 2)
    tails_fractions = round(element.fractions[1], 2)
    random_predict = rsch.Analytics.predict_random(rsch, NUM_OF_STEPS)
    random_tails = sum([el[1] for el in random_predict])
    random_heads = sum([el[0] for el in random_predict])

    report = REPORT.format(
        observations , 
        tails_count,
        heads_count, 
        tails_fractions,
        heads_fractions,
        NUM_OF_STEPS,
        random_heads,
        random_tails
        )

    Research.Analytics.save_file(report, REPORT_FILE, EXTENSION)
    send_in_telegramm('The report has been successfully created')

if __name__ == '__main__':
    main()

# чтобы запустить в школе надо запустить виртуальное окружение :
# mkdir test
# python3 -m venv test
# source test/bin/activate
# pip3 install requests