# amygdala_segmentation_Freesurfer
Automatic files/directories generations and resulting data readings for using the brain segmentation of Freesurfer

- These scripts are tools along using the brain segmentation function of the Freesurfer software.
- These python scripts are written in Python 2
- The order of using these 3 files should be: **copy20.py -> write_seg_bash.py -> get_vol.py**


## copy20.py ##
#### This script copies and place the nifti files into directories("Group ##") of 20 files. ####
- You should have all the nifti files (the MRI sources, '.nii.gz' or '.nii' files) placed inside one directory.
- Go to this directory: `cd your_directory`
- Update the `orig_dir` variable with the **absolute path** to your nifti files directory.
- To compile: `python copy20.py` 
- Generated group directories have names like "Group1".
- It generally takes a long time, be patient.


## write_seg_bash.py ##
#### This script generates the bash scripts to run the hypocampus & amygdala (brain structures) segmentation commands of the Freesurfer ####
- The bash scripts will be generated inside each group directories.
- Group directories have name like "Group 1".
- You will need to manually compile these bash scripts containing the Freesurfer commands.
- To compile: `python write_seg_bash.py`


## get_vol.py ##
#### This script reads all the resulted reconstructed amygdala volumes inside processed subjects' nifti directories, and writes these data into 3 csv files ####
- The script will create a "result" directory containing the 3 csv files. 
- This "result" directory will be placed under your currently working directory ("get_vol.py" needs to present under your working directory, too).
- The csv files are:
	1. "all_vol.csv" (all volume data for both left and right amygdala),
	2. "right_vol.csv" (just right amygdala volume), 
	3. "left_vol.csv" (just left amygdala volume). 
- To compile: `python get_vol.py`

Some examples of the format of the csv files:

![sample: all_vol.csv](/images/all_vol.png) 

![sample: right_vol.csv](/images/right_vol.png) 

![sample: left_vol.csv](/images/left_vol.png)

