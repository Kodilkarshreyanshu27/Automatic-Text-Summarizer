# -*- coding: utf-8 -*-
"""lexrank.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DtXQLy7AWV7xnOYLEk-vwb0wrO47ab-E
"""


import sumy
import numpy
import os


from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

import nltk
nltk.download('punkt')



def lexrank() : 
    directory  = "/home/atharva007/Documents/GitHub/Automatic-Text-Summarizer/project/main/documents/one.txt"
    # opening the file 
    file1 = open(directory , "r")

    # reading the file 
    document = file1.read()

    # printing the document 
    print(document)


    parser = PlaintextParser.from_string(document,Tokenizer("english"))

    # Using LexRank
    summarizer = LexRankSummarizer()
    #Summarize the document with 2 sentences
    summary = summarizer(parser.document, 2)

    print()
    print()
    print("The output of the Algorithm is : ")

    output_text = ""

    print("Sumary : " , summary)
    print("summary type : " , type(summary))

    file = "output2.txt"

    directory = os.getcwd()
    print("current working drectory : " , directory)

    with open(os.path.join(directory , file) ,  'w') as file2 : 
        for sentence in summary:
            print(sentence)

            # writing into the file2
            file2.write(str(sentence))


lexrank()