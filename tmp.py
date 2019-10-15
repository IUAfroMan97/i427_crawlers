## Jacob Good
## Lab 7
## Info-I427
## 10/13/2019

## Citations ##
# Used https://docs.python.org/3/library/urllib.parse.html,
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/, 
# and https://docs.python.org/3/library/urllib.request.html#module-urllib.request

## IMPORTS
import os
import time
from collections import deque
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

## Starting Variables
save_location = os.getcwd() + '/files/' ## change this as needed
starting_link = ['https://en.wikipedia.org/wiki/Special:Random'] ## seed
d = deque(starting_link)

page_num = 1
last_num_of_links = len(d)
while(len(d) > 0):
    u = urllib.parse.urlparse(d.popleft())
    with urllib.request.urlopen(u.geturl()) as f:
        page = f.read()
        soup = BeautifulSoup(page, 'html.parser')
        print('CURRENT LINK: {}'.format(u.geturl()))
        print('Parsing for links ...')
        start = time.time()
        for link in soup.findAll('a'):
            l = link.get('href')
            if l:
                if l[:2] == '//':
                    new_url = l[2:]
                    if new_url not in d:
                        d.append(new_url)
                if l[0] == '/':
                    new_url = u.scheme+'://'+u.netloc+l
                    if new_url not in d:
                        d.append(new_url)
                if l[:8] == 'https://':
                    if l not in d:
                        d.append(l)
        print('Found {} pages in {} sec(s)'.format(len(d)-last_num_of_links, time.time()-start))
        last_num_of_links = len(d)
        
        start = time.time()
        with open(str(os.path.join(save_location, 'file{}'.format(page_num)+'.html')), 'w') as nf:
            nf.write(str(soup.encode('utf-8')))
            nf.close()
        print('Cached new page: {}'.format(u.geturl()) + ' in {} sec(s)'.format(time.time()-start))
    page_num += 1
