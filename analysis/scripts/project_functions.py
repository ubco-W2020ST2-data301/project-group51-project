import pandas as pd
import numpy as np
import seaborn as sns

def load_and_process(path = "/Users/a123/Desktop/School/UBC_2021Summer/Cosc301/Project/spare.csv"):

    # Method Chain 1 (Initial stage : Load data, sort delimiter, rename columns, drop columns with missing data)

    df1 = (
          pd.read_csv("/Users/a123/Desktop/School/UBC_2021Summer/Cosc301/Project/spare.csv", delimiter=';')
          .rename({"marital":"marriage status"}, {"education":"education level"}, {"job":"occupation"},{"y":"have termed deposit"})
          .dropna()
      )

    # Method Chain 2 (Clean-up stage : Drop other columns that is not needed, fill up missing numerical data and object data, drop rows that doesn't have a termed deposit record)

    df2 = (
          df1
        .df2.drop(['default','default','contact','day','month','duration','campaign','pdays','previous','poutcome'],axis='columns')
        .df3['balance'].fillna(0)
        .df1[['occupation','marriage status','education level','housing','loan','have termed deposit']].fillna("unknown")
        .df5['have termed deposit'].dropna(axis='rows')
        
      )
    
    # Method Chain 3 (Analysis stage 1 : view every attribute in terms of age)
    
    df3 = (
        df2
        .df6.median() #we know 
        .df6.groupby('have termed deposit')['age'].median()
        .df6.groupby('occupation')['age'].median()
        .df6.groupby('marriage status')['age'].median()
        .df6.groupby('education level')['age'].median()
        .df6.groupby('housing')['age'].median()
        .df6.groupby('loan')['age'].median()
      )
    
    # Method Chain 4 (Analysis stage 2 : view every attribute in terms of balance)
    
    df4 = (
        df2
        .df6.median() #we know 
        .df6.groupby('have termed deposit')['balance'].median()
        .df6.groupby('occupation')['balance'].median()
        .df6.groupby('marriage status')['balance'].median()
        .df6.groupby('education level')['balance'].median()
        .df6.groupby('housing')['balance'].median()
        .df6.groupby('loan')['balance'].median()
    )
    
    
    # Method Chain 5 (Visualise stage : visualised the following attributes which have more than 3 entries, except our main attribute 'have termed deposit')
    
    df5 = (
          df2
        .sns.countplot(y='have termed deposit',data=df6)
        .sns.countplot(y='age',data=df6)
        .sns.countplot(y='occupation',data=df6)
        .sns.countplot(y='education level',data=df6)
      )
    
    # Make sure to return the latest dataframe

    return df2