#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse the excel file and lists the top 3 countries that visits Singapore in 10 years.
#Name: <Benedict Ang>
#Group Name: <Mackerel-Tackler>
#Class: <PN2004J>
#Date: <09/02/2021>
#Version: <1.0>
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd
import re
#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################

#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
  def __init__(self):

    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthyVisitors.csv')
    #show specific country dataframe

    df_year = (dataframe['Year'])
    df_month = (dataframe['Month'])

    euro_countr = 'United Kingdom', 'Germany', 'France', 'Italy', 'Netherlands', 'Greece', 'Belgium & Luxembourg', 'Switzerland', 'Austria'
    
    new_df = dataframe.loc[(dataframe['Year'] >= 1996) & (dataframe['Year'] <= 2004) & (dataframe['United Kingdom']) & (dataframe['Germany'])]

    print(new_df)
    

    proceed = input("Proceed?")
    if proceed == "yes":
     sortCountry(dataframe)
    else:
      exit()
#########################################################################
#CLASS Branch: End of Code
#########################################################################

#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def sortCountry(df):

  #print number of rows in dataframe
  print("There are " + str(len(df)) + " data rows read. \n")

  #display dataframe (rows and columns)
  print("The following dataframe are read as follows: \n")
  print(df)

  #display a specific country (Australia) in column #33
  country_label = df.columns[33]
  print("\n\n" + country_label + "was selected.")

  #display a sorted dataframe based on selected country
  print(" The" + country_label + "was sorted in ascending order. \n")
  sorted_df =df.sort_values(country_label,ascending=[1])
  print(sorted_df)

  return
#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':
  
  #Project Title
  print('######################################')
  print('# Data Analysis App - PYTHON Project #')
  print('######################################')

  #perform data analysis on specific excel (CSV) file
  DataAnalysis()

#########################################################################
#Main Branch: End of Code
#########################################################################