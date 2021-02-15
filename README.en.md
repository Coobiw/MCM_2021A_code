# MCM_2021A_code

## Introduction
The repository is about some of my codes which I do in 2021 MCM Question A.
This data warehouse is about part of the data and code for my question A in the 2021 Mathematical Modeling Contest.

### Data source statement:

[1]Fungi Database: https://github.com/dsmaynard/fungal_biogeography/tree/master/fungi_data.

[2]WorldClim Global Climate Data database(https://www.worldclim.org/)

[3]The vegetation distribution data (https://commons.wikimedia.org/wiki/File:Vegetation.pn)

The code uses the python programming language, and the virtual environment uses Anaconda to manage python related libraries (such as: numpy, pandas, matplotlib, sklearn, scipy, etc.)

## Software function
### Software function description:

[1] The two .py files, 2Dpicture and 3D-Normal, are used to draw the 2D and 3D images of the fungal growth rate with the two factors of temperature and humidity. Among them, the 2D image is described by the heat map, and the 3D image is selected for use The surface map also shows the contours except for the contours on the three planes, which is relatively clear.

[2] The double.py file is used to describe the solution of the differential equation of double fungus/multi fungus. Here, the combination of the SIS model and the population competition model is used, which makes it difficult to obtain the analytical solution of the differential equation. For the convenience of visualization, we still use quantitative Analysis, so choose to find a numerical solution and draw (note: the first part is Logistic (single-species S-curve growth), the second half is the curve drawn by the numerical solution of the differential equation).

[3] The Logistic.py file draws the single population growth curve and growth rate curve of 4 fungi in a single figure.

[4] The Normal_fit.py file uses the least squares method to fit two normal distributions. Why you need to describe the two can be found in our paper.

[5] The Regression.py file uses multiple regression analysis to determine the linear relationship between the fungal decomposition rate, the growth rate of the fungus, and the fungus's moisture resistance (see the data folder for the data), and two two-dimensional images and projections are made. Vitu. (Ternary regression analysis)

[6] The remaining two documents are graphs of the decomposition percentage of trees (unit: %) and the percentage rate of decomposition of trees (unit: %/day) over time. The formula is still in our paper.

If you are interested in our paper, you can send an e-mail to my personal mailbox, and we will share it when circumstances permit.