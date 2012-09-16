#!/usr/bin/python
# -*- coding:utf-8 -*-
from Downloader import getStream
from FileHelper import getFilenameFromURL, writeBinFile
from threading import Thread

class threadDown(Thread):
  def __init__(self, url, failure=[], directory='.', timeout=10):
    Thread.__init__(self)
    self.url = url
    self.directory = directory
    self.timeout = timeout
    self.failure = failure
    self.finished = False
  def run(self):
    stream = getStream(self.url, timeout=self.timeout)
    file_name = getFilenameFromURL(self.url)
    if not stream or not writeBinFile(stream, file_name, self.directory):
      self.failure.append(self.url)
    self.finished = True

def threadDownloadFromList(alist, count=10, directory='.', timeout=10):
  """Url in alist, count a time"""
  # 多线程下载alist中的url，count为一组 默认count是10
  failure = [] # 这个list是公用的
  threads = [threadDown(url, failure, directory=directory, timeout=timeout) for url in alist]
  countWait(threads, 10)
  return failure

def countWait(threadlist, count):
  if not threadlist:
    return None
  threadlist = [t for t in threadlist if not t.finished]
  for t in threadlist:
    if not t.isAlive():
      try:
        t.start()
      except (Exception, SystemExit):
        pass
    if not threadlist.index(t) % count:
      t.join()
  countWait([t for t in threadlist if not t.finished], count)
