import logging, time
import pandas as pd
import openpyxl as xl
import pyexcel as p
import logging, os
import json

import requests

def test_4():
    fileName = "Exported Orders - 18.xls"
    sheetName = "Overview"
    excel_file = os.path.join(os.getcwd(), fileName)
    try:
        df = pd.read_excel(excel_file,sheet_name=sheetName)
        output = df.iloc[3:,1:].to_csv(index=False, header=False, sep=',')
        logging.info(output)
    except Exception as e:
        logging.error(f"Error is - {e}")
        pass
