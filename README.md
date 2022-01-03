# surfs_up
Module 9

## Overview of Project
This project is an analysis of temperature data in Hawaii. The analysis utilizes a SQLite file, where SQLite is a relational database management system. In Jupyter Notebook, functions to read and interact with the .sqlite are imported from SQLAlchemy. Queries are written to the .sqlite in Jupyter Notebook.
### Purpose
The purpose of this file is to write queries to view all temperature data stored in the .sqlite by month. Because our temperature data spans multiple years, our query filter utilizes an extract function imported from sqlalchemy. For the first deliverable, a query written to the .sqlite is filtered with an extract function, returning Hawaii's temperature data spanning 2010 to 2017 for the month of June. Summary statistics are collected for this dataset. The steps are repeated for the month of December in the second deliverable; the temperature data for this dataset spans 2010 to 2016.
## Results
### Deliverable 1
Extract query & summary statistics https://github.com/stereo-chemistry/surfs_up/blob/ef30fd87a85061a85e88dcee0c173a3562be6316/SurfsUp_Challenge.ipynb

![](resources/June_Statistics.png)

* The query  yields Hawaii's temperature data for the month of **June**
* The query yields a dataset of 1700 points
* The dataset spans 7 years 2010 to 2017
### Deliverable 2
Extract query & summary statistics https://github.com/stereo-chemistry/surfs_up/blob/b32783d19da49431674ef0dea1364f9bbc3bc9b3/SurfsUp_Challenge.ipynb

![](resources/December_Statistics.png)

* The query yields Hawaii's temperature data for the month of **December**
* The query yields a dataset of 1517 points
* The dataset spans 6 years 2010 to 2016
  * .sqlite data begins 01/01/2010 and ends 08/23/2017 
## Summary
