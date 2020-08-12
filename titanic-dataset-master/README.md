# titanic-dataset

Requirements
1. Python , jupyter notebook.
2. Numpy, Pandas, seaborn and sklearn library.
3. Dataset(titanic.txt), added in the repository.


This dataset has passenger information who boarded the Titanic along with other information like survival status, Class, Fare, and other variables. 
The unfortunate event which was occurred on 15 April 1912, the Titanic sank after colliding with an iceberg, aboard 2224 peoples. 

This project addresses the following Data Analysis topics:
1. Data Exploration and Preparation
2. Data Representation and Transformation
3. Data Visualization and Presentation 

1. Data Exploration and Preparation
Learn about data:
 Are there missing data?
 Is it categorical? if not, min , max, avg values? if yes, what are the categories?
 distribution of variables
 Duplicate entry
 
2. Data Representation and Transformation
Few Passengers didn't pay for the ticket, so there may be a possibility that they didn't purchase a ticket or it was "complimentary" (ticket No. 112050,112059). After checking sample entries, i found out some of the passengers did get a complimentary ticket. This may also help to analyze whom(Important figure in society) to distribute the promotion ticket. 

Transformation on dataframe:
Droping some of the columns which many not contribute much to our machine learning model such as Name, Ticket, Cabin etc

3. Data Visualization and Presentation 
Age distribution per class.  
Upper-class passenger median Age - 36 years 
Middle-class passenger median Age - 29 years 
Lower- class passenger median Age - 26 years

rest all presentation is on jupyter python file Titanic_work.ipynb

The given dataset has entries of 950 peoples.Translated only 42.5% data we have for analysis.

sklearn is used for the machine learning algorithm( Decision tree) with score around 81.05%.

Reference-
1. Tutorial: Titanic dataset machine learning for Kaggle
https://corpocrat.com/2014/08/29/tutorial-titanic-dataset-machine-learning-for-kaggle/ 
 
2. Titanic data-science solutions
https://www.kaggle.com/startupsci/titanic-data-science-solutions/notebook 
