#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
import os.path
import tinify

tinify.key = "gfx-gzBLyuVpvleuuf_ragZBcqKmrkWi"		# API KEY

# 压缩的核心
def compress_core(inputFile, outputFile):
	source = tinify.from_file(inputFile)
	source.to_file(outputFile)

# 压缩一个文件夹下的图片
def compress_path(path,suf):
	if not os.path.isdir(path):
		print "这不是一个文件夹，请输入文件夹的正确路径!"
		return
	else:
		fromFilePath = path 			# 源路径

		toFilePath = os.getcwd()+"/drawable-"+suf 		# 输出路径
		print "fromFilePath=%s" %fromFilePath
		print "toFilePath=%s" %toFilePath

		for root, dirs, files in os.walk(fromFilePath):
			print "root = %s" %root
			print "dirs = %s" %dirs
			print "files= %s" %files
			for name in files:
				fileName, fileSuffix = os.path.splitext(name)
				if fileSuffix == '.png' or fileSuffix == '.jpg' or fileSuffix == '.jpeg':
					toFullPath = toFilePath + root[len(fromFilePath):]
					toFullName = toFullPath + '/' + name
					if os.path.isdir(toFullPath):
						pass
					else:
						os.mkdir(toFullPath)
					compress_core(root + '/' + name, toFullName)
			break									



def run():
	if os.path.exists(os.getcwd()+"/hdpi"): 
		compress_path(os.getcwd()+"/hdpi","hdpi")
	if  os.path.exists(os.getcwd()+"/xhdpi"): 		
		compress_path(os.getcwd()+"/xhdpi","xhdpi")	
	if  os.path.exists(os.getcwd()+"/xxhdpi"): 		
		compress_path(os.getcwd()+"/xxhdpi","xxhdpi")	
	if  os.path.exists(os.getcwd()+"/xxxhdpi"): 		
		compress_path(os.getcwd()+"/xxxhdpi","xxxhdpi")	
	
	print '\033[1;32;40m'
	print "ok\npower by smallstrong"
	print '\033[0m'

if __name__ == "__main__":
    run()

