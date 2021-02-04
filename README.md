# Data Visualization Final Project (Group6)

We created a tool that determines the quality of wines depending on its physiochemical properties: **[VINTLY](https://wine-quality-vintly.herokuapp.com/)**. 

1. Pick a dataset
2. Clean data in jupyter notebook
3. Train the model in jupyter notebook then save the models 
5. Use flask and html to visually render the results on a webpage

note: we could have a live machine learning algo or app to generate results off an upload of a picture. (could use some web scraping to get online info).


Attribute information:
   Input variables (based on physicochemical tests):
   1. Fixed acidity (tartaric acid - g / dm^3)
   2. Volatile acidity (acetic acid - g / dm^3)
   3. Citric acid (g / dm^3)
   4. Residual sugar (g / dm^3)
   5. Chlorides (sodium chloride - g / dm^3
   6. Free sulfur dioxide (mg / dm^3)
   7. Total sulfur dioxide (mg / dm^3)
   8. Density (g / cm^3)
   9. pH
   10. Sulphates (potassium sulphate - g / dm3)
   11. Alcohol (% by volume)
   Output variable (based on sensory data): 
   12 - Quality (score between 0 and 10)

<br /><br />

**Description of Attributes**<br />
1 - Fixed acidity: most acids involved with wine or fixed or nonvolatile (do not evaporate readily)

2 - Volatile acidity: the amount of acetic acid in wine, which at too high of levels can lead to an unpleasant, vinegar taste

3 - Citric acid: found in small quantities, citric acid can add ‘freshness’ and flavor to wines

4 - Residual sugar: the amount of sugar remaining after fermentation stops, it’s rare to find wines with less than 1 gram/liter and wines with greater than 45 grams/liter are considered sweet

5 - Chlorides: the amount of salt in the wine

6 - Free sulfur dioxide: the free form of SO2 exists in equilibrium between molecular SO2 (as a dissolved gas) and bisulfite ion; it prevents microbial growth and the oxidation of wine

7 - Total sulfur dioxide: amount of free and bound forms of S02; in low concentrations, SO2 is mostly undetectable in wine, but at free SO2 concentrations over 50 ppm, SO2 becomes evident in the nose and taste of wine

8 - Density: the density of water is close to that of water depending on the percent alcohol and sugar content

9 - pH: describes how acidic or basic a wine is on a scale from 0 (very acidic) to 14 (very basic); most wines are between 3-4 on the pH scale

10 - Sulphates: a wine additive which can contribute to sulfur dioxide gas (S02) levels, wich acts as an antimicrobial and antioxidant

11 - Alcohol: the percent alcohol content of the wine

Output variable (based on sensory data)<br />
12 - Quality (score between 0 and 10)
