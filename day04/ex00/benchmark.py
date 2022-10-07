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


if __name__ == '__main__':
    ITERATIONS = 9 * 10 ** 4

    time_for_loop = timeit.timeit(EmailTester.test_loop, number = ITERATIONS)
    time_for_list = timeit.timeit(EmailTester.test_list, number=ITERATIONS)

    if time_for_loop > time_for_list:
        print('it is better to use a list comprehension')
    else:
        print('it is better to use a loop')
    
    print(f'{min(time_for_loop, time_for_list)} vs ' + \
        f'{max(time_for_loop, time_for_list)}')

    
    # print("\nLoop :", EmailTester.test_loop())
    # print("\nList comprehension :", EmailTester.test_list())
    # print("\nList_map :", EmailTester.test_listmap())
    # print("\nmap :", EmailTester.test_map())


