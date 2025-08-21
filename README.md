<h1 align='center'>Marketing Campaigns A/B Testing | Fashion Retail Case Study</h1>

This project uses A/B testing techniques in Python to determine which marketing campaign is most effective in driving product sales. The analysis evaluates and compares the impact of three different promotional strategies launched across randomly selected outlets of a fashion retail company.

## Problem Context

A fashion retail company is preparing to launch a new product as part of its apparel catalog expansion. However, the management is uncertain about which of the three proposed marketing campaigns would generate the highest product sales. To make an informed decision, they conduct an **A/B test** by deploying each campaign variant randomly across selected store outlets and tracking the weekly sales for a one-month period (4 weeks). The ultimate goal is to assess which campaign yields the best sales performance and should be adopted for a full-scale rollout.

## Objectives

The key objectives of this project are:

1. **Compare the effectiveness** of three marketing campaigns (Campaign 1, Campaign 2, Campaign 3) using statistical analysis.
2. **Identify statistically significant differences** in sales using appropriate A/B testing techniques.
3. **Recommend** the most impactful campaign based on data-driven insights.


## Dataset Description

The dataset contains **548 observations** with the following features:

| Column Name        | Description                                                                                           |
| ------------------ | ----------------------------------------------------------------------------------------------------- |
| **OutletID**       | Unique identifier for each store location (total of 137 outlets).                                     |
| **Market Size**    | Categorical variable indicating the outlet’s market size: `Small`, `Medium`, or `Large`.              |
| **Age of Outlets** | Age of the store in years, ranging from 1 to 28.                                                      |
| **Campaigns**      | Categorical variable specifying the campaign type: Control Group, Loyalty Bonus and Product Discount. |
| **Week**           | Indicates the week number (1 to 4) the data point corresponds to.                                     |
| **Sales ('000')**  | Sales revenue in thousands of dollars for the specific campaign, store, and week.                     |



## Methodology

1. **Data Preparation and Exploration**

   * Load and inspect the dataset using `pandas`.
   * Generate summary statistics .
   * Visualize data distribution.

2. **Assumption Testing for Parametric Tests**
   a. **Normality Check**

   * Perform **Shapiro-Wilk test** for each group.
   * Visualize with **Q-Q plots** to confirm normality.
     b. **Homogeneity of Variance**
   * Use **Levene’s test** to test if group variances are equal.

3. **One-Way ANOVA (Analysis of Variance)**

   * Conduct a one-way ANOVA to determine if there are statistically significant differences in mean sales among the three campaigns.

4. **Independent Samples t-Tests (Pairwise Comparison)**

   * Perform **pairwise independent t-tests** between each combination of campaign groups.
   * Identify which specific pairs show significant differences in mean sales.

5. **Post-Hoc Analysis: Tukey’s HSD**

   * Apply **Tukey’s Honest Significant Difference** test to control for multiple comparisons.
   * Identify exactly which campaign pairs are significantly different.

6. **Compact Letter Display (CLD)**

   * Summarize Tukey’s HSD results using **Compact Letter Display**.
   * Assign letters to groups: same letters = not significantly different; different letters = significantly different.

7. **Result Interpretation and Business Insights**

   * Compile a summary table of mean ± SE, group letters, and p-values.
   * Translate findings into business recommendations for selecting the optimal marketing strategy.


## 🛠️ Technologies Used

* **Python** – Core programming language for data analysis and statistical modeling
* **Pandas** – Data manipulation and preprocessing
* **NumPy** – Numerical operations and array handling
* **Matplotlib** – Data visualization
* **Seaborn** – Enhanced statistical plots
* **SciPy (scipy.stats)** – Statistical tests (Shapiro-Wilk, Levene’s test, t-tests)
* **Statsmodels** – ANOVA, Tukey HSD, regression modeling, and statistical summaries
* **Jupyter Notebook** – Interactive development environment for code, visualizations, and documentation
* **Compact Letter Display (custom logic)** – For summarizing post-hoc comparison results in an interpretable format





## Results Summary

* ANOVA and post-hoc tests confirmed statistically significant differences between some campaigns.
* Campaign performance differed significantly, with the **Loyalty Bonus campaign** showing the highest average sales.
* Loyalty Bonus and Control campaigns performed similarly with high sales, while Product Discount significantly underperformed; thus, loyalty rewards sustain or boost sales, whereas discounts can harm brand value and profitability.
* Market size played a supporting role, with **large markets** performing better overall.


## Conclusion

A/B testing revealed that marketing campaign type significantly impacts sales performance. Loyalty Bonus campaigns effectively maintain or increase sales, performing on par with standard control conditions, while Product Discount campaigns tend to reduce sales and may negatively affect brand perception. Additionally, larger markets generally yield better sales outcomes. These findings suggest that businesses should prioritize loyalty-based incentives over discounting strategies to enhance profitability and sustain customer value.

## 👨‍💻 Author


This analysis was performed by **Jabulente**, a passionate and dedicated data analyst with a strong commitment to using data to drive meaningful insights and solutions. For inquiries, collaborations, or further discussions, please feel free to reach out via.  

----

<div align="center">  
    
[![GitHub](https://img.shields.io/badge/GitHub-Jabulente-black?logo=github)](https://github.com/Jabulente)  [![LinkedIn](https://img.shields.io/badge/LinkedIn-Jabulente-blue?logo=linkedin)](https://linkedin.com/in/jabulente-208019349)  [![Email](https://img.shields.io/badge/Email-jabulente@hotmail.com-red?logo=gmail)](mailto:Jabulente@hotmail.com)  

</div>

----
