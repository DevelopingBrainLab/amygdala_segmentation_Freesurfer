# Author: Jianan Chen, Western University

''' this file is written in python2
    to compile: python Iterate_dir_file.py
    look for: 3 csv files in 'result' folder
'''

import os
import re
import csv


rootdir = "/scratch/eduerden/pond/Groups"

# current directory
cwd = os.getcwd()
# new folder 'result' containing vlume data
dir = os.path.join(cwd, 'result')
os.mkdir(dir)

# open csv files
# within the new folder 'result'
file_l = "left_vol.csv"
file_r = "right_vol.csv"
file_all = "all_vol.csv"
path_l = os.path.join(dir, file_l)
path_r = os.path.join(dir, file_r)
path_all = os.path.join(dir, file_all)
left_vol = open(path_l, 'w+')
right_vol = open(path_r, 'w+')
all_vol = open(path_all, 'w+')

# writers of csv files
field_name = ['Side', 'Sub_id', 'Nuclei', 'Volume']
writer_l = csv.DictWriter(left_vol, fieldnames=field_name)
writer_r = csv.DictWriter(right_vol, fieldnames=field_name)
writer_all = csv.DictWriter(all_vol, fieldnames=field_name)
# write the headers
writer_l.writeheader()
writer_r.writeheader()
writer_all.writeheader()

##### DEBUG #####
sbj_per_grp = []

''' record the subjectID: volume in dictionaries to print (for test)
    write data into 3 csv files
'''
def getAmygVol (vol_txt, sbj_ID, side):
    sbj = sbj_ID + side  # e.g. 1050207_[lr]

    try:
        txt = open(vol_txt, 'r')  # open .txt file
        lines = txt.readlines()

        # write data into csv
        if (side == "_L"):  # all left
            for line in lines:
                results = line.split()
                nuclei = "lh" + results[0] # to match Dr.Emma Duerden's excel sheets' naming
                volume = float(results[1])

                # write one row into corresponding csv
                row = {'Side': 'left', 'Sub_id': sbj_ID, 'Nuclei': nuclei, 'Volume': volume}
                writer_l.writerow(row)
                writer_all.writerow(row)

        elif (side == "_R"):  # all right
            for line in lines:
                results = line.split()
                nuclei = "rh" + results[0] # to match Dr.Emma Duerden's excel sheets' naming
                volume = float(results[1])

                # write one row into corresponding csv
                row = {'Side': 'right', 'Sub_id': sbj_ID, 'Nuclei': nuclei, 'Volume': volume}
                writer_r.writerow(row)
                writer_all.writerow(row)

    finally:
        txt.close()

''' go inside the 'Groups' dir
'''
def iterate(rootdir):
    for sbj_grp in os.listdir(rootdir):
        flag = False ###

        if sbj_grp.startswith("Group"): # inside 'Groups'
            sbj_grp_path = os.path.join(rootdir, sbj_grp)
            print(sbj_grp) ###
            sbj_count = 0 ### processed sbj
            left_count = 0 ### processed left
            right_count = 0 ### processed right

            for sbj in os.listdir(sbj_grp_path): # inside 'Group##'
                if sbj.startswith("sub"):
                    sbj_path = os.path.join(sbj_grp_path, sbj)
                    sbj_ID = sbj[4:11]
                    # print(sbj_path) ###

                    for data in os.listdir(sbj_path): # inside 'sub-...'
                        if data == "mri":
                            mri_path = os.path.join(sbj_path, data)
                            l_r_num = 0
                            lh_txt_path = ""
                            rh_txt_path = ""

                            # only read the subjects with BOTH lh and rh...
                            for txt in os.listdir(mri_path): # inside 'mri'
                                if (txt.startswith("lh.amyg") and txt.endswith(".txt")) or (txt.startswith("rh.amyg") and txt.endswith(".txt")):
                                    # vol_txt_path = os.path.join(mri_path, txt)
                                    flag = True ###

                                    if (txt.startswith("l")):  # indicate right of left amygdala
                                        l_r_num += 1 # sbj has lh...
                                        lh_txt_path = os.path.join(mri_path, txt)
                                        left_count += 1 ###
                                        # getAmygVol(vol_txt_path, sbj_ID, "_L")  # use the readfile funnction to get the volumes
                                    else:
                                        l_r_num += 1 # sbj has rh...
                                        rh_txt_path = os.path.join(mri_path, txt)
                                        right_count += 1 ###
                                        # getAmygVol(vol_txt_path, sbj_ID, "_R")  # use the readfile funnction to get the volumes

                            if (flag == True): ###
                                sbj_count += 1 ###
                                flag = False ###
                            if l_r_num == 2: # subject has BOTH lh and rh...
                                print("%s both l&r" % sbj_ID)          
                                getAmygVol(lh_txt_path, sbj_ID, "_L")
                                getAmygVol(rh_txt_path, sbj_ID, "_R")
                            # reset
                            l_r_num = 0
                            lh_txt_path = ""
                            rh_txt_path = ""

            print("\n processed sbj: %d" % sbj_count) ###
            print("\n left_count: %d" % left_count) ###
            print("\n right_count: %d\n\n" % right_count) ###



# do magic
iterate(rootdir)
print("\n\n\t\tC'est fini.\n")
left_vol.close()
right_vol.close()
all_vol.close()


#ssh -X jchen985@niagara.scinet.utoronto.ca
#rootdir = "/Users/jiananchen/Desktop/CS4490/anatomicals"
#rootdir = "/scratch/e/eduerden/eduerden/POND/Groups"
# scp /Users/jiananchen/Desktop/Iterate_dir_file.py jchen985@niagara.scinet.utoronto.ca:/scratch/e/eduerden/jchen985/
