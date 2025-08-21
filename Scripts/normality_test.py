from scipy.stats import shapiro, levene, skew, kurtosis
import scipy.stats as stats
import seaborn as sns  
import pandas as pd  
import numpy as np 
import math

filepath = "Datasets/Marketing Campaign Data 01.csv"
df = pd.read_csv(filepath)

def bootstrapping(df, column, num_samples=1000, sample_size=30):
    sample_means = []
    for _ in range(num_samples):
        sample = df[column].dropna().sample(n=sample_size, replace=True)
        sample_means.append(sample.mean())
    return sample_means

def shapiro_wilk_test(df, group_col, numeric_cols=None, use_bootstrap=True, num_samples=1000, sample_size=30): 
    if numeric_cols is None:
        numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
        if group_col in numeric_cols:
            numeric_cols.remove(group_col)
    
    results = []
    for group, group_df in df.groupby(group_col):
        for col in numeric_cols:
            if use_bootstrap:
                data = bootstrapping(group_df, col, num_samples=num_samples, sample_size=sample_size)
            else:
                data = group_df[col].dropna()
                
            if len(data) >= 3:  # Shapiro requires at least 3 values
                stat, p_value = shapiro(data)
                interpretation = 'Normal' if p_value > 0.05 else 'Not Normal'
            else:
                stat, p_value, interpretation = None, None, 'Insufficient data'
            
            results.append({
                'Main-Group': group_col,
                'Group': group,
                'Variable': col,
                'Test Statistic': stat,
                'P-Value': p_value,
                'Interpretation': interpretation,
                'Used Bootstrap': use_bootstrap
            })
        
    results_df = pd.DataFrame(results)
    return results_df

result_df = shapiro_wilk_test(df, group_col='Campaigns', use_bootstrap=True)
print(result_df)

def qqplot_groups(data, group_col, value_col):
    groups = data[group_col].unique()
    n_groups = len(groups)
    fig, axes = plt.subplots(1, n_groups, figsize=(5 * n_groups, 5))
    if n_groups == 1:
        axes = [axes]
    
    for ax, group in zip(axes, groups):
        group_data = data[data[group_col] == group][value_col].dropna()
        stats.probplot(group_data, dist="norm", plot=ax)
        ax.set_title(f'Q-Q Plot: {group}')
        ax.grid(linestyle='--', alpha=0.6)
    
    plt.tight_layout()
    plt.show()

qqplot_groups(df, group_col='Campaigns', value_col='Sales (\'000\')')
