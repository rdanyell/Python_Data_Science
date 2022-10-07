def data_types():

    a = 1
    b = 'Hello'
    c = 1.2
    d = True
    e = ['1', '2'] # list
    f = {'name': 'rdanyell', 'coalition': 'honeybadger'} # dict
    g = ('Hello', 1, True) # tuple
    h = set() # set

    print('[%s, %s, %s, %s, %s, %s, %s, %s]' #чтобы не было кавычек в выводе
          % (
              type(a).__name__, type(b).__name__ , #__name__ для того, чтобы выводилось только имя класса
              type(c).__name__, type(d).__name__,
              type(e).__name__, type(f).__name__ ,
              type(g).__name__, type(h).__name__
            )
          )
          
if __name__ == '__main__':
    data_types()
