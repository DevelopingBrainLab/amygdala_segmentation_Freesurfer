# Author: Jianan Chen, Western University
# to generate the bash script "segment_amygdala.sh"
# which calls the segmentHA_T1.sh command
# for each subject in each Group folder

import os

# Algorithm:
# if it is a directory:
	# if its name starts with 'Group':
		# create 'segment_amygdala.sh' inside it
		# for each subject folder (sbj folders only):
			# copy the subject folder name, concatenate with the command
			# write it into 'segment_amygdala.sh'

cwd = os.getcwd()
scp_name = "segment_amygdala.sh"
# openings = ["#!/bin/bash\n", 
# 			"#\n", 
# 			"#SBATCH --nodes=20\n", 
# 			"#SBATCH --time=24:00:00\n", 
# 			"#SBATCH --job-name abide20\n", 
# 			"#SBATCH --ntasks=20\n"]
line = " \n" # initialized empty string


for folder in os.listdir(cwd):
	folder_path = os.path.join(cwd, folder)

	if os.path.isdir(folder_path):
		if folder.startswith("Group"):

			scp_path = os.path.join(folder_path, scp_name)
			file = open(scp_path, "w+")
			print("created %s in %s" % (scp_name, folder_path))

			openings = ["#!/bin/bash\n", 
						"#\n", 
						"#SBATCH --nodes=20\n", 
						"#SBATCH --time=24:00:00\n", 
						"#SBATCH --job-name " + folder + "\n", 
						"#SBATCH --ntasks=20\n"]
			file.writelines(openings)
			print("write openings")

			line = "export SUBJECTS_DIR=" + folder_path + "\n"
			file.write(line)
			print("write export")

			print("write cmds")
			# for sbj in sbj_list:
			for sbj in os.listdir(folder_path):
				if sbj.startswith("sub"):  # ignore any other weird files
					print("\t one line")
					line = "segmentHA_T1.sh " + sbj + " " + folder_path + "\n"
					file.write(line)

			file.close()
			# sbj_list = []


