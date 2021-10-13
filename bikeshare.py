#!/usr/bin/env python
# coding: utf-8

# In[3]:


import time
import calendar
import pandas as pd
import numpy as np
from datetime import datetime


# In[ ]:


print(pd.__version__)


# # Function to parse dates while reading the CSV's

# In[23]:


start = time.time()
parse_datesf = lambda x:pd.datetime.strptime(x, '%m/%d/%Y %H:%M')
chicago = pd.read_csv('./chicago.csv', parse_dates = ['Start Time', 'End Time'], date_parser = parse_datesf)
new_york_city = pd.read_csv('./new_york_city.csv', parse_dates = ['Start Time', 'End Time'], date_parser = parse_datesf)
washington = pd.read_csv('./washington.csv', parse_dates = ['Start Time', 'End Time'], date_parser = parse_datesf)
print("Total time is {}".format(time.time() - start))


# # Adding Trip_Day as Data set column

# In[24]:


chicago['Trip_Day'] = chicago['Start Time'].dt.day_name()
new_york_city['Trip_Day'] = new_york_city['Start Time'].dt.day_name()
washington['Trip_Day'] = washington['Start Time'].dt.day_name()


# # Adding Trip_Month as dataset column to each csv

# In[25]:


chicago['Trip_Month'] = chicago['Start Time'].dt.month_name()
new_york_city['Trip_Month'] = new_york_city['Start Time'].dt.month_name()
washington['Trip_Month'] = washington['Start Time'].dt.month_name()


# In[ ]:


#washington


# In[ ]:



# # Prompts the users to specify their choice of city, month and day 

# In[36]:



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
       
    # TO DO: get user input for month (all, january, february, ... , june)
    while True: 
        city = str(input("Type your city (chicago, new york city or washington):    ")).replace(" ", "").lower().title()
        month = str(input("Type the month (all or January, February...etc):    ")).replace(" ", "").lower().title()
        day  = str(input ("Type the day (all or Sunday, Monday... etc:   ")).replace(" ", "").lower().title()
        data = city + month + day
        if  data.isalpha() == True:
            print("Successfully taken inputs")
            break
        else:
            print("Please enter the correct day, month and from mentioned city names.\n Thank you!")
            pass


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day


# # Loads the users choice and applies filter based on user choice

# In[37]:


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
        
    """
    trip_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    trip_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday','Thursday','Friday','Saturday']
    
    if city == 'Chicago': 
        if month in trip_months:
            if day in trip_days:
                m_filt = (chicago['Trip_Month'] == month) & (chicago['Trip_Day'] == day)
                df = chicago.loc[m_filt]
                
            elif day == 'All':
                df = chicago.loc[chicago['Trip_Month'] == month]
                
            else:
                print("You have entered wrong day!")
                
        elif month == 'All':
            if day in trip_days:
                df = chicago.loc[chicago['Trip_Day'] == day]
                #print("Your chosen Time's information\n\n: {}".format(df))
            elif day == 'All':
                df = chicago
                
            else:
                print("You have entered wrong day!")

        else:
            print("You have entered wrong month!")  
    
    
            
    elif city == 'Newyorkcity':
         if month in trip_months:
            if day in trip_days:
                n_filt = (new_york_city['Trip_Month'] == month) & (new_york_city['Trip_Day'] == day)
                df = new_york_city.loc[n_filt]
                
            elif day == 'All':
                df = new_york_city.loc[new_york_city['Trip_Month'] == month]
                
            else:
                print("You have entered wrong day!")
        
         elif month == 'All':
                if day in trip_days:
                    df = new_york_city.loc[new_york_city['Trip_Day'] == day]
                    
                elif day == 'All':
                    df = new_york_city
                    
                else:
                    print("You have entered wrong day!")
        
         else:
            print("You have entered wrong month!")
            pass
            
    elif city == 'Washington':
        if month in trip_months:
            if day in trip_days:
                w_filt = (washington['Trip_Month'] == month) & (washington['Trip_Day'] == day)
                df = washington.loc[w_filt]
                
            elif day == 'All':
                df = washington.loc[washington['Trip_Month'] == month]
                
            else:
                print("You have entered wrong day!")
        
        elif month == 'All':
            if day in trip_days:
                df = washington.loc[washington['Trip_Day'] == day]
                
            elif day == 'All':
                df = washington
                
            else:
                print("You have entered wrong day!")
        
        else:
            print("You have entered wrong month!") 
        #pass'''
    else: 
        print("Please enter cities from mentioned city names.")   

    
    return df


# # Shows the time statistics according to user choice

# In[28]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    M_c_Month = df['Trip_Month'].value_counts().nlargest(1)
    print("\n The most common Month and tours in it \n {}".format(M_c_Month))

    # TO DO: display the most common day of week
    M_c_Day = df['Trip_Day'].value_counts().nlargest(1)
    print("\n The most common Day and tours in it\n {}".format(M_c_Day))

    # TO DO: display the most common start hour
    M_c_Hour = df['Start Time'].dt.hour.value_counts().nlargest(1)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("\nThe most common Hour and tours in it\n {}".format(M_c_Hour))
    print('-'*40)


# # Show station statistics according to user choice

# In[29]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    M_c_Start_Station = df['Start Station'].value_counts().nlargest(1)
    print("\n The most common Start Station and tours from it \n {}".format(M_c_Start_Station))

    # TO DO: display most commonly used end station
    M_c_End_Station = df['End Station'].value_counts().nlargest(1)
    print("\nThe most common End Station and tours to it\n {}".format(M_c_End_Station))

    # TO DO: display most frequent combination of start station and end station trip
    df_pair = df['Start Station'] + df['End Station']
    M_c_Pair = df_pair.value_counts().nlargest(1)
    print("\nThe most common Station Pairs and tours in it\n {}".format(M_c_Pair))

    print("\nThis took %s seconds." % (time.time() - start_time))
    
    print('-'*40)
    print('-'*40)


# # Show trip duration according to user choice

# In[30]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    mean_duration = df['Trip Duration'].mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("Total travel duration {}\n Average Trip Duration {}".format(total, mean_duration))
    print('-'*40)


# # User demographics

# In[31]:


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print("\n Total User Type\n {}".format(user_type))
    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print("\n Total Gender\n {}".format(gender))
    else:
        print("\n Gender information not found!!\n")
        pass
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest = df['Birth Year'].min()
        print("\n Most elderly user's birth year {}".format(earliest))
        recent   = df['Birth Year'].max()
        c_year_birth = df['Birth Year'].value_counts().nlargest(1)
        print("\n Most youngest user's birth year {}".format(recent))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print("\n Most common birth year {}".format(c_year_birth))
        print('-'*40)
    else:
        print("\n Birth Year information not found!!\n")
        pass


# # Prompting the user for their choice of exploration

# In[38]:


def main():
    while True:
        city, month, day = get_filters()
        global df
        df = load_data(city, month, day)
        m  = df
        x = 0
        y = 5
        print(m.iloc[x:y])
        h = str(input("Want more data? (y/n):  "))

        for i in range(len(m)):
            if h == 'y':
                x +=5
                y +=5
                print("\n\nMore datas \n\n: {}".format(m.iloc[x:y]))
                
                h = str(input("\nWant more data? (y/n):  "))
                continue
            elif h == 'n':
                x = 0
                y = 0
                print("Thank you! Hope you enjoyed the experience!")
                break
            else:
                print("Please enter valid inputs!")
                return
                
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
