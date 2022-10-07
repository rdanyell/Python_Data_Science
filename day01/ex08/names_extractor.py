import sys

def names_extractor():
  with open('employees.tsv', 'a') as f_write: # 'a' to add in the end of file
    f_write.write('Name\tSurname\tE-mail\n') # header
    with open('email.tsv', 'r') as f_read:
      line = f_read.readlines() # list of emails
      for i in range(len(line)):
        name = line[i].split('@')[0].split('.')[0]
        surname = line[i].split('@')[0].split('.')[1]
        f_write.write(f'{name.capitalize()}\t{surname.capitalize()}\t{line[i]}')

if __name__ == '__main__':
  if len(sys.argv) != 2:
    raise Exception("Error argument")
  names_extractor()
