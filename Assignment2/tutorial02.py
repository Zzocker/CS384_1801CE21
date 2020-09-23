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