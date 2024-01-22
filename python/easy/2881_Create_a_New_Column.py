import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.assign(bonus=employees['age'] * 2)

df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]})
print(createBonusColumn(df))