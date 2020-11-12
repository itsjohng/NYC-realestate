## **Predicting NYC Real-Estate Sales Volume**
#### **Solo project 1, Metis Data Science Bootcamp**
-----------------
**The goal of this project is to evaluate whether real-estate sales volume in Manhattan can be predicted by using NYC Open data sets.** 

#### **DATA**

Three data sets were gathered and collated for analysis.
1. NYC Rolling Sales Data. This set includes a rolling total of sales for the previous 12 months. Using "way back machine" was able to collate sales from much of the previous decade. This set provided the time scoping for the project. Google maps scraped to provide long/lat values based on addresses provided in this data set.
2. NYC Crime Data. This set includes every crime commited in NYC by date, type, and location (long/lat)
3. NYC Permit Data. This set includes every permit for construction pulled in NYC by date, type, and location (long/lat)

#### **PROCESS**

*WIP. Reframing the problem. The only 'tool in our toolbox' at this point in the curriculum was linear regression. This problem extends well beyond simple linear regression. Investigating time series and poisson (due to count data being used)*

#### **NOTEBOOKS**
* Sales, NYC Crime, and Permit Data Cleaning notebooks clean each data set individually, jettisoning useless columns and dealing with NaN values, etc. where needed
* scraper sits within the Sales Data Cleaning notebook, takes a partially formatted df and uses that to scrape google maps.
* Master DataFrame notebook is where the three notebooks are collated and models are built.
* zonebuilder.py is a legacy and extremely inefficient script built before more intuitive long/lat binning methods were used. 