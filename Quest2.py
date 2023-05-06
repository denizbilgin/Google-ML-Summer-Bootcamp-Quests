'''
Buradaki görev Python'un core kütüphanelerini kullanarak bir linear regression
modeli oluşturmak olacaktır.
linear_regression adındaki fonksiyonun X (features) ve y (targets) listelerini
parametre olarak almalıdır.
Fonksiyonunuz, tahmin edilen ve gerçek hedef değerler arasındaki 'Sum of Squared Errors'
(SSE) toplamını en aza indiren slope (m) ve intercept (b) döndürmelidir.

Bu modeli uygularken şu adımları takip etmelisiniz:
- Calculate the mean of X and y using a for loop
- Calculate the variance of X using a for loop
- Calculate the covariance between X and y using a for loop
- Calculate the slope m using the formula: m = cov(X, y) / var(X)
- Calculate the intercept b using the formula: b = mean(y) - m * mean(X)


Ayrıca küçük bir test için burada birkaç kod da bulabilirsin.

X = [1, 2, 3, 4, 5]
y = [2.1, 3.9, 6.2, 8.1, 9.8]
m, b = linear_regression(X, y)
print(f"Slope (m): {m:.2f}")
print(f"Intercept (b): {b:.2f}")

OUTPUT:
Slope (m): 1.98
Intercept (b): 0.12
'''

# Do not import any additional libraries
import math
import os
import random
import re
import sys

def mean(values):
    """
    Calculate the mean of a list of values.

    Parameters:
    values (list): A list of numeric values.

    Returns:
    float: The mean value.
    """
    # YOUR CODE HERE
    total = 0
    for num in values:
        total += num
    result = total / len(values)
    return result

def variance(values):
    """
    Calculate the variance of a list of values.

    Parameters:
    values (list): A list of numeric values.

    Returns:
    float: The variance value.
    """
    # YOUR CODE HERE
    mean_of_values = mean(values)

    # Calculating variance
    vari = 0
    for num in values:
        vari += (num - mean_of_values)**2
    return vari / len(values)

def covariance(x_values, y_values):
    """
    Calculate the covariance between two lists of values.

    Parameters:
    x_values (list): A list of numeric values.
    y_values (list): A list of numeric values.

    Returns:
    float: The covariance value.
    """
    # YOUR CODE HERE

    # Get means
    mean_x = mean(x_values)
    mean_y = mean(y_values)

    covar = 0
    for i in range(len(x_values)):
        covar += (x_values[i] - mean_x) * (y_values[i] - mean_y)
    return covar / len(x_values)

def linear_regression(X, y):
    """
    Implement a basic linear regression model using Python core libraries.

    Parameters:
    X (list): A list of features.
    y (list): A list of target values.

    Returns:
    float: The slope (m) that minimizes the sum of squared errors.
    float: The intercept (b) that minimizes the sum of squared errors.
    """
    # YOUR CODE HERE

    # Calculating the slope
    m = covariance(X,y) / variance(X)

    # Calculating the intercept
    b = mean(y) - m * mean(X)

    return m, b

if __name__ == '__main__':
    sample_X = [1, 2, 3, 4, 5]
    sample_y = [2.1, 3.9, 6.2, 8.1, 9.8]

    assert round(mean(sample_X), 2) == 3.0
    assert round(mean(sample_y), 2) == 6.02
    print('Median test is succeed')

    assert round(variance(sample_X), 2) == 2.0
    assert round(variance(sample_y), 2) == 7.7
    print('Variance test is succeed')

    assert round(covariance(sample_X, sample_y), 2) == 3.92
    print('Covariance test is succeed')

    assert round(linear_regression(sample_X, sample_y)[0], 2) == 1.96
    assert round(linear_regression(sample_X, sample_y)[1], 2) == 0.14
    print('Linear Regression test is succeed')