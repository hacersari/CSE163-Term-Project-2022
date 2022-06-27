'''
David, Gita, Aynur
Assigned TA: Karen Velderrain-Lopez
Implements the machine learning model (DecisionTreeRegressor), computes the
test accuracy by using %20 of the data as a test.
Used the kindergarten preparedness data to train the model, trained model
predictes  Kindergarten Preparedness in Several Domains based off Language
learning and Socioeconomic Status.
Prints out the mean squared error and r-squared of the model.
'''
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


def decision_tree(df):
    '''
    This function implements the DecisionTreeRegressor from sklearn.
    It uses percentage of preperadness as a label and other columns
    as features. The data is not numeric so hot-coding used to get
    a data that fits into our model.
    '''
    # preparing the data
    features = df.loc[:, df.columns != 'PreparedForK_Percent']
    features = pd.get_dummies(features)
    labels = df['PreparedForK_Percent']
    labels = labels.notna()

    # training the model
    model = DecisionTreeRegressor()
    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.2)
    model.fit(features_train, labels_train)

    # testing the accuracy
    test_predictions = model.predict(features_test)
    print('Test Error (Decision):',
          mean_squared_error(labels_test, test_predictions))
    score = model.score(features_train, labels_train)
    print("R-squared:", score)


def main():
    data = pd.read_csv("/home/edited_report.csv")
    decision_tree(data)


if __name__ == '__main__':
    main()
