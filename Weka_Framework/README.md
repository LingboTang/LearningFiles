## Introduction: ##

First of all, I would like to give credit to the authors who created this template here: http://www.programcreek.com/2013/01/a-simple-machine-learning-example-in-java/

This is very simple weka program based on the development of weka API. However, the programming API of the version 3.8.1 (Current Latest Version Until April 6th, 2017) for some unknown reason is not stable, some API functions are missing or mislinked. Therefore, I suggest developer download the stable version 3.6.2 for programming use. You can easily link it in any java IDE. (I used intelliJ). For convenient purpose, I ran my program in intelliJ as well. If developers are more convenient with terminal debugging, you should parse some input options through command line.

In the program I used few important class:


	Evaluation: This is a super class of all kinds of evalution. I have a `classify` function in my class which allows you to plug in any `Classifier` model in this evaluation.

	Instances: This is the class which will parse the input file (`*.arff` or `*.csv`) and store each row/data_point as weka instance.

	FastVector: This can store a particular column or corresponding columns of data as a Vector with plain value.

	LinearRegression: This is builtIn LinearRegression Function in Weka API. It allows you to alter different input options by passing different commandline strings:
		Example: silicoRegression.setOptions(weka.core.Utils.splitOptions("-S 2 -R 1.0E-8 -additional-stats -num-decimal-places 4")); 

		-S is the option to choose the reducing dimension method, 0 means no attribute selection, 1 is M5 method and 2 is stepwise method.

		-R is the option to set the value of ridge (You can use this value for ridge regression or stepwise regression)

		-additional-stats allows you to display stats such as R^2 value. I'm not sure why weka didn't set them as default and hide the method to calculate it in their source.

		-num-decimal-places will set all numeric value to be display to maximum 4 decimal places.
	
		(For more information, please read my comment in my code)
	
	*Caution:* You must use "weka.core.Utils.splitOptions()" to parse the command line, otherwise you will encounter errors.


My program will have an attribute selection using greedy stepwise method first and then execute stepwise regression on the rest of the attributes which is the procedure followed in "In silico" Paper. You can set the same procedure and same otions in GUI as well. I commented out the evaluation metric function `calculateIscore()` in this program for now, we can uncomment it in the future.
