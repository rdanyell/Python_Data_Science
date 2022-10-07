def read_and_write():
    with open ('ds.csv', 'r') as infile:
        with open ('hh.tsv', 'w') as outfile:
            res = infile.read().replace('\",', '\"\t')
            res = res.replace(',false,', '\tfalse\t')
            res = res.replace('false,', 'false\t')
            res = res.replace(',true,', '\ttrue\t')
            res = res.replace('true,', 'true\t')
            outfile.write(res)
           

if __name__ == '__main__':
    read_and_write()
