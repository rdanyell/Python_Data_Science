def data():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    return dict(list_of_tuples)

def inv_dict(): #инвертируем словарь
    old_dict = data() #создаем временный старый словарь, конвертировав кортеж в словарь
    my_dict = {} # создаем новый словарь
    for key in old_dict: #для каждого  ключа в старом словаре
        my_dict.setdefault(old_dict[key], []).append(key) # добавляем значеие в новый словарь к нужному ключу
    return my_dict

def print_dict():
    new_dict = inv_dict()
    for key, value in new_dict.items():
        for i in range(len(value)): #распечатываем значения к каждому ключу по порядку 
            print("\'%s\' : \'%s\'" % (key, value[i]))

if __name__ == '__main__':
    print_dict()