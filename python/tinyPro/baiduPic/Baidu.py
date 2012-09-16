#!/usr/bin/python
# -*- coding:utf-8 -*-
from Downloader import getStream
from MyParser import MyParser
from String import longestString, cutTo, cutBegin, getCodingContent
from urllib2 import quote
import re

def getImageUrlFromScript(script):
  pattern = re.compile(r'(?<="objURL":").*?(?=")')
  groups = pattern.findall(script)
  new_group = [amatch.strip() for amatch in groups] # 更Pythonic的方式
  return new_group

def getImageUrlList(url):
  stream = getStream(url)
  data = getCodingContent(stream)
  parser = MyParser()
  parser.feed(data)
  alist = parser.scriptList
  longestStr = longestString(alist)
  var_img = cutTo(longestStr, ';')
  return getImageUrlFromScript(var_img)

def nextPage(url, pn):
  url_pn = cutBegin(url, '&pn=')
  if not url_pn:
    url_pn = 0
  url_pn = int(url_pn) + pn
  return cutTo(url, '&pn') + '&pn=' + str(url_pn)

def search(keyword, addtionParams={}):
  """Generate a search url by the given keyword."""
  url = 'http://image.baidu.com/i?'
  parser = MyParser()
  params = getParams('http://image.baidu.com', parser)
  params.update(addtionParams)
  return url + appendParams(params) + '&word=' + quote(keyword)
def searchResult(url):
  parser = MyParser()
  parser.feed(getCodingContent(getStream(url)))
  block = longestString(parser.scriptList)
  parser.close()
  pattern = re.compile('(?<="listNum":)\d*(?=,)')
  count = pattern.findall(block)
  if count:
    count = int(count[0])
    return count
  return 0
def getParams(url, parser):
  stream = getStream(url)
  data = getCodingContent(stream)
  parser.feed(data)
  return parser.formParams

def appendParams(adict):
  """Generate a url with params in adict."""
  p = [key + '=' + adict[key] for key in adict]
  return '&'.join(p)
