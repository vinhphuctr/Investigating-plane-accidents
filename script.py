aviation_data = []
aviation_list = []

# open the file, split into line and for each line, split into words
with open('AviationData.txt', 'r') as file:
    for line in file:
        aviation_data.append(line)
        text = line.split('|')
        words = []
        for word in text:
            word = word.strip()
            words.append(word)
        aviation_list.append(words)
        
# seach through aviation_list for LAX94LA336 using linear time algorithm
def linear_search(code):
    lax_code = list()
    for row in aviation_list:
        if code in row:
            lax_code.append(row)
    return lax_code

linear_search = linear_search('LAX94LA336')


# create a hash table
def hash_table(data):
    # clean input and create a list of keys for a hash table
    key_sets = data[0].split('|')
    keys = []
    for key in key_sets:
        key = key.strip()
        keys.append(key)
    
    # get the values for the keys
    values = []
    for index in range(1, len(data)):
        value_sets = data[index].split('|')
        clean_values = []
        for value in value_sets:
            value = value.strip()
            clean_values.append(value)
        values.append(clean_values)
    
    # pair the values to the keys
    aviation_dict_list = [] 
    for y in range(0, len(values)): 
        pairs = {}
        for x in range(0, len(keys)):
            pairs[keys[x]] = values[y][x]
        aviation_dict_list.append(pairs)
    return aviation_dict_list

aviation_dict_list = hash_table(aviation_data)

# return a dictionary containing 'LAX94LA336'
def dict_search(code, dict_list):
    lax_dict = []
    for d in range(0, len(dict_list)):
        for value in dict_list[d].values():
            if code == value:
                lax_dict.append(dict_list[d])
    return lax_dict

dict_search = dict_search('LAX94LA336', aviation_dict_list)


# COUNT HOW MANY ACCIDENTS OCCURED IN EACH STATE
from collections import Counter
def top_states(n):
    states = []
    for x in range(0, len(aviation_dict_list)):
        # for each location in each dictionary, get only the state
            states.append(aviation_dict_list[x]['Location'][-2:])
    states_count = Counter(states)
    return states_count.most_common(n)

# top five states with the most aviation accidents
top_5 = top_states(5)


# FATALITY AND SERIOUS INJURIES BY MONTH
def worst_month_accidents(n, data):
    months = []
    change_months = {"01": "January",
                     "02": "February",
                     "03": "March",
                     "04": "April",
                     "05": "May",
                     "06": "June",
                     "07": "July",
                     "08": "August",
                     "09": "September",
                     "10": "October",
                     "11": "November",
                     "12": "December"
                    }
    for i in range(0, len(data)):
        month = data[i]['Event Date'][0:2]
        try:
            month = change_months[month]
        except KeyError:
            month = data[i]['Event Id'][4:6]
            month = change_months[month]
        if data[i]['Event Date'] != '':
            year = data[i]['Event Date'][-4:]
        else:
            year = data[i]['Event Id'][0:4]
        months.append(month + ' ' + year)
    
    worst_month = Counter(months) 
    return worst_month.most_common(n)

# return a worst 3 months from the records
worst_3 = worst_month_accidents(3, aviation_dict_list)


def most_deadly_months(n, data):
    monthly_injuries = {}
    change_months = {"01": "January",
                     "02": "February",
                     "03": "March",
                     "04": "April",
                     "05": "May",
                     "06": "June",
                     "07": "July",
                     "08": "August",
                     "09": "September",
                     "10": "October",
                     "11": "November",
                     "12": "December"
                    }
    
    for i in range(0, len(data)):
        injuries = 0
        month = data[i]['Event Date'][0:2]
        try:
            month = change_months[month]
        except KeyError:
            month = data[i]['Event Id'][4:6]
            month = change_months[month]
        if data[i]['Event Date'] != '':
            year = data[i]['Event Date'][-4:]
        else:
            year = data[i]['Event Id'][0:4]
        month = month + ' ' + year
        
        fatal = data[i]['Total Fatal Injuries']
        serious = data[i]['Total Serious Injuries']
        if fatal:
            injuries += int(fatal)
        if serious:
            injuries += int(serious)
        
        monthly_injuries[month] = injuries
    injuries_count = Counter(monthly_injuries)  
    return injuries_count.most_common(n)

# return the top 3 deadly months from the records
top_3 = most_deadly_months(3, aviation_dict_list) 


# TOP AIR CARRIERS THAT HAVE THE MOST ACCIDENTS
def air_carriers_acc(n, data):
    air_carriers = []
    for i in range(0, len(data)):
        air_carrier = data[i]['Air Carrier']
        if air_carrier != '':
            air_carriers.append(air_carrier)
    ac_count = Counter(air_carriers)
    return ac_count.most_common(n)

top_4 = air_carriers_acc(4, aviation_dict_list)


# WORST WEATHER CONDITIONS: top percentage of accidents during the weather
def worst_weather(data):
    weathers = []
    for i in range(0, len(data)):
        weather = data[i]['Weather Condition']
        if weather != '':
            weathers.append(weather)
    weather_count = Counter(weathers)
    percentage = [(x, weather_count[x]/len(data)*100) for x in weather_count]
    return sorted(percentage, key=lambda x: x[1], reverse=True) 

worst_weathers = worst_weather(aviation_dict_list)
print(worst_weathers) 