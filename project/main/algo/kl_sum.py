# -*- coding: utf-8 -*-
"""kl-sum.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AWachzsGEfgJVSNfVY0cjEEHvuSFClhm
"""

import sumy

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.kl import KLSummarizer
import nltk
nltk.download('punkt')

import os




"""

document = Machine learning is a branch of artificial intelligence (AI) and computer science which focuses on the use of data and algorithms to imitate the way that humans learn, gradually improving its accuracy.

IBM has a rich history with machine learning. One of its own, Arthur Samuel, is credited for coining the term, “machine learning” with his research (PDF, 481 KB) (link resides outside IBM) around the game of checkers. Robert Nealey, the self-proclaimed checkers master, played the game on an IBM 7094 computer in 1962, and he lost to the computer. Compared to what can be done today, this feat seems trivial, but it’s considered a major milestone in the field of artificial intelligence.

Over the last couple of decades, the technological advances in storage and processing power have enabled some innovative products based on machine learning, such as Netflix’s recommendation engine and self-driving cars.

Machine learning is an important component of the growing field of data science. Through the use of statistical methods, algorithms are trained to make classifications or predictions, and to uncover key insights in data mining projects. These insights subsequently drive decision making within applications and businesses, ideally impacting key growth metrics. As big data continues to expand and grow, the market demand for data scientists will increase. They will be required to help identify the most relevant business questions and the data to answer them.

Machine learning algorithms are typically created using frameworks that accelerate solution development, such as TensorFlow and PyTorch.

"""


def write(directory , file , summary) : 
    with open(os.path.join(directory , file) ,  'w') as file2 : 
        for sentence in summary:
            print(sentence)

            # writing into the file2
            file2.write(str(sentence))
    
    return True

def caller(write , directory , file , summary) : 
    return write(directory , file , summary)


def kl_sum() : 
    directory  = "/home/atharva007/Documents/GitHub/Automatic-Text-Summarizer/project/main/documents/one.txt"
    # opening the file 
    file1 = open(directory , "r")

    # reading the file 
    document = file1.read()

    # printing the document 
    print(document)

    # For Strings
    parser=PlaintextParser.from_string(document,Tokenizer("english"))
    # Using KL
    summarizer = KLSummarizer()
    #Summarize the document with 4 sentences
    summary = summarizer(parser.document,4)

    print()
    print()
    print("The output of the Algorithm is : ")

    output_text = ""

    print("Sumary : " , summary)
    print("summary type : " , type(summary))

    file = "output1.txt"

    directory = os.getcwd()
    print("current working drectory : " , directory)

    result = caller(write , directory , file , summary)
    print(result)

    

        

kl_sum()