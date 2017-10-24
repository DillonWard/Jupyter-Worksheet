# Read in the CSV Fisher's Iris data set and store it into a numpy array
# Author: Dillonward2017@gmail.com
# Date: 24/10/17

import numpy as np
import csv

# Open the CSV file
with open('./data/fishers-data-set.csv') as csvfile:
    # Read in the CSV file
    # NOTE: everything is separated everything by ','
    readCSV = csv.reader(csvfile, delimiter=',')

    # Arrays for storing the CSV values are initialized
    # will be used later for storing
    sepal_length = []
    sepal_width = []
    petal_length = []
    petal_width = []
    iris_class = []


    # loops for the size of the CSV file
    for row in readCSV:

        # temporary values for appending to the arrays
        # the first row '[0]' will be the sepal length
        # the second will be sepal width, etc.
        sepal_l = row[0]
        sepal_w = row[1]
        petal_l = row[2]
        petal_w = row[3]
        iris_c = row[4]

        # appending the values that are read in from the files to arrays
        sepal_length.append(sepal_l)
        sepal_width.append(sepal_w)
        petal_length.append(petal_l)
        petal_width.append(petal_w)
        iris_class.append(iris_c)

        print(iris_c)


    # printing out for testing
    # print(sepal_length)
