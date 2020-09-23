import math

# Function to compute sum. You cant use Python functions
def summation(first_list):
    # sum Logic
    summation_value = 0
    for item in first_list:
        summation_value+=item
    return summation_value

def sorting(first_list):
    sorted_list = first_list[:]
    for i in range(1,len(sorted_list)):
        plug = sorted_list[i]
        j = i-1
        while  j>=0 and sorted_list[j]>plug:
            sorted_list[j+1]=sorted_list[j]
            j-=1
        sorted_list[j+1]=plug
    return sorted_list

# Function to compute mean
def mean(first_list):
    # Validation
    if len(first_list) == 0:
        return 0
    if isinstance(first_list,tuple) != False:
        return 0
    for item in first_list:
        if isinstance(item,str):
            return 0
    # Logic
    mean_value = float("{:.3f}".format(summation(first_list)/len(first_list)))
    return mean_value

# Function to compute median. You cant use Python functions
def median(first_list):
    # Validation
    n = len(first_list)
    if n == 0:
        return 0
    if isinstance(first_list,tuple) != False:
        return 0
    for item in first_list:
        if isinstance(item,str):
            return 0
    # Logic  
    sorted_list = sorting(first_list)
    median_value = 0
    if n % 2 == 0 :
        mid = n/2
        if n == 2:
            median_value = (sorted_list[0]+sorted_list[1])/2
        else:
            median_value =  (sorted_list[mid]+sorted_list[mid+1])/2
    else :
        median_value = sorted_list[int(n/2)]
    median_value = float("{:.3f}".format(median_value))
    return median_value

# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    # Standard deviation Logic
        # Validation
    n = len(first_list)
    if n == 0:
        return 0
    if isinstance(first_list,tuple) != False:
        return 0
    for item in first_list:
        if isinstance(item,str):
            return 0
    # Logic
    list_mean = mean(first_list)
    temp = first_list[:]

    for i in range(0,len(first_list)):
        temp[i] = (first_list[i]-list_mean)*(first_list[i]-list_mean)
    
    sq_sum = summation(temp)

    standard_deviation_value = float("{:.3f}".format(math.sqrt(sq_sum/n)))
    return standard_deviation_value

# Function to compute variance. You cant use Python functions
def variance(first_list):
    # variance Logic
    list_variance = standard_deviation(first_list)
    variance_value = float("{:.3f}".format(list_variance*list_variance))
    return variance_value

# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    # RMSE Logic
    # validation 
    n = len(first_list)
    if n == 0:
        return 0
    if isinstance(first_list,tuple) != False or isinstance(second_list,tuple) != False :
        return 0
    if len(first_list) != len(second_list):
        return 0
    for i in range(0,n):
        if isinstance(first_list[i],str) | isinstance(second_list[i],str):
            return 0
    
    # logic
    temp = first_list[:]
    for i in range(0,len(first_list)):
        temp[i] = (first_list[i]-second_list[i])*(first_list[i]-second_list[i])
    temp_sum = summation(temp)
    rmse_value = float("{:.3f}".format(math.sqrt(temp_sum/n)))
    return rmse_value

# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    # mse Logic
    mse_value = float("{:.3f}".format(rmse(first_list,second_list)*rmse(first_list,second_list)))
    return mse_value

# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    # mae Logic
    # validation
    n = len(first_list)
    if n == 0:
        return 0
    if isinstance(first_list,tuple) != False or isinstance(second_list,tuple) != False :
        return 0
    if len(first_list) != len(second_list):
        return 0
    for i in range(0,n):
        if isinstance(first_list[i],str) | isinstance(second_list[i],str):
            return 0
    
    # logic
    temp = first_list[:]
    for i in range(0,len(first_list)):
        temp[i] = abs(first_list[i]-second_list[i])
    temp_sum = summation(temp)
    mae_value = float("{:.3f}".format(temp_sum/len(first_list)))
    return mae_value

# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    # nse Logic
    # validation
    n = len(first_list)
    if n == 0:
        return 0
    if isinstance(first_list,tuple) != False or isinstance(second_list,tuple) != False :
        return 0
    if len(first_list) != len(second_list):
        return 0
    for i in range(0,n):
        if isinstance(first_list[i],str) | isinstance(second_list[i],str):
            return 0
    
    first_mean = mean(first_list)
    numerator = first_list[:]
    denominator = first_list[:]

    for i in range(0,len(first_list)):
        numerator[i] = (first_list[i]-second_list[i])*(first_list[i]-second_list[i])
        denominator[i] = (first_list[i]-first_mean)*(first_list[i]-first_mean)
    sum_num = summation(numerator)
    sum_den = summation(denominator)

    nse_value = float("{:.3f}".format(1 - (sum_num/sum_den)))
    return nse_value