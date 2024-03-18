#!/usr/bin/python3
import os 
import csv 
import json
from datetime import *

date=date.today()
time1=datetime.now()

#filepath=time1.strftime("daily_reports_%Y%m-%d-%H-%M.csv")
filepath=("daily_reports.csv")
jsonfile="update_file.json"
with open(jsonfile) as jf:
    my_dict=json.load(jf)
os_name=os.popen(my_dict['os_flavour']).read().strip('\n')
print(os_name)
if os_name == "ubuntu" or os_name == "rhel":
    print("ubuntu and rhel found and we gathering the information , please wait!!!!")

    #hostname deatails
    hostname=os.popen(my_dict["hostname"]).read()
    print(hostname)

    #ip_details
    ip=os.popen(my_dict["ip_address"]).read()
    print(ip)

    #file storage details
    df_details=os.popen(my_dict["df_details"]).read()
    print(df_details)

    #storing variable into  list for clear csv
    header_csv=(my_dict['header_para'])
    header_csv=[str(x) for x in header_csv]
    print(header_csv)

    #data csv
    data_csv= [hostname,ip,df_details]

    file1=open(filepath,'a+')
    writer=csv.writer(file1)
    writer.writerow(header_csv)
    writer.writerow(data_csv)
    file1.close()

    print("file import successfully your current directory"+filepath)
else:
    print("other os found")






