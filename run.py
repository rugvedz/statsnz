import ipdb
import pandas as pd
from clean import Clean

def run():
    excel_file = pd.ExcelFile('covid_19_data_portal.xlsx')
    data = pd.read_excel(excel_file, 'data')
    metadata = pd.read_excel(excel_file, 'metadata')

    mortgage_data = data[data['ResourceID'] == 'CPFIN3'].reset_index(drop=True)

    bank_data = data[data['ResourceID'] == 'CPFIN13'].reset_index(drop=True)

    cleaner = Clean()
    bank_data_mean = cleaner.aggregate_month(bank_data)
    bank_data_mean.rename(columns = {'Value': 'bank_data_mean'}, inplace= True)

    mortgage_data_mean = cleaner.aggregate_month(mortgage_data)
    mortgage_data_mean.rename(columns = {'Value': 'mortgage_data_mean'}, inplace= True)

    merged = pd.merge(bank_data_mean, mortgage_data_mean, on=['Period'])
    merged['date'] = merged.apply(lambda x : str(x['Period']), axis= 1)

    cleaner.plot_scatter(list(merged['date']), list(merged['bank_data_mean']))

    return

if __name__ == '__main__':
    run()