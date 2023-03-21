#   
#   Excel Process
#   Remove_Blank_Columns
#   Date of Modified    : 04-Aug-2022
#   Modified            : Karthik Ravi (karthik.ravi@external.merckgroup.com)
#   

import pandas as pd
import os

data=[None] * 3
#data[0]="PR_ListC.xlsx" # file name
#data[1]="D:\\" #should end with \
#data[2]="PR_ListC" # sheet name

try:
    def remove_blank_columns(inp):
        Input_file_name                        =   inp[0]
        Input_file_path                        =   inp[1]
        Sheet_name                             =   inp[2]
        
        if (".xlsx" in Input_file_name):
            if Sheet_name != '':
                try:
                    Input_file_name_with_path          =   Input_file_path + Input_file_name
                    file_exists                        =   os.path.exists(Input_file_name_with_path)
                    
                    if file_exists == True:
                        input_df_1                  =   pd.read_excel(Input_file_name_with_path,sheet_name=Sheet_name, engine="openpyxl")
                        input_df_2                  =   input_df_1.loc[:, ~input_df_1.columns.str.match('Unnamed')]
                        input_df_3                  =   input_df_2.dropna(how='all')
                        
                        with pd.ExcelWriter(Input_file_name_with_path, mode="a", engine="openpyxl",if_sheet_exists="replace") as writer:
                            input_df_3.to_excel(writer, sheet_name=Sheet_name,index=False) 
                        print("'Remove Blank Columns' is Done")
                        return "True : 'Remove Blank Columns' is Done"
                    
                    else:
                        print("Input Path/File not Found")
                        return "False: Input Path/File not Found"
                except Exception as e:
                    print("Error is : ",str(e))
                    return "Error is : " + str(e)
            else:
                print("Error: Sheet Name is Empty")
                return "Error: Sheet Name is Empty"
        else:
            print("Wrong Input file name")
            return "False : Wrong Input file name"
        
    if __name__ == '__main__':
        remove_blank_columns(data)

except Exception as e:
        print('Error occurred ' , str(e))
