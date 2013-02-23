#!/usr/bin/python

import sys
import socket
import io
import shutil
import requests
import listener

class Alpha(object):
    def __init__(self, max_beta_number = 20):
        listener = listener.listener(max_beta_number, self)
        listener.run()
        self.urls = []
        self.download_ranges = {}

    def add_url(self, url):
        self.urls.append(url)
        self.download_ranges[url] = []


#url = sys.argv[1]
#file_name = url.split('/')[-1]
#betas = int(sys.argv[2])

#r = requests.head(url)
#file_size = int(r.headers['content-length'])

#ranges = calculate_ranges(betas, file_size)

#threads = []
#if betas:
    #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s.bind(('', 54321))
    #s.listen(betas)

    #for i in range(1, betas + 1):
        #t = AlphaThread(s, url, i, ranges[i], file_name)
        #threads.append(t)
        #t.start()

#print 'downloading my part'
#r = requests.get(url, headers={'range': "bytes=%s" % ranges[0]})
#print 'downloaded my part'
#print r.headers

#f = open("%s.0" % file_name, 'wb')
#f.write(r.content)
#f.close()

## Wait for all the threads to finish.
#for t in threads:
    #t.join()

#final_file = open(file_name, 'wb')
#for i in range(betas + 1):
    #shutil.copyfileobj(open("%s.%d" % (file_name, i), 'rb'), final_file)
#final_file.close()
