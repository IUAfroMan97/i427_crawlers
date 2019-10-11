#!/usr/bin/python3.7

import crawler
import time
import os
import multiprocessing as mp
from multiprocessing import Pool
import urllib.request
import urllib.parse
import urllib.robotparser
import shutil
import tempfile



#import concurrent.futures

def main():
    start = time.time()

    ### Processes

    #Process(target=crawl, args=(crawler.Crawler("C{}".format(p)),)3
    #c = crawler.Crawler("Test")
    #t = Process(target=crawl, args=crawler.Crawler("Test"))

    # print(f"Server[{os.getppid()}]")
    # processes = [Process(target=crawl, args=[crawler.Crawler(f'C{p}')]) for p in range(1,7)]   

    # for p in processes:
    #     p.start()


    # for p in processes:
    #     p.join()


    ### Older Style

    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     f1 = executor.submit(crawl, crawler.Crawler('C1'))
    #     print(f1.result())


    ### Pooling (modern simple)

    with Pool(8) as p:
        p.map(crawl, [crawler.Crawler(f'C{n}',) for n in range(7)])

    print("Finished in {} secs.".format(round(time.time()-start, 2)))

def crawl(crawler):
    pid = mp.current_process().pid
    crawler.setPid(pid)
    print(f"{crawler.name}[{crawler.pid}] is crawling ...")
    
    with urllib.request.urlopen('http://iu.edu/') as response:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            shutil.copyfileobj(response, tmp_file)
    
    with open(tmp_file.name) as html:
        pass

    print(f"{crawler.name}[{crawler.pid}] has finished crawling.")
    return True


if __name__ == "__main__":
    main()