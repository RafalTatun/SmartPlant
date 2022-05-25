import openpyxl
import datetime
import  sys

dataExcel = {}

today = datetime.date.today()
now = datetime.datetime.now()

def givedateexcel():
    # dd/mm/YY
    d1 = today.strftime("%d/%m/%Y")
    # hh/mm
    t1 = now.strftime("%H:%M") 
    
    wb = openpyxl.load_workbook('Dane.xlsx')
    sheet = wb["dane"]
    print(d1, " ", t1)
    sheet['B2'] = d1
    sheet['C2'] = t1
    wb.save('Dane.xlsx')
    
givedateexcel()
