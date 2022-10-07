import sys

def letter_starter():
  with open('employees.tsv', 'r') as f_read:
    line = f_read.readlines() # makes a list of emails
    name = '' # if wronf email
    for i in range(len(line)):
      if line[i].split('\t')[2] == sys.argv[1] + '\n': # if found email
        name = line[i].split('\t')[0]
    print(f'Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.')
    if name == '': # error if there is no email
      print('Error email')

if __name__ == '__main__':
    if len (sys.argv) != 2:
        raise Exception("Error argument")
    letter_starter()