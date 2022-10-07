import sys

class Research:
    def __init__(self, file_name): # Конструктор, вызываемый при инициализации
        self.file_name = file_name

    def file_reader(self, has_header = True):
        with open(self.file_name, 'r') as file:
            line = file.readlines()
            if not line:
                raise Exception("File is empty")
            if line[0] == '0,1\n' or line[0] == '1,0\n' or line[0] == '1,0':
                self.has_header = False
            # Если заголовок есть, то начнем записывать со второй строки (start = 1), иначе - с первой
            start = 0
            if has_header == True:
                start = 1
            list_lists = []
            for i in range(start, len(line)): # 
                list_i = [int(line[i][0])] #записываем 0 элемент и 2, т.к. 1 - запятая
                list_i.append(int(line[i][2]))
                list_lists.append(list_i)
            return(list_lists)

    class Calculations:
        def counts(list_lists):
            heads = 0
            tails = 0
            for i in range(len(list_lists)):
                if list_lists[i][0] == 1:
                    heads += 1
                else:
                    tails += 1
            return(heads, tails)

        def fractions(list_counts):
            sum_counts = list_counts[0] + list_counts[1]
            return(list_counts[0] / sum_counts, list_counts[1] / sum_counts)


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
        list_lists = Research(sys.argv[1]).file_reader()
        print(list_lists)
        list_counts = Research.Calculations.counts(list_lists)
        print(list_counts[0], list_counts[1])
        list_fractions = Research.Calculations.fractions(list_counts)
        print(list_fractions[0], list_fractions[1])