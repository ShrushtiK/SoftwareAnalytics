
## Project Description
For the subject of Software Analytics, we have been tasked with developing a project that analyzised metrics involving global collaboration in software products.

Authors: Andra Trandafir, Elena Georgiou, Eduard Sabo, Shrushti . 

## Hypothesis
***Do projects that involve big global collaboration have a lower review speed?***

## Intuition
The hypothesis we have come up with suggests that project that involve international collaboration may be subjected to slower review speeds due to various communication issues: language barriers, different timezones, cultural differences, technology and infrastructure differences, communication channels and tools, work-life balance and burnout regulations etc. 

## Data Extraction
### Repositories Criteria
We have choosen projects that include at least one of the libraries **tensorflow, pytorch or keras** in their descriptions, README file, or codebase. The reason behind the 3 libraries is that they are the most popular libraries used in deep learning. 
### Commit Count
We are filtering repositories based on their commit count falling withing the range of **1000 to 100,000** commits. We are looking for active communities with many contributions. We want to avoid small projects or excessibely large projects that will take a lot of time to analyze.
### Open-source
We are prioritizing open-source projects that have been developed by the community, because this will rise the availability and diversity of projects, transparency and knowledge-sharing.
### Timezone identification
At least 50% of the authors have sth that reveals their timezone (see 3-4 different ways below). Why 50%? We need to find the difference between contributors and collaborators!! WitHub identifies contributors by author email address. This endpoint groups contribution counts by GitHub user, which includes all associated email addresses. To improve performance, only the first 500 author email addresses in the repository link to GitHub users. The rest will appear as anonymous contributors without associated GitHub user information.


## Metrics and Thresholds
1. Timezone Identification
Derived from the organisation that some users might have on their profile (e.g. Microsoft UK)
Time of commit
Country & Bio fields?

2. "Big" Global Collaboration
How do we define 'big' global collaboration? We can get the data and analyse their distribution and then decide (Emeralda)
How do we define big 'global' collaboration? We need to set a threshold regarding how many different time zones we consider global and non-global. Or percentage of different values? How much difference is considered significant (i.e., is 1 our difference significant?)
   
3. Review Speed Definition
 How do we define review speed? Is it time-to-merge? Is it time-to-accept?
![309892999-3ddc89bc-3ade-4ef3-b41e-202ed91af2c2](https://github.com/ShrushtiK/SoftwareAnalytics/assets/64592227/2b4ec453-0c9a-4c08-832e-d508bc0b363f)


## Results
