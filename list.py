#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys



def write_name(path):
	f = open(os.getcwd()+"/name.txt", "wt") 
	for root, dirs, files in os.walk(path):		
		for name in files:
			if (name[0] != "."):
				f.write(name+"\n")
				print name
	f.close()			

def run():
	print '\033[1;32;40m'
	print "需要更名的有以下图片"
	print '\033[0m'

	
	
	if os.path.exists(os.getcwd()+"/hdpi"): 
		write_name(os.getcwd()+"/hdpi")
	elif  os.path.exists(os.getcwd()+"/xhdpi"): 		
		write_name(os.getcwd()+"/xhdpi")
	elif  os.path.exists(os.getcwd()+"/xxhdpi"): 		
		write_name(os.getcwd()+"/xxhdpi")	
	elif  os.path.exists(os.getcwd()+"/xxxhdpi"): 		
		write_name(os.getcwd()+"/xxxhdpi")	
	else:
		print "陛下，该目录没有找到 hdpi xhdpi xxhdpi xxxhdpi中的任何一个，您让臣妾怎么玩？"	
	
	
	print '\033[1;32;40m'
	print "请\n1.打开当前目录下的name.txt\n2.输入重新更改的名字(例子：demo.png=smallstrong)\n3.注意每一行更改一个文件的名字，不要有空行记住啊亲，更名后缀png或者jpg不需要加\n4.写完之后运行python cname.py命令进行文件更名"
	print '\033[0m'
	

if __name__ == "__main__":
    run()

