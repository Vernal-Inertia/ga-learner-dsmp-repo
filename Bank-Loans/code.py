# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode

# code starts here
bank = pd.read_csv('/opt/greyatom/kernel-gateway/data/executor/attachments/account/b1/2a7f53f8-19f6-45c7-9d74-560da9338b1a/b69/a340d73b-3d57-4e25-9cfd-074cea5af958/file.csv')
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)

numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)



# code ends here


# --------------
# code starts here
bank.drop(['Loan_ID'], inplace=True, axis=1)
banks = pd.DataFrame(bank)

print(banks.isnull().sum())
bank_mode = banks.mode
banks = banks.fillna(value=bank_mode)
print(banks.isnull().sum())

#code ends here



# --------------
# Code starts here

avg_loan_amount = pd.pivot_table(data = banks, index = ['Gender','Married','Self_Employed'], values = ['LoanAmount'], aggfunc = 'mean')
#banks.dtypes


# --------------
# code starts here
loan_approved_se = banks[(banks['Self_Employed'] == 'Yes') & 
(banks['Loan_Status'] == 'Y')]
loan_approved_nse = banks[(banks['Self_Employed'] == 'No') & 
(banks['Loan_Status'] == 'Y')]

# percentage_se = 614/loan_approved_se
percentage_se = len(loan_approved_se['Self_Employed'] == 'Yes') / 614 * 100
percentage_nse = len(loan_approved_nse['Self_Employed'] == 'No') / 614 * 100



# code ends here


# --------------
# code starts here
loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12)

big_loan_term = len(loan_term[loan_term >= 25])



# code ends here






# --------------
# code starts here

loan_groupby = banks.groupby('Loan_Status')[['ApplicantIncome', 'Credit_History']]

mean_values = loan_groupby.mean()
print(mean_values)

# code ends here


