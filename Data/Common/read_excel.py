__author__ = 'Administrator'
# coding=utf-8
import xlrd
from datetime import date,datetime
import time

# path = r'C:\Users\Administrator\Desktop\PCLogin.xls'     #不加r会报 (unicode error)错



def read_excel(path,sheetname):
    ExcelFile= xlrd.open_workbook(path,on_demand=True)
    sheet=ExcelFile.sheet_by_name(sheetname)
    return  sheet


#获取行数
def get_rows(sheet):
    return  sheet.nrows

def get_value(sheet,rows,cols):
    ctype = sheet.cell(rows,cols).ctype
    value = sheet.cell(rows,cols).value
    if ctype == 2 and value % 1 == 0:  # 如果是整形
        value = int(sheet.cell(rows,cols).value)
    else:
        value = sheet.cell(rows,cols).value
    return value







