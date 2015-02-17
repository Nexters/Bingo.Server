from django.core.files.storage import default_storage
import datetime
import hashlib
import os

def generateNewFilePath(dir_path, f_name):
	file_path = dir_path + f_name
	i = 1
	while isExistingFile(file_path):
		suffix = '(' + str(i) + ')'
		if isExistingFile(modifyFilePath(file_path, suffix)):
			i = i + 1
		else:
			file_path = modifyFilePath(file_path, suffix)
	return file_path

def isExistingFile(file_path):
	if os.path.exists(file_path):
		return True
	else:
		return False

def modifyFilePath(ori_file_path, suffix):
	ext = getExt(ori_file_path)
	temp = len(ori_file_path) - len(ext) - 1
	ret_file_path = ori_file_path[:temp] + suffix + '.' + ext
	return ret_file_path

def getExt(file_path):
	temp = file_path.split('.')
	ext = temp[len(temp)-1]
	return ext

class FileUploader:

	BASE_DIR = os.path.dirname(os.path.dirname(__file__))
	
	def __init__(self, target_file, dir_middle_path):
		self.dir_path = os.path.join(self.BASE_DIR, dir_middle_path)
		self.target_file = target_file
		self.file_path = generateNewFilePath(self.dir_path, self.target_file.name)
		self.ext = getExt(self.file_path)

	def uploadFile(self):
		with open(self.file_path, 'wb+') as destination:
			for chunk in self.target_file.chunks():
				destination.write(chunk)

	def getFilePath(self):
		return self.file_path



