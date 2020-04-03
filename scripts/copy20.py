# Author: Jianan Chen, Western University
# iterate throught he source directory
# mkdir for every 20 files
# copy each file to new directory

import sys
import time
import random

import os
import shutil
from distutils.dir_util import copy_tree


orig_dir = "/scratch/eduerden/pond/pond_transforms"

mkdir_num = 1
dir_count = 1
obj_count = 1
cwd = os.getcwd()
new_dir = ""  # group directory (size of 20), naming 1,2,3...
destination = ""  # destination directory (with the same old folder name)

# Algorithm:
# is the file a directory?
	# NO: next file, obj_count++
	# YES: is the dir_count % 20 == 1? (the 1st, 21st, 41st...)
		# NO: copy, dir_count++
		# YES: mkdir(str(mkdir_num)), copy, mkdir_num++, dir_count++

for obj in os.listdir(orig_dir):
	source = os.path.join(orig_dir, obj)

	if os.path.isdir(source):
		if dir_count % 20 == 1:
			dir_name = "Group" + str(mkdir_num)
			new_dir = os.path.join(cwd, dir_name)
			os.mkdir(new_dir)
			###
			sys.stdout.write("Please wait... copying for Group[{0}]   \r".format(mkdir_num))
			sys.stdout.flush()
			time.sleep(random.random())
    		###
			mkdir_num += 1

		destination = os.path.join(new_dir, obj)
		copy_tree(source, destination)
		dir_count += 1

	else:
		obj_count += 1

# REPORT:
print("%d files in total" % obj_count)
# print("%d subject folders" % dir_count)
print("%d group folders created" % (mkdir_num-1))
