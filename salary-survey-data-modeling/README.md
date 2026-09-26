# From Raw Salary Surveys to Model-Ready Data

This was my first machine learning project. It began with a practical challenge: combining inconsistent, crowdsourced salary responses into a dataset that could support analysis and modeling. I have kept the original work as part of my project archive, with updated interpretations of what the models did—and did not—show.

## Objective

The primary goal was to analyze salary data collected through surveys shared by TikTok users. I explored salary distributions, bonuses, and relationships involving education, industry, job title, geography, and experience. I then developed exploratory models for salary prediction and gender classification.

## Data Aggregation

The collected files were processed through an SSIS package and SQL Server. Using pandas, I combined the processed CSV files into a single dataset for analysis.

## Data Dictionary

| Variable | Description |
|---|---|
| Age Range | Participant's age group |
| Experience | Years of professional experience |
| Industry | Industry in which the participant works |
| Job Title | Participant's job title |
| Education | Highest reported education level |
| Country | Country of employment |
| Annual Salary | Reported annual salary |
| Annual Bonus | Reported annual bonus, if any |
| Signon Bonus | Reported sign-on bonus, if any |
| Gender | Participant's reported gender |

## Data Cleaning and Preprocessing

The data cleaning phase involved several steps to improve consistency across survey responses:

- **Standardizing columns:** Renamed and corrected columns for categorical consistency.
- **Categorization and grouping:** Created broader categories for education, industry, job title, and gender based on survey responses. Education levels were grouped into broad categories, with similar approaches used for industries and job titles.
- **Web scraping and fuzzy matching:** Scraped lists of standardized industries and job titles from the Bureau of Labor Statistics website. Used fuzzy matching to align survey responses with those lists.
- **Country data standardization:** Corrected and standardized country names.
- **Salary conversion:** Converted salaries into USD using country-specific exchange rates to support analysis on a common currency scale.

## Findings

The exploratory analysis showed variation in reported compensation across countries, experience levels, industries, and job titles. Age and experience were positively associated with earnings in the analyzed data. Education and industry patterns also varied, although this self-selected survey cannot establish what employers prioritize or represent the broader workforce.

## XGBoost Model for Salary Prediction

XGBoost was used to explore relationships between the prepared features and annual salary.

### Reported Holdout Results

- **Mean squared error (MSE):** Approximately 446 million on the holdout test set.
- **R-squared (R²):** 0.602 on the holdout test set.

The reported R² indicates that the model accounted for approximately 60% of the variation in salary **within that test set**, relative to predicting its mean. The holdout MSE was slightly lower than the reported mean cross-validation MSE, but that comparison alone does not establish that the model would perform similarly on a new survey or a different workforce.

MSE is measured in squared target units. If it was calculated on untransformed salaries in USD, the corresponding root mean squared error would be approximately **$21,100**. The target scale should be verified in the notebook before interpreting that figure as a dollar error.

These results showed that the model learned patterns in the analyzed survey. They do not establish that it is suitable for salary estimates outside this dataset, particularly given the survey's self-selected respondents and the choices made during cleaning and currency conversion.

## Classification Model for Gender

The exploratory classifier reported **81% overall accuracy**, but performance differed substantially across classes:

| Class | Precision | Recall |
|---|---:|---:|
| Female | 83% | 97% |
| Male | 61% | 19% |
| Non-Binary | 33% | 6% |


The reported class counts were 37,088 female, 9,320 male, and 81 non-binary respondents. On those full-data counts, a classifier that always predicted “Female” would achieve approximately **79.8% accuracy**. That is close to the reported 81%, although an exact baseline comparison should use the same holdout set as the model.

The low recall for male and non-binary respondents is more informative than the overall accuracy. Class imbalance likely contributed to the result, and the very small number of non-binary observations makes that class especially difficult to evaluate reliably. This experiment is retained as a lesson in evaluating imbalanced classifiers, not as a tool for inferring a person's gender.

## What This Project Taught Me

This project started with data engineering and cleaning rather than a model. Combining files through SSIS and SQL Server, resolving inconsistent categories in pandas, and matching free-text job and industry responses taught me how much modeling depends on the quality and meaning of the underlying data.

The modeling work taught me to look beyond a single performance number. A holdout R² needs context about the sample and target scale. Classification accuracy can conceal very poor performance for smaller groups. Those lessons have shaped how I approach data preparation, evaluation, and interpretation in later projects.

## Limitations

- The respondents were drawn from a crowdsourced social-media survey, so the sample should not be treated as representative of workers generally.
- Grouping categories and fuzzy matching involve judgment and can introduce classification errors.
- Converting salaries to USD creates a common currency but does not account for differences in local purchasing power or cost of living.
- The reported model metrics describe the original analysis and have not been rerun for this retrospective README update.

## Conclusion

The lasting contribution of this first ML project is the process of turning inconsistent salary surveys into structured data for analysis. The original models remain part of that history. Their results are most useful when read alongside the limitations of the sample, the cleaning decisions, and the class-specific evaluation.