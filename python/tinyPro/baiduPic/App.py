#!/usr/bin/python
# -*- coding:utf-8 -*-
from Baidu import getImageUrlList, search, nextPage, searchResult
from FileHelper import getFilenameFromURL, addExtension
from ThreadDownloader import threadDownloadFromList
import os, sys, urllib2

def makedir(directory):
  if not os.path.isdir(directory):
    os.mkdir(directory) # 不捕获directory是文件时的异常，让程序自己退出

def proxy_install(proxy):
  proxy_handler = urllib2.ProxyHandler({"http" : proxy})
  opener = urllib2.build_opener(proxy_handler)
  urllib2.install_opener(opener)

if __name__ == "__main__":
  keyword = '美女'.decode('utf8') # 要搜索的关键字
  addtional = {'width':'1920', 'height':'1200'} # 宽度和高度 可以为空 {}
  directory = r'image'  # 存放的位置
  count = 500     # 要下载的数量，自动进到20的倍数
  # 代理设置
  proxy = 'http://localhost:7001'
  use_proxy = False
  # 开始准备
  if use_proxy: # 设置代理
    proxy_install(proxy)

  while_n = 0 # 循环计数器
  imglist = []
  makedir(directory)
  print 'Generate search url'
  searchURL = search(keyword.encode('gbk'), addtional)
  # 下载 #############
  # 获取搜索结果数量并与count比较取其较小值
  count = min(searchResult(searchURL), count)
  # 没有搜索结果时退出
  if not count:
    print "No search result at current condition."
    sys.exit(1)
  # 获得指定数量的url, 存放于list  ,one page by one page
  print 'Fetching page',
  while len(imglist) < count:
    print while_n,
    #mark the times of while
    while_n += 1
    tmplist = getImageUrlList(searchURL)
    imglist = imglist + tmplist
    searchURL = nextPage(searchURL, len(tmplist))
  print '' # 换行
  count = len(imglist)
  print "There're %d files to download" % count
  # 将已有文件从imglist中去除
  imglist = [url for url in imglist if not getFilenameFromURL(url) in os.listdir(directory)]
  print "There's %d files already downloaded." % (count - len(imglist))
  # 下载该list 使用超时20 10好像小了点
  print 'Fetching list of %d files' % len(imglist)
  failure = threadDownloadFromList(imglist, directory=directory, timeout=20)
  print "%d failed to fetch." % len(failure)
  # 清理
  # 1.添加后缀
  print 'Adding extension ...',
  for fname in os.listdir(directory):
    addExtension(directory + os.sep + fname, '.jpg')
  print 'done.'
