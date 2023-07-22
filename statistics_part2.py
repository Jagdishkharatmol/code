import numpy as np
from scipy.stats import skew

def find_variance(data):
    mean = np.mean(data)
    squared_deviations = [(x - mean) ** 2 for x in data]
    variance = np.mean(squared_deviations)
    return variance

def find_standard_deviation(data):
    variance = find_variance(data)
    std_deviation = np.sqrt(variance)
    return std_deviation

def find_range(data):
    max_value,min_value=max(data),min(data)
    range_value=max_value-min_value
    return range_value



def find_IQR(data):
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr_value=q3-q1
    return iqr_value





data = [23, 25, 30, 32, 35, 37, 40]

variance = find_variance(data)
std_deviation = find_standard_deviation(data)
iqr_value= find_IQR(data)
range_value=find_range(data)

print(f'''
      Variance : {variance},
      Standard deviation : {std_deviation},
      Inter quartile range : {iqr_value},
      Range: {range_value}
      ''')



def find_covariance(data1, data2):
    print('check this out',np.cov(data1, data2))
    covariance = np.cov(data1, data2)[0, 1]
    return covariance

# Example data
data1 = [1, 2]
data2 = [5, 4]

covariance = find_covariance(data1, data2)

print("Covariance:", covariance)




data = [10,56,89,42,15,36,89,25,24,16,89]

skewness = skew(data)

print("Skewness:", skewness)