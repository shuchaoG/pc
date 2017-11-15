# -*- coding:utf-8 -*-
import re


#标签工具类
class Tool:
    #去除img标签,1-7位空格,&nbsp;
    removeImg = re.compile('<img.*?>| {1,7}|&nbsp;')
    #删除超连接标签
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行符换成\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #制表符<td>换成\t
    replaceTD= re.compile('<td>')
    #换行符或者双换行符换成\n
    replaceBR = re.compile('<br><br>|<br>')
    #去掉其余标签
    removeExtraTag = re.compile('<.*?>')
    #去掉多余空行
    removeNoneLine = re.compile('\n+')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        x = re.sub(self.removeNoneLine,"\n",x)
        #strip()
        return x.strip()
