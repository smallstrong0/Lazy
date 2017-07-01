#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys


def find_source_and_rename_it(path,oldname,newname,type):
	for file in os.listdir(path):
   		if file == oldname:
   			os.rename(os.path.join(path,file),os.path.join(path,newname+"."+type))


def rename(oldname,newname,type):# 准备找到文件中 然后找到文件换名字
	print oldname + "   change name to ====>     " + newname+"."+type

	if os.path.exists(os.getcwd()+"/hdpi"): 
		find_source_and_rename_it(os.getcwd()+"/hdpi",oldname,newname,type)
	if  os.path.exists(os.getcwd()+"/xhdpi"): 		
		find_source_and_rename_it(os.getcwd()+"/xhdpi",oldname,newname,type)
	if  os.path.exists(os.getcwd()+"/xxhdpi"): 		
		find_source_and_rename_it(os.getcwd()+"/xxhdpi",oldname,newname,type)
	if  os.path.exists(os.getcwd()+"/xxxhdpi"): 		
		find_source_and_rename_it(os.getcwd()+"/xxxhdpi",oldname,newname,type)
	 

def run():
	f = open(os.getcwd()+"/name.txt", 'r')
	for line in f.xreadlines():
		list = line.split("=",1)
		type = list[0].split(".",1)[1]
		rename(list[0],list[1].replace("\n",""),type)
	f.close()
	print '\033[1;32;40m'
	print "更名成功:请\n1.运行python tinypng.py进行压缩图片，请耐心等待\n2.压缩完成之后会出现Android的四个资源文件夹，东西在里面自行copy"
	print '\033[0m'

if __name__ == "__main__":
    run()

