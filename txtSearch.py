import re
import time
import os
showOption = True

def filterDirectory(parentDirectory):
	txtFiles = []
	folderList = []
	for item in parentDirectory:
		if (os.path.splitext(item)[1] == ''):
			folderList.append(item)
		if (os.path.splitext(item)[1] == '.txt'):
			txtFiles.append(item)
	return [txtFiles, folderList]

def searchForString(searchString, txtFile, fileName):
		lineCount = 0
		matchCount = 0
		for line in txtFile:
			lineCount += 1
			if re.search(searchString, line.strip()):
				matchCount += 1
				print("Match number " + str(matchCount) + " found for term \"" + searchString + "\" at line number: " + str(lineCount))
				print("'" + line.strip() + "'\n")
		print("Search Finished for file: " + fileName)
		print("Match frequency:" + str(matchCount))
		print("-----------------------------------------------------------------")

def stringInFile():
	print("Welcome to .TXT term finder\n")
	inputString = input("Enter a search term string\nString to find: ")
	try:
		inputName = input("Enter a file name to search\nFile name: ")
		inputFile = open(inputName,"r")
	except:
		print("\n File not found (or possibly don't have permissions), please try again and enter in form txtFile.txt and make sure it's in the same folder as main.py")
		time.sleep(2)
		showOption = True
	time.sleep(2)
	searchForString(inputString, inputFile, inputName) 
	print("\n")

def stringInDirectory():
	inputString = input("Enter a search term string\nString to find: ")
	try:
		directoryName = input("Please enter a directory name\nDirectory path:")
		time.sleep(2)
		fileList = filterDirectory(os.listdir(directoryName.strip().replace("/", "//")))
		print(fileList)
		for file in fileList[0]:
			textFile = open(directoryName+"\\"+file, "r")
			searchForString(inputString, textFile, file)
	except:
		print("\n Directory not found, please try again and enter in form C:/Folder1/Folder2")
		time.sleep(2)
		showOption = True



while (showOption == True):
	print("1. Find all strings in a .TXT\n")
	print("2. Find all strings in .TXT files in a directory\n")
	try:
		optionNumber = int(input("Enter a option number 1-2.\nOption Number: "))
	except:
		print("Please try again and enter a valid number 1-2")
	if (optionNumber==1):
	 	showOption = False
	 	stringInFile()

	if (optionNumber==2):
	 	showOption = False
	 	stringInDirectory()

	else:
	 	showOption= True

	time.sleep(2)
