import pandas as pd

def read_data(self):
    print("OPENING DATA INFORMATION")
    df = pd.read_excel ("data\test.xlsx")
    print("TESTING FIRST ROW")
    print(df.iloc[0])

    return df

def analyze_month(self, df):
    print("GETTING MONTH INFORMATION")
    df_month = df[['month']]
    print("TESTING FIRST ROW")
    print(df_month.iloc[0])

    return 0

def analyze_year():
    return 0

def analyze_earnings():
    return 0

def analyze_losses():
    return 0

def analyze_type():
    return 0

def analyze_leisure():
    return 0

def analyze_betting():
    return 0

def analyze_trading():
    return 0

def analyze_work():
    return 0

def analyze_gas():
    return 0

def analyze_extras():
    return 0