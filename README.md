# Marketing Campaign A/B Testing

This repository analyses three promotional strategies for a fashion retail company using classical A/B testing techniques. The aim is to determine which campaign drives the greatest lift in weekly sales and to provide actionable recommendations for future marketing rollouts.

## Problem Context

FashionCo, a national retailer, is exploring different promotional tactics to boost revenue across its store network. To move beyond assumptions and anecdotal evidence, the company ran a four‑week experiment in which 137 outlets were randomly assigned to one of three campaigns:

* **Control Group** – standard marketing spend with no additional incentives.
* **Loyalty Bonus** – targeted rewards to encourage repeat purchases.
* **Product Discount** – price reductions on selected items.

Weekly sales were recorded along with store attributes such as market size and age. Management seeks to understand how each strategy affects revenue and which option should be deployed at scale.

## Project Objective

* Provide a reproducible framework for testing promotional hypotheses using classical A/B testing.
* Evaluate the effectiveness of three marketing campaigns – **Control**, **Loyalty Bonus** and **Product Discount** – on product sales across different market sizes and store ages.
* Quantify whether observed differences in weekly sales are statistically significant and practically meaningful.
* Recommend the most impactful campaign and describe the conditions under which it performs best.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Pavankumarmanagoli/AB-Testing-on-Marketing-Campaigns.git
cd AB-Testing-on-Marketing-Campaigns
```

### 2. Install dependencies

Install the required Python packages. A virtual environment is recommended.

```bash
pip install pandas numpy matplotlib seaborn scipy statsmodels jupyter
```

### 3. Run the analysis

* **Jupyter Notebook**: launch the notebook for an interactive walkthrough of the analysis.

  ```bash
  jupyter notebook 01_AB_Testing_Statistical__Analysis.ipynb
  ```

* **Scripts**: individual statistical tests are implemented as standalone scripts in the `Scripts/` directory.  For example, to run a one‑way ANOVA:

  ```python
  import pandas as pd
  from Scripts.anova import One_way_anova

  data = pd.read_csv("Datasets/marketing_campaign_data.csv")
  results = One_way_anova(data, ["Sales ('000')"], ["Campaigns"])
  print(results)
  ```

## Dataset

The dataset (`Datasets/marketing_campaign_data.csv`) contains 548 records describing weekly sales for randomly selected store outlets.

| Column | Description |
| ------ | ----------- |
| `OutletID` | Unique identifier for each store (137 outlets). |
| `Market Size` | Size of the market: Small, Medium or Large. |
| `Age of Outlets` | Age of the store in years. |
| `Campaigns` | Campaign type: Control Group, Loyalty Bonus or Product Discount. |
| `Week` | Week number (1–4) of the trial. |
| `Sales ('000')` | Sales in thousands of dollars for the given week and campaign. |

## Methodology

1. **Data exploration** – load the dataset, compute summary statistics and visualise distributions.
2. **Assumption checks** – assess normality (Shapiro‑Wilk) and homogeneity of variances (Levene’s test).
3. **One‑way ANOVA** – test whether mean sales differ across campaigns.
4. **Pairwise t‑tests** – compare campaign pairs to identify where differences occur.
5. **Tukey’s HSD** – control for multiple comparisons in post‑hoc analysis.
6. **Compact Letter Display** – summarise Tukey results for easy interpretation.
7. **Business interpretation** – translate statistical findings into marketing recommendations.

## Repository Structure

```
├── Datasets/                     # Raw data files
├── Outputs/                      # Generated figures and tables
├── Scripts/                      # Reusable analysis scripts
└── *.ipynb                       # Jupyter notebooks containing full analysis
```

## Technologies Used

* Python
* pandas
* NumPy
* Matplotlib & Seaborn
* SciPy
* Statsmodels
* Jupyter Notebook

## Results Summary

* ANOVA and post‑hoc tests reveal significant differences among campaigns.
* **Loyalty Bonus** produces the highest average sales and performs on par with the control group.
* **Product Discount** underperforms and may erode brand value, particularly in smaller markets.

## Conclusion

A/B testing confirmed that marketing strategy has a measurable impact on sales.  Loyalty‑based incentives are the most effective, while discounting tends to depress revenue.  The analysis supports deploying the Loyalty Bonus campaign for a wider rollout.


## License
This project is licensed under the [MIT License](LICENSE).
