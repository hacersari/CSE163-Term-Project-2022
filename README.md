# Predicting Kindergarten Readiness of children based on different socio-economic identities of children. 

#### Author(s): David Zoro, Gita Dhungana, and Aynur Sari

## Description:
Washington State has created the “Washington Kindergarten Inventory of Developing Skills (WaKIDS)” assessment tool to assess incoming kindergarten children every school year.
We used the dataset (collected through the WaKIDS assessment done over a period of 7 years) about kindergarten preparedness to see how the social identities of children are related to their kindergarten preparedness in certain skill areas. The dataset contains data about children’s preparedness in six skill areas: social-emotional, physical, language, literacy, cognitive, and mathematics. In certain school districts and in some years, Spanish language and Spanish literacy are added to the list, increasing the total number of skill domains to eight. 


## Dataset: 
We got the dataset about kindergarten preparedness in Washington from Data.Gov. 
#### The title of the report: 
#### Report Card Kindergarten Readiness for 2011-12 to Most Recent Year [link to dataset](https://catalog.data.gov/dataset/report-card-kindergarten-readiness-for-2011-12-to-most-recent-year).
The dataset describes students with different social identities as well as the percentage of students prepared for kindergarten based on certain domains. 


### `[CSV Files]`
The original dataset is in `CSV` format. Since it  is very large, we first removed the columns that we were not using in python in `VSCODE` environment. We retrieved the dataset in May 2022 from the webpage mentioned above. However, we noticed that the dataset is no longer available in the webpage. We tried including the CSV file of the original dataset in our folder, but the file size exceeds the maximum limit allowed by Gradescope. So it couldn't be uploaded.  If you want to see the orginal dataset, let us know, we may have to share it through Google Drive.
The names of the CSV files we have in our submission folder:
Original dataset(also called larger dataset in our report) after editing out the unrelated columns: KG_Readiness_Decade_Edited.csv
Smaller dataset (for the school year 2019-20) after editing out the unrelated columns: edited_report.csv


## Graphing

### `data_visualization.py`(specify the name of the graph for each graph)
This python file is for all the data visualization. There are 4 graphs implemented using
`matplotlib`,`pandas` and `seaborn`. You need to run the program in the terminal by writing
`python data_visualization.py`, then it will save all graphs in the folder. 


## Machine Learning
We used 3 different machine learning models in our project. These are `sklearn.linear_model.LinearRegression`, SGDRegressor` and `DecisionTreeRegressor`.


### `Linear_Regression.py`
 You need to run the program in the terminal by writing `python Linear_Regression.py`.
The model is trained with the kindergarten preparedness percentage label and the features
are the domains and student group types. 

### `SGD_Regressor.py`
 You need to run the program in the terminal by writing `python SGD_Regressor.py`.
The model is trained with the kindergarten preparedness percentage label and the features
are the domains and student group types.

### `Decision_Tree_Regressor.py`

 You need to run the program in the terminal by writing `python Decision_Tree_Regressor.py`.
The model is trained with the kindergarten preparedness percentage label and the features
are the domains and student group types.

## Machine Learning Models Comparing
After you run all the machine learning files, you will be able to compare their mean squared errors and R-squared values to decide which one is the best for our dataset.
