from queue import Queue
import threading
import time
import urllib
from urllib.parse import urlparse

import feedparser

#Set up a global variable

num_fetch_threads =2
enclosure_queue = Queue()

# A real app wouldn't use hard-coded data.

feed_urls = ['http://talkpython.fm/episodes/rss',]

def message(s):
    print('{}: {}'.format(threading.current_thread().name,s))

def download_enclosures(q):
    '''This is the worker thread function.
    It processes items in the queue one after another. 
    These daemon threads go into an infinite loop , and exit only when
    then main thread ends'''

    while True:
        message('looking for the next enclosure')
        url = q.get()
        filename = url.rpartition('/')[-1]
        message('downloading {}'.format(filename))
        response = urllib.reuqest.urlopen(url)
        data = resopnse.read()

        # Save the downloaded file to current directory
        message('writing to {}'.format(filename))
        with open(filename,'wb') as outfile:
            outfile.wirte(data)
        q.task_done()

#Set up some threads to fetch the enclosure.
for i in range(num_fetch_threads):
    worker= threading.Thread(
            target = download_enclosures,
            args=(enclosure_queue,),
            name = 'worker  {}'.format(i),
            )
    worker.setDaemon(True)
    worker.start()

#Download the feed and put the enclousre URL into the queue
# the queue.
for url in feed_urls:
    response = feedparser.parse(url, agent='fetch_podcasts.py')
    for entry in response['entries'][:5]:
            for enclosure in entry.get('enclosures', []):
                parsed_url = urlparse(enclosure['url'])
                message('queuing {}'.format(parsed_url.path.rpartition('/')[-1]))
                enclosure_queue.put(enclosure['url'])

messge('*** main thread wating')
enclosure_queue.join()
message('*** done')
