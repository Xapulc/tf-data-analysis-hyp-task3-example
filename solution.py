import pandas as pd
import numpy as np


chat_id = 402739329 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    alpha = 0.06
    stat, p_value = stats.ttest_ind(x, y, alternative='two-sided')
    return (p_value < alpha)
