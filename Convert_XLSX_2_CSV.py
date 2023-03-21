import openpyxl
import csv
import array as arr 

data=[None] * 3
#data[0]="//SGSI2W2221.ap.merckgroup.com/RPA_DEV_SHARE/INDONESIA_PR_PO/CONFIG/INDONESIA_PR_PO_User_Config - Copy.xlsx"
#data[1]="//SGSI2W2221.ap.merckgroup.com/RPA_DEV_SHARE/INDONESIA_PR_PO/CONFIG/INDONESIA_PR_PO_User_Config - Copy.csv"
#data[2]="Holiday"
try:
    def convertFileType(inp):
        ob = csv.writer(open(inp[1],'w', newline = ""))
        data = openpyxl.load_workbook(inp[0])
        wb=data[inp[2]]
        for r in wb.rows:
            row = [a.value for a in r]
            ob.writerow(row)
                
    if __name__ == '__main__':
        convertFileType(data)

except Exception as e:
        print.error('Failed : Error occurred ' + str(e))