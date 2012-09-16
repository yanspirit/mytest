# -*- coding:UTF8 -*-
#import rhinoscriptsyntax as rs

import re
str1 = "abc \\ 123 456"
print re.findall("\\\\",str1)  # ����r����r����
print re.findall(r"\d\Z",str1) # ��"r"����������ַ�

p = re.compile('(a)b')
m = p.match('ab')
print m.group()

s = "aaa1 22 gg 333 ccc 4444 pppp 55555 666"
print re.findall(r"\b\d{3}\b",s)
print re.findall(r"\b\d{2,4}\b",s)

s2 = "aaa111aaa , bbb222 , 333ccc"
#print re.findall( r"(?<=[a-z]+)\d+(?=[a-z]+)",s2 )
#print re.findall( r"\d+(?=[a-z]+)",s2 )
### Ŀ�� ǰ����a-z 1-��Ρ��м�����1-9 1-���
print re.findall(r"\d+(?!\w+)",s2)
#��������
print re.findall(r"[a-z]+(\d+)[a-z]+",s2) # ֻ����()�����
s3 = 'aaa111aaa,bbb222,333ccc,444ddd444,555eee666,fff777ggg,hhh888hhh'
print re.findall(r"([a-z]+)\d+([a-z]+)",s3) #�������������
##��(?P<name>��)�� ������
print re.findall( r"(?P<g1>[a-z]+)\d+(?P=g1)",s3 ) #�ҳ����м�������ֵ�ǰ��ͬ�����ĸ
print re.findall(r"([a-z]+)\d+\1",s3)
s4 = "111aaa222aaa111,333bbb444bb33"
print re.findall( r"(\d+)([a-z]+)(\d+)(\2)(\1)", s4 ) #���֡���ĸ�����֡���ĸ��������Գ�
print re.compile(r"(\d+)([a-z]+)(\d+)(\2)(\1)").findall(s4)
#
##compile( rule [,flag] ) ʹ��compile����
s5 = "111,222,aaa,bbb,ccc333,444ddd"
print re.compile(r"\d+\b").findall(s5) # \�˸� ƥ��һ��λ�ڿ�ͷ�����֣�û��ʹ��Mѡ��
#
s6 = "123 456\n789 012\n345 678"
print re.compile(r"^\d+",re.M).findall(s6) # ƥ��λ��(M/����)��ͷ������

rcm=re.compile(r"\d+$")# ���ڡ�$����˵��û��ʹ��Mѡ���ƥ�����һ����β�����֣�����678���������Ժ󣬾���ƥ�������β������456 012��678��.
print re.compile(r"\d+$",re.M).findall(s6) # 






