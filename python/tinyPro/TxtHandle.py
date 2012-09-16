#!/usr/local/bin/python

str_seperator = "=================================================================================="

timePointName = ["enter OpenNextImage at",#0  

                  "enter OpenImage at",#1  

                  "In OpenImage send On_ImageRefresh at",#2  

                  "leave OpenImage at",#3  

                  "leave OpenNextImage at",#4  

                  "enter LoadImage at",#5  

                  "decode began at",#6  

                  "enter DrawClient at",#7  

                  "leave DrawClient at",#8  

                  "decode end at",#9  

                  "in LoadImage send On_ImageRefresh at",#10  

                  "leave loadImage at",#11  

                  "second enter DrawClient at",#12  

                  "second leave DrawClient at" #13  

                  ]  


itemNumber= 0;  

avgTotal = 0; #13-0  

avgFirstDraw = 0; #8-2  

avgLoadImage = 0; #11-5  

avgSecondDraw = 0;#13-10  



fobj = open("F:\log.txt","r")
imageTimeSta = {}


