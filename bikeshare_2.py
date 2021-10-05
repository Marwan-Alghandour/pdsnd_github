import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    while True:
        # user enters the city that he wants to load its csv
        city = input('Would you like to see the data for Chicago, New York City, or Washington?\n').lower()
        # error handler if the user enters a city not in the list (chicago, new york city, washington)
        if city not in CITY_DATA:
            print('Invalid city name.')
            continue
    # TO DO: get user input for month (all, january, february, ... , june)
        # user choose if he want to filter the data according to the month or not (all)
        month = input('Which month? January, February, March, April, May, June, or All?\n').lower()
        # error handler if the user enters a month not in the list (all, january, february, ... , june)
        month_check_list = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
        if month not in month_check_list:
            print('Invalid month option')
            continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        # user choose if he want to filter the data according to the day or not (all)
        day = input('Which day or All days? please write the day name\n').lower()
        # error handler if the user enters a day not in the list (all, monday, tuesday, ... sunday)
        day_check_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
        if day not in day_check_list:
            print('Invalid day option')
            continue
        break
    print('-'*40)
    return city, month, day

def check_input(input):
    """
    Check the user input if it's 'yes' or 'no' to print the first statement or the other statement.
    Args:
        (str) input - the user input to check if it's yes, no, or something else
    Returns:
        bool - if the user input is yes or no
    """
    return (input == 'no' or input == 'yes')


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
    # read data from the required file according to the user input
    df = pd.read_csv(CITY_DATA[city])
    # condition to print the first statement again or not
    exit_condition = True
    # decleartion of the input data and the indices of slicing
    req_data = ''
    first_index = 0
    last_index = 5
    # infinite while lopp 
    while True:
        # condition to see print the first statement or to move on to the next statement
        if exit_condition:
            req_data = input('Would you like to display the first five rows in the data? (answer with yes or no)').lower()
            # if user's input is valid we don't enter this conditional statement again
            if check_input(req_data):
                exit_condition = False
            # if not we print an error statement and continue to enter this conditional statement again
            else:
                print('Invalid input')
                continue
        # if input is valid
        if not check_input(req_data):
            print('Invalid input')
        # if the user requests to see data we slice the first five rows and increment by 5 the indices
        elif req_data == 'yes':
            print(df.iloc[first_index: last_index if last_index < len(df) else len(df) - 1])
            first_index += 5
            last_index += 5
        # if no we break out the loop
        elif req_data == 'no':
            break
        # if want to the see the next five rows and first statement in the lopp won't be printed again as exit_condition is equal to false
        req_data = input('Want the next five rows? (answer with yes or no)').lower()
            
         
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #df['month'] = df['Start Time'].dt.month_name() # for check purpose
    #df['day'] = df['Start Time'].dt.weekday_name   # for check purpose
    # filters the data according to the user choice
    if month != 'all':
        df = df.loc[df['Start Time'].dt.month_name() == month.title()]
    if day != 'all':
        df = df.loc[df['Start Time'].dt.weekday_name == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month:', df['Start Time'].dt.month_name().value_counts().idxmax())

    # TO DO: display the most common day of week
    print('The most common day of week:', df['Start Time'].dt.weekday_name.value_counts().idxmax())

    # TO DO: display the most common start hour
    print('The most common start hour:', df['Start Time'].dt.hour.value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station:', df['Start Station'].value_counts().idxmax())

    # TO DO: display most commonly used end station
    print('The most commonly used end station:', df['End Station'].value_counts().idxmax())

    # TO DO: display most frequent combination of start station and end station trip
    print('The most frequent combination of start station and end station trip: (' + df['Start Station'].str.cat(df['End Station'], sep = ', ' ).value_counts().idxmax() + ')')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['End Time'] = pd.to_datetime(df['End Time'])
    # calculate the trip duration
    df['Trip Duration'] = df['End Time'] - df['Start Time']
    print('Total travel time:', df['Trip Duration'].dt.total_seconds().sum(), 'seconds')

    # TO DO: display mean travel time
    print('Average travel time:', df['Trip Duration'].dt.total_seconds().mean(), 'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # get each user type count and put it in a dictionary
    dict_user_type = dict(df['User Type'].value_counts())
    # pretty printing
    print('The count of each user type: (', end = '')
    count = 0
    for key, value in dict_user_type.items():
        count += 1
        print('{}: {}'.format(key, value), end =', ' if count < len(dict_user_type) else ')\n')

    # TO DO: Display counts of gender
    # get each gender count and put it in a dictionary
    dict_gender = dict(df['Gender'].value_counts())
    # pretty printing
    print('The count of each gender: (', end = '')
    for key, value in dict_gender.items():
        print('{}: {}'.format(key, value), end =', ')
    # printing number of Nan in the gender column as unspecified
    print('Unspecified:', df['Gender'].isnull().sum(), end =')\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    print('The earliest year of birth:', df['Birth Year'].min())
    print('The most recent year of birth:', df['Birth Year'].max())
    print('The most common year of birth:', df['Birth Year'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters() # 'chicago', 'all', 'all' # instead of writing them everytime I test the program
        df = load_data(city, month, day)
        #print(df.info()) # checking columns names and its count
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
