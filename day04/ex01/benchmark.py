#!/usr/bin/env python3

import timeit

class EmailTester:

    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
                'anna@live.com', 'philipp@gmail.com'] * 5

    email_domain = '@gmail.com'

    def test_loop() -> list:
        result = [] #creates new list
        for email in EmailTester.emails: #goes through elements in emails list
            if email.find(EmailTester.email_domain) != -1: #if it finds @gmail 
                result.append(email)
        return result

    def test_list() -> list:
        return [email for email in EmailTester.emails if email.find(EmailTester.email_domain) != -1]

    def test_listmap() -> list:
        return list(map(lambda x: x if x.find(EmailTester.email_domain) != -1 else None, EmailTester.emails))

    def test_map() -> list:
        map1 = map(lambda x: x if x.find(EmailTester.email_domain) != -1 else None, EmailTester.emails)
        return list(map1)

if __name__ == '__main__':
    ITERATIONS = 9 * 10 ** 3

    time_results ={
        'loop': timeit.timeit(EmailTester.test_loop, number = ITERATIONS),
        'list comprehension': timeit.timeit(EmailTester.test_list, number=ITERATIONS),
        'listmap': timeit.timeit(EmailTester.test_listmap, number=ITERATIONS),
        'map': timeit.timeit(EmailTester.test_map, number=ITERATIONS)
    }
    sorted_results = dict(sorted(time_results.items(), key=lambda item: item[1]))
    sorted_list = list(sorted_results.items())
    print(f'it is better to use a {sorted_list[0][0]}')
    print(sorted_list[0][1], 'vs', sorted_list[1][1], 'vs', sorted_list[2][1], 'vs', sorted_list[2][1] )

    # print("\nLoop :", EmailTester.test_loop())
    # print("\nList comprehension :", EmailTester.test_list())
    # print("\nList_map :", EmailTester.test_listmap())
    # print("\nmap :", EmailTester.test_map())

   



