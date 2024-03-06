# Hypothesis:
Do projects that involve big global collaboration have a lower review speed?

**Intuition behind it:** Due to lack of communication (due to language barriers) and differences in timezones, the review speed might be slower

# Data extraction:
## Repositories criteria: <sub> https://docs.github.com/en/rest/search/search?apiVersion=2022-11-28</sub>
- **DL projects (include tensorflow AND pytorch AND keras)**
  We have choosen projects that include at least one of the libraries in their descriptions, README file, or codebase.
  The reason behind the 3 libraries is that they are the most popular libraries used in deep learning.
  ***Emeralda confirmed that these libraries are okay.
  Recommends to find a reason behind this choice.***
- **Have 1000 to 100,000 commits.**
  We are filtering repositories based on their commit count falling withing this range. We are looking for active communities with many contributions. We want to avoid small projects or excessibely large projects that will take a lot of time to analyze.
  ***Range is fine. Again, recommends explaining why we chose this range.***
- **Are non-industry**:
We are prioritizing open-source projects that have been developed by the community, because this will rise the availability and diversity of projects, transparency and knowledge-sharing.
***Open source. Confirmed.***
- **At least 50% of the authors have sth that reveals their timezone** (see 3-4 different ways below). Why 50%? We need to find the difference between contributors and collaborators!!
<sub> WitHub identifies contributors by author email address. This endpoint groups contribution counts by GitHub user, which includes all associated email addresses. To improve performance, **only the first 500 author email addresses in the repository link to GitHub users**. The rest will appear as anonymous contributors without associated GitHub user information.</sub>

## Metrics & Thresholds:
- **Timezone:** Three ways to do this:
1. Timezone
2. Derived from the organisation that some users might have on their profile (e.g. Microsoft UK)
3. Time of commit (Emeralda's idea - sounds questionable to me - discuss it)
4. [Country & Bio fields] - might not be representative, but we can have it as an option
- **How do we define 'big' global collaboration?**
We can get the data and analyse their distribution and then decide (Emeralda)
- **How do we define big 'global' collaboration?** We need to set a threshold regarding how many different time zones we consider global and non-global. Or percentage of different values? How much difference is considered significant (i.e., is 1 our difference significant?)
- **How do we define review speed?** Is it time-to-merge? Is it time-to-accept?![image](https://github.com/ShrushtiK/SoftwareAnalytics/assets/67713265/3ddc89bc-3ade-4ef3-b41e-202ed91af2c2)

## Other ideas:
- filter by language (language_url field in API)
- use topics (repositories have tags, which we can use e.g. to identify open-source)
- stars (popular repositories)

## Other points:
- Some people work remotely, so the organisation field might not be representative. But we believe that they will be working for the hours of the organisation
