import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee['salary'].drop_duplicates()
    employee = employee.sort_values(ascending=False)
    column = 'getNthHighestSalary('+str(N)+')'
    if N > len(employee) or N <= 0:
        return pd.DataFrame({column:[None]})
    return pd.DataFrame({column:[employee.iloc[N-1]]})
