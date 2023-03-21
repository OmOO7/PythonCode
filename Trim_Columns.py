#   
#   Excel Process
#   Trim_Columns
#   Date of Modified    : 04-Aug-2022
#   Modified            : Karthik Ravi (karthik.ravi@external.merckgroup.com)
#   

import pandas as pd
import os
import openpyxl

data=[None] * 3
#data[0]="PR_ListC.xlsx" # file name
#data[1]="D:\\" #should end with \
#data[2]="PR_ListC" # sheet name


try:
    def trim_columns(inp):
        Input_file_name                        =   inp[0] #= "Vendor List.xlsx"
        Input_file_path                        =   inp[1] #= "\\idja1vfiler01.ap.merckgroup.com\Groups\FI\SC\SCM_Placing Order\DEV\REFERENCE\"
        Sheet_name                             =   inp[2] #= "VENDOR"
        
        if (".xlsx" in Input_file_name):
            if Sheet_name != '':
                try:
                    Input_file_name_with_path          =   Input_file_path + Input_file_name
                    file_exists                        =   os.path.exists(Input_file_name_with_path)
                    
                    if file_exists == True:
                        
                        input_df_1                  =   pd.read_excel(Input_file_name_with_path,sheet_name=Sheet_name,engine="openpyxl")
                        input_df_1.columns          =   input_df_1.columns.str.strip()
                        
                        with pd.ExcelWriter(Input_file_name_with_path, mode="a", engine="openpyxl",if_sheet_exists="replace") as writer:
                            input_df_1.to_excel(writer, sheet_name=Sheet_name,index=False) 
                        print("'Trim Columns/Header' names is Done")
                        return "True : 'Trim Columns/Header' names is Done"
                    
                    else:
                        print("Input Path/File not Found")
                        return "False: Input Path/File not Found"
                except Exception as e:
                    print("Error is : ",str(e))
                    return "False : Error is : ",str(e)
            else:
                print("Error: Sheet Name is Empty")
                return "False : Error: Sheet Name is Empty"
        else:
            print("Wrong Input file name")
            return "False : Wrong Input file name"
        
    if __name__ == '__main__':
        trim_columns(data)

except Exception as e:
        print.error('Error occurred ' + str(e))