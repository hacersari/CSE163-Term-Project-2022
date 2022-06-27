'''
David, Gita, Aynur
Assigned TA: Karen Velderrain-Lopez
Implements the machine learning model (SGD_Regressir), computes the
test accuracy by using %20 of the data as a test.

Used the kindergarten preparedness data to train the model, trained model
predictes  Kindergarten Preparedness in Several Domains based off Language
learning and Socioeconomic Status.
Prints out the mean squared error and r-squared of the model.
'''
import pandas as pd
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline


def sgd_regressor(df):
    '''
    This function implements the SGDRegressor from sklearn. It uses
    percentage of preperadness as a label and other columns as features.
    We used the parameters loss=huber, penalty=elasticNet to make the
    model more dynamic.
    '''
    # Prepare the data
    features = df.loc[:, df.columns != 'PreparedForK_Percent']
    features = pd.get_dummies(features)
    label = df['PreparedForK_Percent']
    label = label.notna()

    # Train the model
    features_train, features_test, label_train, label_test = \
        train_test_split(features, label, test_size=0.2)
    model = make_pipeline(StandardScaler(), SGDRegressor(loss="huber",
                                                         penalty="ElasticNet",
                                                         shuffle=False))
    model.fit(features_train, label_train)

    # Compute test accuracy
    test_predictions = model.predict(features_test)
    test_error = mean_squared_error(label_test, test_predictions)
    print("Mean square error (SGD)", test_error)
    score = model.score(features_train, label_train)
    print("R-squared (SGD):", score)


def main():
    data = pd.read_csv("/home/edited_report.csv")
    sgd_regressor(data)


if __name__ == '__main__':
    main()
