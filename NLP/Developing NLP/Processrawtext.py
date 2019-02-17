#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 07:27:37 2019

@author: pandit
"""
import nltk
from  nltk.corpus import gutenberg as cg
from  nltk.tokenize import sent_tokenize as st

#Get raw data from file
def fileread():
    file_contents=open("/home/pandit/Downloads/NLP/Developing NLP/rawtext.txt","r").read()
    
    #print file contents
    return file_contents

def localtextvalue():
    text="""one paragraph,  of 100-250 words,which can be used
        and then gradually prune it down """
    return text
    
def readcorpus():
    raw_content_cg=cg.raw("burgess-busterbrown.txt")
    return raw_content_cg[0:1000]

if __name__ =="__main__":
    print(" ")
    print("------Output from Raw Text file-------")
    filecontentdetails=fileread()
    print(filecontentdetails)
    st_list_rawfile=sent_tokenize(filecontentdetails)
    print(len(st_list_rawfile))
    
    print( "")
    print( "-------Output from assigned variable-------")
    print( "")
    localveriabledata = localtextvalue()
    print( localveriabledata)
    # sentence tokenizer
    st_list_local = st(localveriabledata)
    print( len(st_list_local))
    print (st_list_local)

    print( "")
    print( "-------Output Corpus data--------------")
    print( "")
    fromcorpusdata = readcorpus()
    print (fromcorpusdata)
    # sentence tokenizer
    st_list_corpus = st(fromcorpusdata)
    print (len(st_list_corpus))