#!/usr/bin/python
# -*- coding:utf-8 -*-
from FileHelper import getFilenameFromURL, writeBinFile
import urllib2

def getStream(url, timeout=10):
  # 返回一个url流或者False
  request = urllib2.Request(url)
  request.add_header('User-Agent', UserAgent.Mozilla)
  try:
    stream = urllib2.urlopen(request, timeout=timeout)
  except (Exception, SystemExit): # catch SystemExit to keep running
    print "URL open error. Probably timed out."
    return False
  return stream

def downloadFromList(alist, directory='.', timeout=10):
  """Get files from a list of urls.
  return : list, contained the failure fetch"""
  failure = []
  for url in alist:
    print alist.index(url),
    stream = getStream(url, timeout=timeout)
    file_name = getFilenameFromURL(url)
    if not stream or not writeBinFile(stream, file_name, directory):
      failure.append(url)
  return failure

class UserAgent:
  Mozilla = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.14) Gecko/20080404 (FoxPlus) Firefox/2.0.0.14'
