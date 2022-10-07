#!/usr/bin/env python3

import timeit
import sys

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

    def test_map() -> list:
        return list(map(lambda x: x if x.find(EmailTester.email_domain) != -1 else None, EmailTester.emails))

    def test_filter() -> list:
        return list(filter(lambda x: x if x.find(EmailTester.email_domain) != -1 else None, EmailTester.emails))

if __name__ == '__main__':
    try:
        if len(sys.argv) == 3: 
            time_results ={
                'loop': EmailTester.test_loop,
                'list_comprehension': EmailTester.test_list, 
                'map': EmailTester.test_map, 
                'filter': EmailTester.test_filter
            }    
            iterations = int(sys.argv[2])
            if time_results.get(sys.argv[1]) is None:
                raise Exception("Wrong function name")
        else:
            raise Exception("Wrong number of argument")
    except ValueError:
        print("Wrong number of iterations")
    except Exception as err:
        print (err)
    else:
        print(timeit.timeit(time_results[sys.argv[1]], sys.argv[2]))

    # print("\nLoop :", EmailTester.test_loop())
    # print("\nList comprehension :", EmailTester.test_list())
    # print("\nmap :", EmailTester.test_map())
    # print("\nfilter :", EmailTester.test_filter())

   



