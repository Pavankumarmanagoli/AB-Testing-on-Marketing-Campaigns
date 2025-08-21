from scipy.stats import ttest_ind
from itertools import combinations
import pandas as pd  
import numpy as np 

filepath = "Datasets/Marketing Campaign Data 01.csv"
df = pd.read_csv(filepath)

def Independent_ttest(df, group_cols, Variables):
    results = []
    for category in group_cols:
        unique_groups = df[category].unique()
        group_combinations = list(combinations(unique_groups, 2))
        
        for column in Variables:
            for group1, group2 in group_combinations:
                group1_data = df[df[category] == group1][column]
                group2_data = df[df[category] == group2][column]
                t_stat, p_value = ttest_ind(group1_data, group2_data, equal_var=False)
                
                results.append({
                    'Group': category,
                    'Parameter': column,
                    'Group 1': group1,
                    'Group 2': group2,
                    'T-Statistic': t_stat,
                    'P-Value': p_value,
                    'Interpretation': 'Significant' if p_value < 0.05 else 'Not Significant'
                })
        
    results_df = pd.DataFrame(results)
    return results_df


group_col = ['Campaigns', 'Market Size']
Variables = ['Sales (\'000\')']
Results = Independent_ttest(df, group_cols=group_col, Variables=Variables)
print(Results)