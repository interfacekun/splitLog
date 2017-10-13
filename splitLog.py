#!/usr/bin/env python
# coding: utf-8 -*-

#[[
 # @brief:		分割日志
 # @author:		kun si
 # @email:	  	627795061@qq.com
 # @date:		2017-10-12
#]]

import os
import sys
import getopt
import multiprocessing
import time

def splitStart(megaByte, inputPath, outputPath, fileName):
	startTime = time.time()
	print("raw fileName", fileName)
	rawFile = inputPath + "/" + fileName
	postfix = 1
	ro = open(rawFile, "rb")
	readSize = 1024 * 512
	readCount = 0 
	sliceFile = outputPath + "/" + os.path.splitext(fileName)[0] + "_0" + str(postfix) + ".log"

	oo = open(sliceFile,"wb")
	sizehint = megaByte * 1024 * 1024
	position = 0
	lines = ro.readlines(sizehint)
	oo.writelines(lines)
	oo.close()

	while ro.tell() - position > 0:
		postfix = postfix + 1
		if postfix < 10 :
			sliceFile = outputPath + "/" + os.path.splitext(fileName)[0] + "_0" + str(postfix) + ".log"
		else:
			sliceFile = outputPath + "/" + os.path.splitext(fileName)[0] + "_" + str(postfix) + ".log"

		oo = open(sliceFile,"wb")
		position = ro.tell()
		lines = ro.readlines(sizehint)
		oo.writelines(lines)
		oo.close()

	ro.close()

	stopTime = time.time()
	handleTime = stopTime - startTime
	print("split %s done! use %ds."%(fileName, handleTime))

def splitLogs(megaByte, inputPath, outputPath):
	threads = []

	for root, dirs, files in os.walk(inputPath):
		for fileName in files:
			thread = multiprocessing.Process(target = splitStart,args=(megaByte, inputPath, outputPath, fileName))
			threads.append(thread)

	for t in threads:
		t.start()

if __name__ == "__main__":
	rawFileDir = "./rawLogs/"
	slitedFileDir = "./slicesLogs/"
	megaByte = 10

	opts, args = getopt.getopt(sys.argv[1:], "m:i:o")
	for op, value in opts:
		if op == "-m":
			megaByte = value
		elif op == "-i":
			rawFileDir = value
		elif op == "-o":
			slicesLogs = value
	
	splitLogs(megaByte, rawFileDir, slitedFileDir)