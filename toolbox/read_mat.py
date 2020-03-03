#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 15:34:32 2020

@author: skand
"""

from os.path import dirname, join as pjoin
import scipy.io as sio
from datetime import timedelta
from datetime import  date
mat_fname = 'Data/wiki_crop/wiki.mat'

def read_mat(data_dir,file_name):
    """image_list is the list of file_names
        label_list is the list of labels"""
    mat_fname=data_dir+file_name
    mat_contents = sio.loadmat(mat_fname)
    image_list_array=mat_contents['wiki'][0][0][2][0]
    
    dob=mat_contents['wiki'][0][0][0][0] #date_of_birth, matlab datenum format
    photo_taken=mat_contents['wiki'][0][0][1][0] #date the photo was taken
    
    label_list=[]
    image_list=[]

    for i in range(len(dob)):
        dob_dt=date.fromordinal(dob[i]) + timedelta(days=0) - timedelta(days = 366)
        label_list.append(photo_taken[i]-dob_dt.year)
        image_list.append(image_list_array[i][0])
    return image_list,label_list




