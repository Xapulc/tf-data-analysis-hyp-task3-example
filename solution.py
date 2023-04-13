import pandas as pd
import numpy as np

from scipy.stats import mannwhitneyu

chat_id = 694905952 # Ваш chat ID, не меняйте название переменной

def solution(*args) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    
    if len(args) == 1:
        x = args[0]
    elif len(args) == 2:
        x = args[0]
        y = args[1] 
        
    
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.03
    return mannwhitney(x, y, alternative = "less").pvalue < alpha # Ваш ответ, True или False
