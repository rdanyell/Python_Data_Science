import sys
from random import randint
from config import *
import logging

class Research:
    def __init__(self, file_name):
        logging.info("An instance of the Research class is created")
        self.file_name = file_name

    def file_reader(self, has_header = True):
        logging.info("Research.file_reader(): Input file read ")
        with open(self.file_name, 'r') as file:
            line = file.readlines()
            if line[0] == '0,1\n' or line[0] == '1,0\n':
                self.has_header = False
            # Если заголовок есть, то начнем записывать со второй строки (start = 1), иначе - с первой
            start = 0
            if has_header == True:
                start = 1
            list_lists = []
            for i in range(start, len(line)):
                list_i = [int(line[i][0])]
                list_i.append(int(line[i][2]))
                list_lists.append(list_i)
            return(list_lists)

    class Calculations:
        def __init__(self, data):
            # Создаем объекты, чтобы их можно было вызывать снаружи
            logging.info("An instance of the Calculations class is created")
            self.data = data 
            self.count = self.counts()
            self.fractions = self.fractions()

        def counts(self):
            logging.info("Calculations.counts(): Counted the number of heads and tails")
            x = [x[0] for x in self.data]
            y = [y[1] for y in self.data]
            return [sum(x), sum(y)]

        def fractions(self):
            logging.info("Calculations.fractions(): Percentage of heads and tails calculated")
            return [(self.count[0] / (self.count[0] + self.count[1])) * 100,
                    (self.count[1] / (self.count[0] + self.count[1])) * 100]


    class Analytics(Calculations):
        def __init__(self, data):
            logging.info("An instance of the Analytics class is created")
            super().__init__(data)
            
        def predict_random(self, number) ->list:
            logging.info("Analytics.predict_random(): Random sample created")
            predict_dict = {0: [0, 1], 1: [1, 0]}
            return [predict_dict[randint(0, 1)] for x in range(number)]

        def predict_last(self, data):
            logging.info("Analytics.predict_last(): Found the last element of the selection")
            return self.data[-1]
        
        def save_file(report, REPORT_FILE, EXTENSION):
            logging.info("Analytics.save_file(): Report saved")
            with open(f'{REPORT_FILE}.{EXTENSION}', 'w') as report_file:
                report_file.write(report)
