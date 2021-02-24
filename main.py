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

    #Replace all 'na' value to 0
    dataframe = dataframe.replace([' na '],0)

    #Call function
    sortCountry(dataframe)
 
#########################################################################
#CLASS Branch: End of Code
#########################################################################

#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def sortCountry(dataframe):
  #Import matplotlib.pyplot as Pie
  import matplotlib.pyplot as Pie

  #Call variables to sort dataframe
  new_df = dataframe
  sorted_df = new_df

  #Check to see if user input is 1, then convert dataframe to match the Europe region
  if region_input == 1:
    #Filter the data based on Year and Country
    new_df = dataframe.loc[(dataframe['Year'] >= year_start) & (dataframe['Year'] <= year_end), ['Year','Month', ' United Kingdom ', ' Germany ',' France ', ' Italy ', ' Netherlands ', ' Greece ', ' Belgium & Luxembourg ', ' Switzerland ', ' Austria ']]

    #sort the country again, this time without month and year
    sorted_df = new_df.drop(['Year','Month'],axis=1)

    #Convert object column Greece to int
    sorted_df[' Greece '] = sorted_df[' Greece '].astype(int)
    #Convert object column Austria to int
    sorted_df[' Austria '] = sorted_df[' Austria '].astype(int)
    #Convert object column Belguim & Luxembourg to int
    sorted_df[' Belgium & Luxembourg '] = sorted_df[' Belgium & Luxembourg '].astype(int)

  #Check to see if user input is 2, then convert dataframe to match the SEA region
  elif region_input == 2:
      #Filter the data based on Year and Country
      new_df = dataframe.loc[(dataframe['Year'] >= year_start) & (dataframe['Year'] <= year_end), ['Year', 'Month',' Brunei Darussalam ' , ' Indonesia ' , ' Malaysia ' , ' Philippines ' , ' Thailand ' , ' Viet Nam ' , ' Myanmar ' ]]
      #sort SEA country, this time without month and year
      sorted_df = new_df.drop(['Year','Month'],axis=1)
      #Convert object column Brunei to int
      sorted_df[' Brunei Darussalam '] = sorted_df[' Brunei Darussalam '].astype(int)
      #Convert object column Indonesia to int
      sorted_df[' Indonesia '] = sorted_df[' Indonesia '].astype(int)
      #Convert object column Malaysia to int
      sorted_df[' Malaysia '] = sorted_df[' Malaysia '].astype(int)
      #Convert object column Philippines to int
      sorted_df[' Philippines '] = sorted_df[' Philippines '].astype(int)
      #Convert object column Thailand to int
      sorted_df[' Thailand '] = sorted_df[' Thailand '].astype(int)
      #Convert object column Viet Nam to int
      sorted_df[' Viet Nam '] = sorted_df[' Viet Nam '].astype(int)
      #Convert object column Myanmar to int
      sorted_df[' Myanmar '] = sorted_df[' Myanmar '].astype(int)

  #Check to see if user input is 1, then convert dataframe to match the Asia-Pacific region
  elif region_input == 3:
      #Filter the data based on Year and Country
      new_df = dataframe.loc[(dataframe['Year'] >= year_start) & (dataframe['Year'] <= year_end), ['Year', 'Month',' Japan ' , ' Indonesia ' , ' Malaysia ' , ' Philippines ' , ' Thailand ' , ' Viet Nam ' , ' China ' ]]
      #sort Asia-Pacific country, this time without month and year
      sorted_df = new_df.drop(['Year','Month'],axis=1)
      #Convert object column Japan to int
      sorted_df[' Japan '] = sorted_df[' Japan '].astype(int)
      #Convert object column Indonesia to int
      sorted_df[' Indonesia '] = sorted_df[' Indonesia '].astype(int)
      #Convert object column Malaysia to int
      sorted_df[' Malaysia '] = sorted_df[' Malaysia '].astype(int)
      #Convert object column Philippines to int
      sorted_df[' Philippines '] = sorted_df[' Philippines '].astype(int)
      #Convert object column Thailand to int
      sorted_df[' Thailand '] = sorted_df[' Thailand '].astype(int)
      #Convert object column Viet Nam to int
      sorted_df[' Viet Nam '] = sorted_df[' Viet Nam '].astype(int)
      #Convert object column China to int
      sorted_df[' China '] = sorted_df[' China '].astype(int)

  #print number of rows in dataframe
  print("There are " + str(len(new_df)) + " data rows read. \n")

  #display dataframe (rows and columns)
  print("The following dataframe are read as follows: \n")
  print(new_df)

  #Add the total number of visitors together
  total_df = sorted_df.sum()

  #Sort the values from descending order
  sort_df = total_df.sort_values(ascending=False)

  #Check to see if user input is 1, then show the Top 3 countries for Europe
  if region_input == 1:

    #Print the Top 3 countries for Europe
    print('\n'+'The top 3 countries that visited Singapore from Europe are:')
    print(sort_df.head(3))
    #Pie chart variable for Europe
    Country = ['United Kingdom', 'Germany', 'France', ' Italy ', ' Netherlands ', ' Greece ', ' Belgium & Luxembourg ', ' Switzerland ', ' Austria ']
    Visitors = [4569048, 1760776, 823145, 396964, 729330, 130491, 217463, 526466, 172926]
    #Call Pie chart
    Pie.pie(Visitors,
        labels=Country,
        startangle=90,
        shadow=True,
        explode=(0.2, 0, 0, 0, 0, 0, 0, 0, 0),
        autopct='%1.2f%%')

  #Check to see if user input is 2, then show the Top 3 countries for SEA
  elif region_input == 2:
    #Print the Top 3 countries for SEA
    print('\n'+'The top 3 countries that visited Singapore from SEA are:')
    print(sort_df.head(3))
    #Pie chart variable for SEA
    Country = ['Brunei Darussalam' ,' Indonesia' , 'Malaysia' , 'Philippines' , 'Thailand' , ' Viet Nam' , 'Myanmar']
    Visitors = [601772, 15288142, 6292852, 2323026, 2961107, 667954, 267938]
    #Call Pie chart
    Pie.pie(Visitors,
        labels=Country,
        startangle=90,
        shadow=True,
        explode=(0.2, 0, 0, 0, 0, 0, 0),
        autopct='%1.2f%%')

  #Check to see if user input is 1, then show the Top 3 countries for Asia-Pacific
  elif region_input == 3:
    #Print the Top 3 countries for Asia-Pacific
    print('\n'+'The top 3 countries that visited Singapore from Asia-Pacific are:')
    print(sort_df.head(3))
    #Pie chart variable for Asia-Pacific
    Country = ['Japan' ,' Indonesia' , 'Malaysia' , 'Philippines' , 'Thailand' , ' Viet Nam' , 'China']
    Visitors = [8595057, 15288142, 6292852, 2323026, 2961107, 667954, 6073384]
    #Call Pie chart
    Pie.pie(Visitors,
        labels=Country,
        startangle=90,
        shadow=True,
        explode=(0.2, 0, 0, 0, 0, 0, 0),
        autopct='%1.2f%%')


  #Prompt user to close the Pie chart
  print('######################################')
  print("CLOSE PIE CHART TO CONTINUE.")
  print('######################################')
  #Display Pie chart Legend
  Pie.legend(loc="upper left")
  #Display Pie chart
  Pie.show()

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
  #Call variable to show Europe's top 3 country on startup
  region_input = 1
  year_start = 1996
  year_end = 2006
  #perform data analysis on specific excel (CSV) file
  DataAnalysis()

  #PROJECT PT 2 USER INPUT
  #Prompt user to enter region name
  #After calling class DataAnalysis, loop.
  while True:
   #Print user input prompt
   print('\n'+'######################################')
   print('USER REGION INPUT')
   print('######################################')
   print('1) Europe')
   print('2) South East Asia')
   print('3) Asia-Pacific')
   
   #If the user enters incorrect input, loop.
   while True:
     #User input using 'try'+'except' for non-int error checking, prompt user to enter 1 to 3
     try:
       region_input = int(input('Please enter a region number from 1 to 3:'))
     except:
        print('ERROR')
        print('Please enter a valid integer number')
     #If user entered a int, check if its 1 to 3, else loop and prompt them to enter correct range. If its valid, break the region input loop.
     else:
       if region_input == 1:
         break
       elif region_input == 2:
         break
       elif region_input == 3:
         break
       elif (region_input > 3) or (region_input < 1):
         print('ERROR')
         print('Please enter within region number range from 1 to 3')

   #Once the region input is valid, start another loop, this time for year start input. If its valid, break the year start input loop.
   while True:
      try:
        year_start = int(input('Enter the year start range from 1978 to 2017: '))
      except:
        print('ERROR')
        print('Please enter a valid integer number')
      else:
        if (year_start >= 1978) and (year_start <= 2017):
           break
        elif (year_start < 1978) or (year_start > 2017):
          print('ERROR')
          print('Please enter within year range 1978 to 2017')
          
   #Once the year start input is valid, start another loop, this time for year end input. If its valid, break the year end input loop
   while True:
     try:
       year_end = int(input('Enter the year end range: '))
     except:
       print('ERROR')
       print('Please enter a valid integer number')
     else:
       if (year_end < 1978) or (year_end > 2017):
         print('ERROR')
         print('Please enter within year range 1978 to 2017')
       elif (year_end >= year_start):
         break
      
  
   #Call class DataAnalysis and show the region based on user input
   DataAnalysis()
      
#########################################################################
#Main Branch: End of Code
#########################################################################