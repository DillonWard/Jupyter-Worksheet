# Read in the CSV Fisher's Iris data set and store it into a numpy array
# Author: Dillonward2017@gmail.com
# Date: 24/10/17
# (1) Adapted from https://matplotlib.org/users/customizing.html
# (2) Adapted from https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib
# (3) Adapted from https://matplotlib.org/api/markers_api.html
 
import numpy as np
import csv
import matplotlib.pyplot as pl # ref: (1)
import matplotlib.patches as mpatches

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
    fishers_set = []
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

        # a dictionary of arrays
        fishers_set = [{"sepal_length" : sepal_length,
         "sepal_width " : sepal_width, 
         "petal_length" : petal_length, 
         "petal_width" : petal_width, 
         "iris_class" : iris_class}]


# Plot the data read in from the CSV file to a graph
# Date: 25/10/17

# Used for setting the size of the figure to be displayed - ref: (2)
pl.rcParams['figure.figsize'] = 16, 8

# defines which parameters are going to be plotted onto the graph
# the marker is only for changing what the plots look like - ref: (3)
pl.scatter(sepal_length, sepal_width, marker='.')

# the title will be displayed above the graph
pl.title('Sepal Length vs Sepal Width')

# define the x/y labels that are to be plotted
pl.xlabel('Sepal Length')
pl.ylabel('Sepal Width')

# display the graph
pl.show()
