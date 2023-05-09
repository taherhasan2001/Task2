import pandas as pd
from functools import reduce
import re as regex


# Read the data from Travel.csv
# data.to_csv("new.csv", index=False)  # index=False ==> the row index is not included in the output file.
# data = pd.read_csv("Features.csv")
# data.to_csv("new.csv", index=False)  # index=False ==> the row index is not included in the output file.
# data = pd.read_csv("new.csv")
# filtered_df = data.filter(items=['Name'],axis=1).loc[(data['Travel'] == 'available')]

def Q1():
    # Q1
    # read the data from the file
    data = pd.read_csv("new.csv")

    # edit into the data
    data.fillna(0, inplace=True)  # its a special method to replace empty cells with 0

    # save the new edit data into 'new.csv'
    data.to_csv("new.csv", index=False)  # index=False ==> the row index is not included in the output file.
    # end Q1


def Q2():
    # Q2

    columns = pd.read_csv('new.csv')
    followers = columns['followers'].squeeze().tolist()

    # Use reduce() to sum the numbers
    total = reduce(lambda x, y: x + y, followers)

    # Print the total
    print(total)
    # end Q2


def Q3():
    # Q3
    data = pd.read_csv('new.csv')
    filtered_df = data.filter(items=['Id'], axis=1).loc[(data['location'] == 'UK')]
    print(filtered_df.to_string(index=False))  # print the ids without 'index row number!'
    print(filtered_df)  # print the ids with 'index row number!'

    # end Q3


def Q4():
    # Q4
    data = pd.read_csv("new.csv")
    counter = data['Tweet'].value_counts().tolist()
    print(f"the number of repeats is stored in this list {counter}")

    spams = reduce(lambda acc, x: acc + x if x != 1 else acc, counter, 0)
    # acc, x arguments the lambda will create them
    # acc + x if x != 1 else acc condition
    # counter, 0 arguments which will be send to reduce() function , counter is the list , 0 for acc

    print(f"number of repeated tweets = [{spams}]")
    # print a list of integers each will show the number of how many time  its repeat
    # 1 then its unique and there is no spam

    # end Q4


def Q5():
    # Q5

    data = pd.read_csv("new.csv")
    filtered_df = data.filter(items=['Id'], axis=1).loc[(data['following'] > 5000)]

    print(filtered_df)
    print(filtered_df.to_string(index=False))  # print the ids without 'index row number!'
    # end Q5


def Q6():
    # Q6
    data = pd.read_csv("new.csv")
    filtered_df = data.filter(items=['Id'], axis=1).loc[data['Tweet'].str.contains('#')]

    print(filtered_df)
    # end Q6


def Q7():
    # Q7
    data = pd.read_csv("new.csv")
    filtered_df = data.filter(items=['Id'], axis=1).loc[
        data['Tweet'].str.contains(r"https?://|www\.", flags=regex.I, regex=True)]

    print(filtered_df.to_string(index=False))  # print the ids without 'index row number!'
    # end Q7
