import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sort: list[int] = list(sorted(employee['salary'].unique()))

    if len(sort) > 1:
        return pd.DataFrame({'SecondHighestSalary': [sort[-2]]})
    else:
        return pd.DataFrame({'SecondHighestSalary': [None]})
