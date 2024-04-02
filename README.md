
## Project Description
The influence of international collaboration on code review speed in non-industry repositories outside the industrial sector is a subject that warrants detailed examination. This project aims to shed light on how global cooperation affects code review efficiency in these specialized repositories. <br/>

Authors: Andra Trandafir, Elena Georgiou, Eduard Sabo, Shrushti Kaul. <br/>

Blog Post: [Medium Article](https://medium.com/@software.analytics.group7/global-collaboration-and-review-velocity-5201fdafd46d)

## Overview
While existing research on code review speed predominantly analyzes highly active and popular code bases, our investigation targets Deep Learning repositories specifically. This choice is motivated by the desire to understand the unique dynamics of Deep Learning projects and the effect of international collaboration on code review speed within this domain. Our objective is to uncover insights into the collaborative patterns in non-industry Deep Learning projects across different geographical regions and assess their impact on the code review process. Such insights can promote cross-border collaboration, enhance the global Deep Learning community, and lead to improved code review methodologies that boost productivity and innovation.

## Research Questions
### Research Question 1 (RQ1): 
What is the impact of the number of different time zones from where developers collaborate on the speed of code review?

### Research Question 2 (RQ2): 
How does the variation in time zones from where developers collaborate influence the speed of code review? <br/> <br/>

The key metric for assessing code review speed is the “time-to-merge,” defined as the duration from the opening of a pull request by its author to its eventual merge (and closure).<br/>
Multiple metrics were used to quantify global collaboration:
- count of distinct time zones (RQ1)
- Simpson's Diversity index, which is a measure of diversity which takes into account the number of timeones present, as well as the relative frequence of each timezone (RQ1)
- average pairwise difference in hours between the timezones (RQ2)
 <br/>

The analysis for each research question will be conducted through two approaches:
- Repository-Level Analysis: Calculate an aggregated “time-to-merge” metric for all pull requests within a given repository. This figure is then analyzed in relation to the diverse time zones from which the repository’s collaborators operate.
- Pull Request-Level Analysis: Determine the “time-to-merge” for each individual pull request, and examine this in correlation with the time zones of the participating contributors.

## Data Extraction
Our data extraction pipeline is explained step-by-step under 
```
data_collection.ipynb
```
All the relevant data is in the 'data' directory.

## Analysis of our research questions
Please find our exploration on the two research questions in the files
```
RQ1_analysis.ipynb
```
and
```
RQ2_analysis.ipynb
```
respectively.

All the relevant data is in the 'data_rqs' directory.

## Main findings
### RQ1: What is the impact of the number of different time zones from where developers collaborate on the speed of code review?
Our findings are: 
Repository-Level:
- No significant difference has been found in time-to-merge between repositories with low number of distinct timezones and high number of distinct timezones. 
- With respect to distribution of collaborators' timezones, repositories with a more homogenous spread of timezones exhibit faster time-to-merge values when compared to repositories where the distribution/frequency of timezones is skewed.
Pull Request-Level:
- The lower the number of timezones in a Pull Request, the faster the code review speed.

### RQ2: How does the variation in time zones from where developers collaborate influence the speed of code review? 
Our findings are: 
Repository-Level:
- Repositories with lower average timezone difference have lower time-to-merge than repositories with higher average timezone difference.
Pull Request-Level:
- Based of of our filtered data, around half of the pull requests had participants from the same timezone. We found that PRs with participants from the same timezone display a faster time-to-merge metric than participants with timezone difference greater than 0.

## Dependencies
Before running the notebooks please ensure the following commands are run
```
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```
