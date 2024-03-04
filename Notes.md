# Hypothesis:
Do projects that involve big global collaboration have a lower review speed?

**Intuition behind it:** Due to lack of communication (due to language barriers) and differences in timezones, the review speed might be slower

# Data extraction:
## Repositories criteria:
- **DL projects (include tensorflow or pytorch or keras)**
  Emeralda confirmed that these libraries are okay.
  Recommends to find a reason behind this choice.
- **Have 1000 to 100,000 commits.** Range is fine. Again, recommends explaining why we chose this range.
- **Are non-industry**: Open source. Confirmed.
- **At least 50% of the authors have sth that tells their timezone** (see 3-4 different ways below). Why 50%?

## Metrics & Thresholds:
- **Timezone:** Three ways to do this:
1. Timezone
2. Derived from the organisation that some users might have on their profile (e.g. Microsoft UK)
3. Time of commit (Emeralda's idea - sounds questionable to me - discuss it)
4. [Country] - might not be representative, but we can have it as an option
- **How do we define 'big' global collaboration?**
We can get the data and analyse their distribution and then decide (Emeralda)
- **How do we define big 'global' collaboration?** We need to set a threshold regarding how many different time zones we consider global and non-global. Or percentage of different values? How much difference is considered significant (i.e., is 1 our difference significant?)
- **How do we define review speed?** Is it time-to-merge? Is it time-to-accept?![image](https://github.com/ShrushtiK/SoftwareAnalytics/assets/67713265/3ddc89bc-3ade-4ef3-b41e-202ed91af2c2)
