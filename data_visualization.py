"""
David, Gita, Aynur
Assigned TA: Karen Velderrain-Lopez
Implements the functions required to graph
kindergarten preparedness by student group.
Additionally, tests the statistical significance of
two datasets.
Case-sensitive.
"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

sns.set()


def statistics(df, set_two):
    """
    Finds the statistical significance (P-value and Test-Statistic)
    of two datasets. Uses the files of both
    datasets as parameters.
    """
    filter = df['PreparedForK_Percent'].dropna()
    new_value = set_two['PreparedForK_Percent'].dropna()
    value_set = new_value.mean()
    teststat, pvalue = sm.stats.ztest(filter.to_numpy(), value=value_set)
    print('Test Statistic:', teststat)
    print('p-value:', pvalue)


def all_students(df, category):
    """
    Graphs the percent of students prepared for
    every domain in kindergarten. Takes a file to
    graph preparedness for kindergarten for all students.
    Takes a category to separate the names of graphs with
    different files.
    Case-sensitivity matters.
    """
    outcome_column = df[df['PreparedForK_Percent'].notna()]
    sns.catplot(x='Domain', y='PreparedForK_Percent',
                data=outcome_column, kind='bar')
    plt.xticks(rotation=45)
    plt.title('Preparedness for Kindergarten for All Students')
    plt.savefig(f"C:\\Users\\david\\Downloads\\{category}.png",
                bbox_inches='tight')


def graphing(df, first, second, category, rotate):
    """
    Graphs each student group by the percentage of students prepared.
    The domains of prepration include cognitive, social-emotional,
    and literacy. Case-sensitivity matters.
    """
    groups = ((df["StudentGroup"] == first) | (df["StudentGroup"] == second))
    domains = ((df["Domain"] == "Cognitive") |
               (df["Domain"] == "SocialEmotional") |
               (df["Domain"] == "Literacy"))
    graph = df[groups & domains].copy()
    graph["PreparedForK_Percent"] = graph["PreparedForK_Percent"].dropna()
    sns.catplot(y="PreparedForK_Percent", x="StudentGroup",
                kind="bar", data=graph)
    plt.ylabel("Prepared for Kindergarten")
    plt.xlabel("Student Group")
    plt.xticks(rotation=rotate)
    plt.title("Prepared for Kindergarten by Student Group")
    plt.savefig(f"C:\\Users\\david\\Downloads\\{category}.png",
                bbox_inches='tight')


def graphing_helper(file, add):
    """
    Helps the graphing function. Take a file and an addition
    parameter to separate the file names.Graphs each student group
    by the percentage of students prepared.
    The domains of prepration include cognitive, social-emotional,
    and literacy.
    Case-sensitive.
    """
    graphing(file, "Low-Income", "Non-Low Income", f"income{add}", 0)
    graphing(file, "Migrant", "Non Migrant", f"migrant{add}", 0)
    graphing(file, "Non-English Language Learners",
             "English Language Learners", f"language{add}", -45)
    all_students(file, "students")


def main():
    file_name = "C:\\Users\\david\\Downloads\\KG_Readiness_Decade_Edited.csv"
    edited_name = "C:\\Users\\david\\Downloads\\KG_Readiness_Decade_Edited.csv"
    graphing_helper(pd.read_csv(file_name), "")
    graphing_helper(pd.read_csv(edited_name), "_small")
    statistics(pd.read_csv(edited_name), pd.read_csv(file_name))


if __name__ == '__main__':
    main()
