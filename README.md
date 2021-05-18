### Census Data Cleaning

These scripts take in data from https://censusindia.gov.in/2011census/C-series/C-13.html and export files which are grouped by age groups (18-44, 45-59, 60+) for total population.
Download the XLS from the link above and export it to CSV. These scripts take the resulting CSV as input.

Usage:

```
./group.sh andhra.csv
```

This will produce `grouped-cleaned-andhra.csv` which will contain rows like the following:

```
state,district,name,age,persons,males,females
28,000,State - ANDHRA PRADESH (28),18-44,37821449,18888656,18932793
28,000,State - ANDHRA PRADESH (28),45-59,11224253,5587755,5636498
28,000,State - ANDHRA PRADESH (28),60+,8278241,3906328,4371913
28,532,District - Adilabad (01),18-44,1178210,587537,590673
28,532,District - Adilabad (01),45-59,329328,163162,166166
28,532,District - Adilabad (01),60+,232385,104595,127790
28,533,District - Nizamabad (02),18-44,1111161,544800,566361
28,533,District - Nizamabad (02),45-59,318293,151934,166359
28,533,District - Nizamabad (02),60+,250743,109115,141628
```