'''
Author: zhangwj
Date: 2024-11-22 16:45:51
LastEditTime: 2024-11-22 17:27:03
LastEditors: zhangwj
Description: 
'''
import pandas as pd

CPI_PATH = '../data/CPILFESL.csv'

def cpi_loader(start_date:str="",end_date:str="",latest_num:int=0):
    """
    - start_date: str; format like %Y-%m-%d
    - end_date: str; format like %Y-%m-%d
    - latest_num: int; the number of latest data required.
    """
    cpi_data = pd.read_csv(CPI_PATH,engine = "pyarrow")
    if not start_date:
        start_date = cpi_data['DATE'].min()
    if not end_date:
        end_date = cpi_data['DATE'].max()
    cpi_data = cpi_data[(cpi_data['DATE']>=start_date) &(cpi_data['DATE']<=end_date) ]
    if latest_num:
        return cpi_data[-latest_num:]
    return cpi_data

if __name__ == "__main__":
    # 
    all_cpi_data = cpi_loader()
    latest_4q_cpi_data = cpi_loader(latest_num = 12)
    # ----------print all cpi data ----------
    # print(all_cpi_data)
    # ----------print the last 4 quarter cpi data ----------
    print(latest_4q_cpi_data)


