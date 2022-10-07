class Research:
    def file_reader():
        with open('data.csv', 'r') as filename:
            return(filename.read())

if __name__ == '__main__':
    print(Research.file_reader())