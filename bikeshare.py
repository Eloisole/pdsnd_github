import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }

months = ("January", "February","March", "April", "May", "June", "All")

weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "All")

def selection(read, data):
    """
    Ask and check the data provided compare with the available_data. Eloi Sole
    Data Citys
    
    Returns:
        string - input data enter by the users
    """
    while True:
        data_entry = input(read).title()
        if data_entry not in data:
            print("Something is not valid. Please enter a valid option:>")
            continue
        else:
           break
      
    return data_entry
    

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    "-------------------------------------------------------------------------------------"
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    city = selection("Enter a city (chicago, new york city, washington):", CITY_DATA.keys())

    validation = selection("Filter the data by Month, Day, Both or not at all (Type \"none\" for no filter)? ", ["Month", "Day", "Both", "None"])
    month = ""
    day = ""
    
    if (validation in ["Month", "Both"]):
        month = selection("Enter a month (January, February,March, April, May, June, All):", months)
    else:
        month = "All"

    if (validation in ["Day", "Both"]):
        day = selection("Enter a day of week (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, All):", weekdays)        
    else:
        day = "All"
        
    print("\n\nOK let's go to explore {} City and filter the data by {}\n".format(city, validation))
    if month != "":
        print("Filter by {} month(s)\n".format(month))
    if day != "":
        print("Filter by {} day(s)\n".format(day))
    if month == "" and day == "":
        print("No filter is applied\n")

    print('-'*40)
    return city, month, day


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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df["Start Time"])
    # extract month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month_name()
    df["Weekday"] = df['Start Time'].dt.day_name()
    df['Start Hour'] = df['Start Time'].dt.hour

    if month != 'All':           
        # filter by month to create the new dataframe
        df = df[df["Month"]==month]

    if day != 'All':
        # filter by day of week to create the new dataframe
         df=df[((df["Weekday"])==day)]

    return df

def time_stats(df):
    
    print('Displaying the statistics on the most frequent times of travel...')
    start_time = time.time()

    # display the most common month
    most_common_month = df['Month'].mode()[0]
    print('Popular travels is: ' + str(most_common_month) + '.')

    # display the most common day of week
    most_common_day = df['Weekday'].mode()[0]
    print('Popular day of the week is: ' + str(most_common_day) + '.')

    # display the most common start hour
    most_common_hour = df['Start Hour'].mode()[0]
    print('Popular start hour is: ' +  str(most_common_hour) + '.')

    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    

    print('Calculating The Most Popular Stations and Trip...')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_start_station = str(df['Start Station'].mode()[0])
    print("Commonly start station is: " + commonly_start_station)

    # TO DO: display most commonly used end station
    commonly_end_station = str(df['End Station'].mode()[0])
    print("Commonly  end station is: " +  commonly_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start-End Combination'] = (df['Start Station'] + ' - ' + df['End Station'])
    most_start_end_combination = str(df['Start-End Combination'].mode()[0])
    
    print("Commonly combination of start station and end station trip is: " + most_start_end_combination)

    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)
   
    
def trip_duration_stats(df):
    

    print('Calculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_travel_time = (str(int(total_travel_time)) +'d '+ str(int(total_travel_time //3600))+ 'h '+ str(int(total_travel_time % 3600//60)) + 'm ' + str(int((total_travel_time % 3600) % 60)) +'s')
    print('Total travel time is : ' + total_travel_time + '.')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_travel_time = (str(int(mean_travel_time//60)) + 'm ' + str(int(mean_travel_time % 60)) + 's')
    print("Mean travel time is : " + mean_travel_time + ".")

    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df):
   

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts().to_string()
    print("Display for user types:")
    print(user_types) 
    # TO DO: Display counts of gender
    if "Gender" in df:
        gender_counts = df['Gender'].value_counts().to_string()
        print("Counts for each gender:")
        print(gender_counts)
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        earliest_birth_year = str(int(df['Birth Year'].min()))
        print("Earliest birth is: " + earliest_birth_year)
        most_recent_birth_year = str(int(df['Birth Year'].max()))
        print("Most recent birth is: " + most_recent_birth_year)
        most_common_birth_year = str(int(df['Birth Year'].mode()[0]))
        print("Most common birth year is: " + most_common_birth_year)
 


    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data(df, num_rows):
    
      
    display = True
    i=0
    len_df = len(df)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.expand_frame_repr', False)

    while display == True:
        answer = input("Do you want to see {} lines of the data? (Yes/No)".format(num_rows))
        if ((answer.lower() == "yes") and (len_df > i)):
            if len_df > (i + num_rows):
                print(df[i:(i + num_rows)])
                i = i + num_rows           
            else:
                print(df[i:len_df])
                display = False
                
        elif (answer.lower() == "no") or (len_df  <= i):
            display = False
            
        else:
            print("Invalid input. Please enter a valid input...")    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        raw_data(df, 5)

        restart = input('Would you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	    main()
