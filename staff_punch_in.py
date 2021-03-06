# -*- coding: utf-8 -*-
import time
import datetime
import subprocess

# 匯入工號姓名表
import staff_list_file
staff_list = staff_list_file.staff_list

punch_in_or_out = {1: "上班", 2: "下班"}

# 在terminal運作時設定string的顏色
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

staff = True

# 使輸入畫面重複出現>
def staff_input():
    while staff == True:

        subprocess.call('clear',shell=True)
        print "\n"

        print bcolors.WARNING + "人事資料登錄" + bcolors.ENDC
        print "\n"
        
        # 讓員工名單照姓名順序print。待研究這段的意思，Google找來的code，還沒弄懂就先用了。    
        print "姓名", "\t", "工號"
        
        # 把工號姓名的字典 key/value 反過來
        staff_list_reversed = dict((y,x) for x,y in staff_list.iteritems())
        for staff_name, staff_number in sorted(staff_list_reversed.iteritems()):
            print staff_name, "\t", staff_number

        print "\n"

        staff_number = raw_input("請輸入員工編號> ")

        if staff_number in staff_list:
            in_or_out = raw_input("1，上班。2，下班。請輸入> ")
            
            print "\n"
            
            if in_or_out != "1" and in_or_out != "2":
                print bcolors.WARNING + "資料有誤，請重新輸入。" + bcolors.ENDC
                raw_input()
                manual_check_input_data = "n"
                break
            else:
                int_in_or_out = int(in_or_out)

                # 產生時間戳記
                time_in_sec = time.time()
                time_and_date = datetime.datetime.fromtimestamp(time_in_sec).strftime('%Y/%m/%d, %H:%M')

                # print打卡結果給員工看到
                print "請確認輸入資料："
                
                print "\n"
                print bcolors.WARNING + staff_list[staff_number] + bcolors.ENDC
                print bcolors.WARNING + time_and_date + bcolors.ENDC
                print bcolors.WARNING + punch_in_or_out[int_in_or_out] + bcolors.ENDC
                print "\n"
        
                manual_check_input_data = raw_input("確認資料正確？(y/n)")
                print "\n"


        
            if manual_check_input_data != "y":
                print bcolors.WARNING + "資料有誤，請重新輸入。" + bcolors.ENDC
                raw_input()
                break
            else:
                print "輸入完成，謝謝您，祝您有愉快的一天。"
                
                # 找到最後的字元？待研究這段的意思，Google找來的code，還沒弄懂就先用了。
                target = open("staff_punch_in_record", 'r+')
                target.seek(-2, 2)
                if target.read(2) == '\n\n':
                    target.seek(-1, 1)
    
                # 寫入staff_punch_in_record
                target.write(staff_number)
                target.write(", ")
                target.write(staff_list[staff_number])
                target.write(", ")
                target.write(punch_in_or_out[int_in_or_out])
                target.write(", ")
                target.write(time_and_date)
                target.write('\n')
                target.close()
                
                raw_input()

        else:
            print bcolors.WARNING + "編號錯誤。請輸入正確的員工編號。" + bcolors.ENDC
            raw_input()

while staff == True:
    staff_input()
