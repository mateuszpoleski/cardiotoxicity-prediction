# umwpl-cardiotoxicity-prediction  

## Overview  
Repository for Machine Learning in Drug Design course.
The goal of the project is to predict cardiotoxicity of given substances and to determine features that are most responsible for toxicity.  

### Goals  
As part of the project, I wanted to achieve the following goals:  

- perform a comprehensive data analysis of all fingerprint files.  
- perform regression on IC50 values.  
- perform classification to determine if given substance is toxic or not.  
- test classification models with different IC50 thresholds and compare results.  
- compare results of approaches with regression and classification.  
- figure out which fingerprint type gives the best results and test whether mix of different fingerprint types gives better results.  
- validate how well models behave with limited number of features and test different methods for feature selection.  
- determine if it's possible to find features that are essential for determining cardiotoxicity.  

## Installation  
Simply downloading it with `Download ZIP` option on Github or clone it with `git clone <repository>`.  

After that you need to create new conda environment - this can be done with  

`conda create --name <env> --file environment.yml`  

After this it's possible to run in main folder

`jupyter notebook`  

## Data  
The initial data is in `ready_sets.zip`, as size of `.csv` files was too large for github. You need to extract it into `ready_sets` folder.
After extraction it contains three different fingerprint types:  
* Extended-Connectivity Fingerprint   
* Klekhota-Roth Fingerprint  
* Molecular Access System Fingerprint  

## Project structure   
* [`ready_sets.zip`](/ready_sets.zip) : contains data used to predict cardiotoxicity  
* [`data_analysis.ipynb`](/data_analysis.ipynb) : fingerprint data analysis and visualization  
* [`data_preparation.ipynb`](/data_preparation.ipynb) : all required preparation to tranform `.csv` files into data frames for models.  
* [`regression.ipynb`](/regression.ipynb) : notebook with all regression models and results  
* [`classification.ipynb`](/classification.ipynb) : notebook with all classification models and results  
* [`class_regr_comp.ipynb`](/class_regr_comp.ipynb) : noetbook to perform comparison of best regression model with best classification model.  
* [`png`](/utils.py) : contain code from `data_preparation.ipynb` notebook in format that is easier to import.  
* [`presentations`](/presentations) : both entry and final presentations in `.pdf` format.  
* [`png`](/png) : some `.png` files used for results section in README.  

## Results  
For detailed results, please refer to the respective notebooks and [`final presentation`](/presentations/Final%20-%20UMwPL%20-%20przewidywanie%20kardiotoksyczności%20-%20Mateusz%20Poleski.pdf). Here I will just show most important charts.  

### Regression  

![Regression](/png/regression_res.png)  

Regression results for different fingerprints and different amounts of used features. Results were compared with R^2 score.
The best results were obtained for mixed fingerprints, with R^2 score of about **0.68**.  

### Classification  

![Classification](/png/classification_res.png)  

Classification results for IC50 = 10 000 threshold and different amounts of used features. Results were compared with F1 score and accuracy.
The best model had accuracy and F1 score of about **0.79**.  
