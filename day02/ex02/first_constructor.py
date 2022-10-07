import sys

class Research:
    def __init__(self, file_name):
        self.file_name = file_name

    def file_reader(self):
        with open(self.file_name, 'r') as file:
            return(file.read())

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
    # print(check_arg(sys.argv[1]))
    try:
        if len(sys.argv) != 2:
            print("Argument error")
        check_arg(sys.argv[1])
    except Exception as e: 
        print(e)
    else:   
        print(Research(sys.argv[1]).file_reader())