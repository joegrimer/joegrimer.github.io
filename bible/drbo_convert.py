import re
from pprint import pprint
import json

grand_list = []
# list of:
# [bookname, [
#  [chapter, [
#   line number, line]
#  ]
# ],

# book = re.compile('([A-Z ]+)')
chapter = re.compile('([a-zA-Z]+) Chapter ([0-9]+)')
rline = re.compile('([0-9]+:[0-9]+[\s\S]+?)')

bbuffer = ''
with open('drbo2.txt') as fo:
    counter = 0
    for sline in fo.readlines():
        counter += 1
        # print('looping >'+sline+'<')
        if sline.strip() == '':
            if bbuffer:
                print('ifb')
                bbuffer = bbuffer.strip()
                if chapter.match(bbuffer):
                    print('chapter', bbuffer)
                    book_name = bbuffer.split(' Chapter ')[0]
                    if not grand_list or grand_list[-1][0] != book_name:
                        grand_list.append([book_name, []])
                    grand_list[-1].append([bbuffer, []])

#                elif book.match(bbuffer):
#                    current_book += 1
#                    current_chapter = -1
#                    print('book', bbuffer)
#                    grand_list.append([bbuffer, []])
                elif rline.match(bbuffer):
                    print('line', bbuffer)
                    line_split = bbuffer.split('.')
                    grand_list[-1][-1][1].append([line_split[0], '.'.join(line_split[1:])])
                else:
                    print(' ?', bbuffer)
            bbuffer = ''  # reset it
        else:
        #    print('add')
            bbuffer += sline
        #if counter > 10000:
        #    break

# pprint(grand_list)
with open('drbo.json', 'w') as fo:
    fo.write(json.dumps(grand_list))
'''
count = 0
for match in chapter.findall(drbo_raw):
    count+=1
    print(match)
    if count > 200:
        break
        '''
