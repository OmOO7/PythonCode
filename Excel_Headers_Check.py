#   
#   Excel Process
#   Excel_Headers_Check
#   Date of Modified    : 04-Aug-2022
#   Modified            : Karthik Ravi (karthik.ravi@external.merckgroup.com)
#   

import pandas as pd
import os

data=[None] * 4
#data[0]="PR_List.xlsx"
#data[1]="C:\Users\X244577\Karthik\Excel Process\"   #should end with \
#data[2]="Sheet99"  # sheet name
#data[3]="header_name_1|header_name_2|header_name_3" each and every header name should seperated by | symbol
# data[0]="PR_List.xlsx"
# data[1]="D:\\TEST\\"
# data[2]="PR_List"
# data[3] = "Doc. Type|Fix. Vend.|Name of Vendor|Purch.Req.|Item|Material|Short Text|Quantity|Plnt|PGr|POrg|PDT|Deliv.dt|Release Dt|Req. Date|Created|Total Val.|Crcy|MRPC"

try:
    def excel_headers_check(inp):
        Input_file_name                        =   inp[0]
        Input_file_path                        =   inp[1]
        Sheet_name                             =   inp[2]
        Headers_name                          =   inp[3].lower()
        
        if (".xlsx" in Input_file_name):
            if Sheet_name != '':
                try:
                    Input_file_name_with_path          =   Input_file_path + Input_file_name
                    file_exists                        =   os.path.exists(Input_file_name_with_path)
                    
                    if file_exists == True:
                        
                        input_df_1                  =   pd.read_excel(Input_file_name_with_path,sheet_name=Sheet_name,engine="openpyxl")
                        input_df_2                  =   input_df_1.loc[:, ~input_df_1.columns.str.match('Unnamed')]
                        input_header_list           =   list(input_df_2.columns.values)
                        mismatch_header_list        =   []
                        
                        for header in input_header_list:
                            if header.lower() in Headers_name:
                                pass
                            else:
                                mismatch_header_list.append(header)
                        
                        if(len(mismatch_header_list)>0):
                            print("False : Wrong Header(s) Found.\n")
                            mismatch_header = '|'.join(mismatch_header_list)
                            mismatch_header = "False : Wrong Header(s) Found." + mismatch_header
                            print(mismatch_header)
                            print("\n\n\n\n")
                            return mismatch_header
                        else: 
                            print("All headers are Matched!")
                            return "True : All headers are Matched!"
                    
                    else:
                        print("Input Path/File not Found")
                        return "False : Input Path/File not Found"
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
        excel_headers_check(data)

except Exception as e:
        print.error('Error occurred ' + str(e))