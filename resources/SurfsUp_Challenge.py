#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
import numpy as np
import datetime as dt
import pandas as pd
from datetime import datetime

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


# In[2]:


engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station


# In[3]:


# Create our session (link) from Python to the DB
session = Session(engine)


# ## D1: Determine the Summary Statistics for June

# In[4]:


session.query(Measurement.date).first()


# In[5]:


session.query(Measurement.date).order_by(Measurement.date.desc()).first()


# In[7]:


# 1. Import the sqlalchemy extract function.
from sqlalchemy import extract


# 2. Write a query that filters the Measurement table to retrieve the temperatures for the month of June. 

june_start_date = dt.date(2010, 6, 1)

session.query(Measurement.date, Measurement.tobs).filter(extract('month', Measurement.date) == june_start_date.month).all()


# In[8]:


#  3. Convert the June temperatures to a list.
june_results = session.query(Measurement.date, Measurement.tobs).filter(extract('month', Measurement.date) == june_start_date.month).all()


# In[10]:


# 4. Create a DataFrame from the list of temperatures for the month of June. 
June_temps_df = pd.DataFrame(june_results, columns=['date', 'temperature (F)'])
June_temps_df.head(191)


# In[11]:


# 5. Calculate and print out the summary statistics for the June temperature DataFrame.
June_temps_df.describe()


# ## D2: Determine the Summary Statistics for December

# In[12]:


# 6. Write a query that filters the Measurement table to retrieve the temperatures for the month of December.

december_start_date = dt.date(2010, 12, 1)

session.query(Measurement.date, Measurement.tobs). filter(extract('month', Measurement.date) == december_start_date.month).all()


# In[13]:


# 7. Convert the December temperatures to a list.

december_results = session.query(Measurement.date, Measurement.tobs). filter(extract('month', Measurement.date) == december_start_date.month).all()


# In[15]:


# 8. Create a DataFrame from the list of temperatures for the month of December. 

December_temps_df = pd.DataFrame(december_results, columns=['date', 'temperature (F)'])
December_temps_df


# In[16]:


# 9. Calculate and print out the summary statistics for the Decemeber temperature DataFrame.

December_temps_df.describe()


# In[ ]:




