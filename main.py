# -*- coding: utf-8 -*-

import os
from os import listdir
from os.path import isfile, join
import subprocess
import random
 

def getAllFiles(curdir):
        filenames = []
        for dirpath,dirnames,fnames in os.walk(curdir):
                for fn in fnames:
                        filenames.append(os.path.join(dirpath,fn))
                
        return filenames


def main():
    workpath =  r'C:\BaiduPanDownload'
    pl = getAllFiles(workpath) 
    for x in pl:
        tails = '.baiduyun.p.downloading'
        if x.find(tails)>0:
                s_fn = x.split(tails)[0]
                if os.path.exists(s_fn) :
                        os.unlink(x)
                        print("Found source file : %s" % s_fn[s_fn.rfind('/')+1:])
                        print("Delete Over : %s"% x[x.rfind('/')+1:])
                else:
                        print("This file is downloading: %s"% x[x.rfind('/')+1:])                          
            
            
    print( '>'*12)                    
         

if __name__ == '__main__':
	main()

        

