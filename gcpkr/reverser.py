import os ,common ,csv

def reversed_lines(file):
    "Generate the lines of file in reverse order."
    part = ''
    for block in reversed_blocks(file):
        for c in reversed(block):
            if c == '\n' and part:
                yield part[::-1]
                part = ''
            part += c
    if part: yield part[::-1]

def reversed_blocks(file, blocksize=4096):
    "Generate blocks of file's contents in reverse order."
    file.seek(0, os.SEEK_END)
    here = file.tell()
    while 0 < here:
        delta = min(blocksize, here)
        here -= delta
        file.seek(here, os.SEEK_SET)
        yield file.read(delta)



if __name__ == '__main__':
     df = {}#llections.OrderedDict()
     coinNames = common.getCoinName()
     for coinNm in coinNames:
         coinpath = 't/'+coinNm+'.csv'
         with open(coinpath, 'r') as textfile:
             for row in csv.reader(reversed_lines(textfile)):
                 print( ', '.join(row))
