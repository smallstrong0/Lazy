#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys


def run():
	print '\033[1;32;40m'
	print "需要更名的有以下图片"
	print '\033[0m'

	f = open(os.getcwd()+"/name.txt", "wt") 
	for root, dirs, files in os.walk(os.getcwd()+"/hdpi"):		
		for name in files:
			f.write(name+"\n")
			print name
	f.close()
	print '\033[1;32;40m'
	print "请\n1.打开当前目录下的name.txt\n2.输入重新更改的名字(例子：demo.png=smallstrong)\n3.注意每一行更改一个文件的名字，更名后缀png或者jpg不需要加\n4.写完之后运行python cname.py命令进行文件更名"
	print '\033[0m'
	

if __name__ == "__main__":
    run()

