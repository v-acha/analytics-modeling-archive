# Cleaning Marketplace Shoe Data for Price Modeling

## Overview

This project cleaned and combined women’s and men’s shoe listings to explore product prices and build early regression models. The main work involved standardizing inconsistent product fields, extracting merchant information from URLs, and preparing the listings for analysis.

The combined source files contained **38,432 rows**. After cleaning, the working dataset contained **36,213 rows and 17 columns**.

> **Retrospective note:** The original models used price fields from which the target, `avg_price`, was calculated. One Ridge experiment also appears to use `avg_price` itself as a predictor. The reported model errors are retained as historical results, but they do not establish performance at predicting an unknown shoe price.

## Data

The project used Datafiniti product listings from two files:

- `7003_1.csv` — women’s shoes
- `7004_1.csv` — men’s shoes

The original [women’s](https://data.world/datafiniti/womens-shoe-prices) and [men’s](https://data.world/datafiniti/mens-shoe-prices) data.world pages are retained here as source references. Those pages no longer provide downloads. Some products have multiple price observations, so a row does not necessarily represent a unique shoe.

## Data Cleaning and Feature Engineering

The original workflow included:

- Standardizing brand names, category labels, and date fields.
- Creating `shoe_category` to distinguish women’s and men’s listings.
- Filling missing color, condition, and manufacturer-number values with designated labels.
- Converting `prices.amountMin` and `prices.amountMax` to numeric values, examining outliers, and creating log-transformed price fields.
- Creating `avg_price` as the average of `prices.amountMin` and `prices.amountMax`.
- Standardizing sale-status values and retaining records with usable currency information.
- Cleaning `prices.sourceURLs`, extracting merchant domains into `merchant_source`, and logging URLs that could not be parsed.
- Reviewing the resulting columns and removing records identified as unrelated to shoes.

These preparation choices shaped the final dataset. In particular, filling an unknown condition as “new” is an assumption, and outlier removal changes which price ranges are represented.

## Exploratory Analysis

Pair plots, a correlation heatmap, and PCA plots were used to explore variation in the cleaned listings. The strong correlations among minimum price, maximum price, and average price are expected because `avg_price` was calculated directly from the first two fields. Those correlations should not be interpreted as an independent discovery about shoe pricing.

## Original Modeling Results

The project explored Random Forest, linear regression, and Ridge regression. The values below reproduce the errors reported in the original analysis; the models have **not** been rerun for this README update.

| Model or experiment | Reported MAE |
|---|---:|
| Random Forest with 50 estimators | 0.07153 |
| Linear regression | 7.1357 |
| Ridge using `avg_price` alone | 28.9610 |
| Ridge using `prices.amountMin` and `prices.amountMax` | 0.0159 |
| Ridge using all three price fields | 0.0106 |

The Random Forest feature list included `prices.amountMin` and `prices.amountMax`. The Ridge experiments also used those fields and, in one configuration, `avg_price`. The `avg_price`-only result should be checked against the notebook: if `avg_price` was also the target, that feature description and its reported error do not fit together.

The README does not establish whether every MAE was calculated on the same target scale and test split. For that reason, values such as `0.07153` should **not** be described as an error of seven cents, and the table should not be used to declare Ridge the best shoe-pricing model.

## What the Model Evaluation Can and Cannot Show

For this project, the target was defined as:

```text
avg_price = (prices.amountMin + prices.amountMax) / 2
```

A model given both price fields has access to everything needed to calculate the target. If those prices are available at prediction time, `avg_price` can be calculated directly without machine learning. If they are unavailable, they must be excluded when testing a model intended to estimate price from other product characteristics.

Multiple listings for the same shoe may also affect evaluation if records for one product appear in both training and test sets. A future evaluation would need to check that split, use features available before the price is known, and compare errors on a clearly stated currency and target scale.

## Conclusion

The strongest contribution of this early project is its **data preparation workflow**: combining product files, standardizing inconsistent listing fields, and extracting usable merchant information. The regression experiments document the modeling approaches explored at the time. Their low reported errors should be understood in light of the price-derived features used in the models, rather than as evidence of a ready-to-use pricing system.