import sys
from random import randint

class Research:
    def __init__(self, file_name):
        self.file_name = file_name

    def file_reader(self, has_header = True):
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
            self.data = data 
            self.count = self.counts()
            self.fractions = self.fractions()

        def counts(self):
            x = [x[0] for x in self.data]
            y = [y[1] for y in self.data]
            return [sum(x), sum(y)]

        def fractions(self):
            return [(self.count[0] / (self.count[0] + self.count[1])) * 100,
                    (self.count[1] / (self.count[0] + self.count[1])) * 100]


    class Analytics(Calculations):
        def __init__(self, data):
            super().__init__(data)
            
        def predict_random(self, number) ->list:
            predict_dict = {0: [0, 1], 1: [1, 0]}
            return [predict_dict[randint(0, 1)] for x in range(number)]

        def predict_last(self, data):
            return self.data[-1]


def check_arg(file_name):
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


if __name__ == '__main__':
    try:
        if len (sys.argv) != 2:
            raise Exception("Error argument")
        check_arg(sys.argv[1])
    except Exception as e: 
        print(e)    
    else:
        rsch = Research(sys.argv[1])
        output = Research(sys.argv[1]).file_reader()
        element = Research.Calculations(output)
        fractions = Research.Calculations.fractions(element)
        print(element.data)
        print(element.count[0], element.count[1])
        print(round(fractions[0], 2), round(fractions[1], 2))
        print(rsch.Analytics.predict_random(rsch, 3))
        predict_last = Research.Analytics(output)
        print(predict_last.predict_last(output)) 
   