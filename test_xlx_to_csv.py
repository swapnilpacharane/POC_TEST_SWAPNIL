import os
import pandas as pd
import logging

def test_1():
    fileName = "Exported Orders - 10.xls"
    sheetName = "Overview"
    excel_file = os.path.join(os.getcwd(), fileName)
    df = pd.read_excel(excel_file,sheet_name=sheetName)
    output = df.iloc[3:,1:].to_csv(index=False, header=False, sep=',')
    logging.info(output)
