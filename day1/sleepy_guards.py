import pandas as pd
import re

def read_input():
    #Read in input file
    input = ("input.txt")
    data = open(input).readlines()

    #Sort data
    data.sort()

    #Initialize variables
    processed_data = []
    status_array = []
    status_dict = {'asleep':'#', 'wakes':'.'}
    guard = None
    guard_status = '.'
    last_update_time = 0
    date = None

    #Process data
    for line in data:
        #Search the current line for data elements
        guard_search = re.search('(#\d+)', line)
        date_search = re.search('\d{4}-(\d{2}-\d{2}) 00', line)
        status_search = re.search('(asleep|wakes)', line)
        status_time = re.search('00:(\d{2})', line)
        #Capture the first guard, or finish current day and capture next guard
        if guard_search:
            if guard is None:
                guard = guard_search.group(1)
            else:
                status_array = status_array + [guard_status for x in range(last_update_time, 60)]
                complete_row = [date, guard] + status_array
                processed_data.append(complete_row)
                status_array = []
                guard_status = '.'
                guard = guard_search.group(1)
                last_update_time = 0
                pass
        #Capture current date
        if date_search:
            date = date_search.group(1)
        #Update the status array
        if status_search:
            new_update_time = int(status_time.group(1))
            status_array = status_array + [guard_status for x in range(last_update_time, new_update_time)]
            guard_status = status_dict[status_search.group(1)]
            last_update_time = new_update_time

    #Add the last row
    status_array = status_array + [guard_status for x in range(last_update_time, 60)]
    complete_row = [date, guard] + status_array
    processed_data.append(complete_row)

    return(processed_data)

def analyze_data(processed_data):
    column_names = ['date', 'guard'] + [format(x, '02d') for x in range(0, 60)]

    #Create DataFrame
    df = pd.DataFrame(processed_data, columns=column_names)
    def sleep_convert(x):
        if x == '#':
            return 1
        else:
            return 0
    #Calculate hours slept per day
    df['minutes_slept'] = df.loc[:, '00':'59'].apply(lambda x: sum(map(sleep_convert, x)), axis=1)

    #Display completed dataframe
    print(df.to_string())

    #Aggregate data to determine sleepiest guard
    aggregated = df.groupby('guard').agg({'minutes_slept': [('total', 'sum'), ('average', 'mean'), ('max', 'max')],'guard':[('days_worked','count')]})

    #Rank guards by total hours slept
    print(aggregated.sort_values(by = ('minutes_slept','total'), ascending = False))

    #Display sleepiest guards based on total, average, and max
    print('Sleepiest guard(s) based on total minutes slept: ', list(aggregated.index.values[aggregated[('minutes_slept','total')] == max(aggregated[('minutes_slept','total')])]))
    print('Sleepiest guard(s) based on average minutes slept: ', list(aggregated.index.values[aggregated[('minutes_slept', 'average')] == max(aggregated[('minutes_slept', 'average')])]))
    print('Sleepiest guard(s) based on max minutes slept: ', list(aggregated.index.values[aggregated[('minutes_slept', 'max')] == max(aggregated[('minutes_slept', 'max')])]))

if __name__ == "__main__":
    processed_data = read_input()
    analyze_data(processed_data)
