#================= COLLEGE ADMISSION SYSTEM ===================

#importing pandas to print cutoff list in tabular format
import pandas as pd

# FOR TAKING DATE OF BIRTH INPUT
from datetime import datetime    

#=================== IMPORTING MYSQL FOR DATABASE =================
import mysql.connector as mysql

mydb = mysql.connect(host='localhost',user='root',password='rootroot',database='ncollegeManagement')
if mydb.is_connected():
    print(" MySQL connection successful")

 # create  student tables in collegeManagement db.
'''cur=mydb.cursor()
s="CREATE TABLE student(username varchar(20), password char(15) NOT NULL)"
cur.execute(s)'''

# create staff table in collegeManagement db.
'''cur=mydb.cursor()
ss="CREATE TABLE staff(username varchar(20), password char(15) NOT NULL)"
cur.execute(ss)'''

# creating applied student table in for staff menu
'''cur=mydb.cursor()
Add="CREATE TABLE applied_student(stud_id int not null autoname varchar(20), gender char(15) NOT NULL, email varchar(100) ,DOB varchar(10) not null, contact varchar(20) , percent double NOT NULL , course char(15) NOT NULL )"
cur.execute(Add)'''

#creating merit list db
'''cur=mydb.cursor()
mer="CREATE TABLE merit_list(name varchar(20), gender char(15) NOT NULL, email varchar(100) ,DOB varchar(10) not null , contact varchar(20) , percent double NOT NULL , course char(15) NOT NULL)"
cur.execute(mer)'''



#============ STUDENT MENU ======================
def student():

    print("============ WELCOME STUDENT !!! ============== ")   
    print("1.VIEW COURSES AND FEES")
    print("2.VIEW CUTOFF LIST")
    print("3.APPLICATION FORM")
    print("4.VIEW MERIT LIST")
    print("5.LOGOUT")

    stud_select = input("\nENTER OPTION (1/2/3/4/5) : ")

#============ VIEW COURSES AND FEES =======================
    while 1: #we use loop for coming back to main option menu
        
        if stud_select == '1':
            while 1:
                    
                print("********** COURSES AND THEIR FEES ***********")
                print("PLEASE SELECT STREAM: ")
                print('1.SCIENCE')
                print('2.COMMERCE')
                print('3.ARTS')
                print('4.GO BACK')
                
                user_select = input("\nENTER OPTION (1/2/3/4): ")
                
                if user_select =="1":
                    print("********* SCIENCE COURSES OPTIONS WITH THIER FEES **********")
                    course1=[['BSC',20000],['BSC in computer science',40225],['BSC in IT',40000],['BSC in biotech',45000],['BSC in data science',42550]]

                    df = pd.DataFrame(course1,columns = ['courses ',' fees'])
                    print(df.to_string(index=False)) 

                    

                elif user_select =="2":
                    print(" ********* COMMERCE COURSE OPTIONS WITH THEIR FEES *********")
                    course2=[['BCOM',20000],['BCOM ACCOUNTING AND FINANCE',51855],['BCOM BANKING AND INSURANCE',51855],['BCOM FINANCIAL MARKET',51855]]

                    df = pd.DataFrame(course2,columns = ['courses ',' fees'])
                    print(df.to_string(index=False)) 


                elif user_select =="3":
                    print(" ********* ARTS COURSE OPTIONS WITH THEIR FEES **********")
                    course3=[['BA',20000],['BA in ENGLISH',25000],['BA in SANSKRIT',25000],['BA in ECONOMICS',25000],['BA in PHILOSOPHY',25000],['BA in MULTIMEDIA AND MASS COMMUNICATION',30000]]

                    df = pd.DataFrame(course3,columns = ['courses ',' fees'])
                    print(df.to_string(index=False))

                    

                elif user_select =="4":
                    choice = input('\nDO YOU WANT TO GO BACK (yes/no) : ')
                    if choice == 'yes':
                        # calling student module
                        student()
                    else:
                        pass
                    

            else:
                print("********** INVALID OPTION CHOOSE VALID OPTION ************")

            
         
    #============================CUTOFF LIST==================================
        elif stud_select =='2':
            print("=================== CUTOFF LIST 2022 ======================")
            cutoff=[['BSC',80],['BSC in computer science',85],['BSC in IT',85],['BSC in biotech',82],['BSC in data science',85],['BCOM',75],['BCOM ACCOUNTING AND FINANCE',80],['BCOM BANKING AND INSURANCE',80],['BCOM FINANCIAL MARKET',82],['BA',68],['BA in ENGLISH',70],['BA in SANSKRIT',70],['BA in ECONOMICS',70],['BA in PHILOSOPHY',70],['BA in MULTIMEDIA AND MASS COMMUNICATION',75]]

            df = pd.DataFrame(cutoff,columns = ['courses','cutoff'])
            #print(df)
            print(df.to_string(index=False))
            
            choice = input('\nDO YOU WANT TO GO BACK (yes/no) : ')
            if choice == 'yes':
                # calling student module
                student()
            else:
                pass
                

        #======================Application FORM================================
        elif stud_select =='3':
            print("================= Application form ====================== ")
            print("ALL SECTIONS ARE MENDATORY TO FILL")

            cur=mydb.cursor()
            app= "INSERT INTO applied_student(name,gender, email , DOB , contact, percent, course) VALUES(%s, %s,%s, %s,%s, %s ,%s)"
            
            name=input("ENTER FULL NAME : ")
            gender =input("GENDER (MALE/FEMALE) : ")
            email=input("ENTER YOUR EMAIL: ")
            DOB=input("ENTER YOUR DATE OF BIRTH (DD-MM-YYYY) : ")
            contact_no=int(input("ENTER YOUR CONTACT NUMBER : "))
            percent= float(input("ENTER YOUR PERCENTAGE : "))
            course= input("ENTER COURSE (BCA,BSC,BA,BCOM,BMS,...) : ")

            #INSERTING DATA INTO applied_students TABLE
            x=(name,gender, email ,DOB , contact_no, percent, course)       
            cur.execute(app,x)
            mydb.commit()
            
            print("\nFORM FILLING COMPLETED!!")
            print("YOU WILL GET AN EMAIL FROM THE CLG IF YOU GOT SELECTED")


            choice = input('\nDO YOU WANT TO GO BACK (yes/no) : ')
            if choice == 'yes':
                # calling student module
                student()
            else:
                pass
            #student()


        #====================== VIEW MERIT LIST ==========================

        elif stud_select == '4':
            print("================== MERIT LIST =============== ")
            cur=mydb.cursor()
            m="select * from merit_list"
            cur.execute(m)
            result=cur.fetchall()
            for rec in result:
                print(str(rec[0]) + " | " + str(rec[1]) + " | " + str(rec[2]) + " | " + str(rec[3]) + " | " + str(rec[4]) + " | " + str(rec[5]) + " | "  + str(rec[6]) + "|" + str(rec[7]))

            print("\n\n********** NOTE ************\n 1. Name in the merit list DOES NOT assure admission. \n2. It is mandatory for students to report to College for physical verification of documents within a week to claim admission.")
            print("\n\n==== List of documents to be brought at the time of admission ======\n\n1. Print out of college application form\n2. Self- Attested copy of Aadhar Card\n3. Original and One Self attested copy of HSC marksheet\n4.  Original and One Self attested copy of leaving certificate\n5. Valid Document for claiming other reservation")

            choice = input('\nDO YOU WANT TO GO BACK (yes/no) : ')
            if choice == 'yes':
                # calling student module
                student()
            else:
                pass

        

        #==================== LOGOUT =============================
        elif stud_select == '5':
            logout() #CALLING LOGOUT MODULE


        else:
            print("======= INVALID OPTION =======")
        student()       # calling student module becoz if user put invalid option it will kick out of the program 
        break

#=============== STAFF MENU =========================

#1.view applied student list
#2.confrim student for admission

#STAFF FUNCTION
def staff():
    while 1:
        
        print("========= WELCOME STAFF !!! ========")
        print("1.STUDENT APPLICATION")
        print("2.SELECTED STUDENT LIST BASED ON MERIT LIST")
        print("3.LOGOUT")

        staff_select = input("\nENTER OPTION (1/2/3) : ")


    #============= VIEWING APPLIED STUDENT ====================
        if staff_select =='1':
            cur=mydb.cursor()
            t="SELECT *from applied_student"
            cur.execute(t)
            result=cur.fetchall()
            for rec in result:
                print(str(rec[0]) + " | " + str(rec[1]) + " | " + str(rec[2]) + " | " + str(rec[3]) + " | " + str(rec[4]) + " | " + str(rec[5]) + " | "  + str(rec[6]) + "|" + str(rec[7]))


    #============ PREPARING MERIT LIST ====================
        elif staff_select =='2':
            cur=mydb.cursor()

            m="delete from merit_list"     # It delete old data from merit list table  if we dont do it. It will give us error of duplicate key.....
            cur.execute(m)
            
            m="INSERT INTO merit_list(stud_id,name,gender,email,DOB,contact,percent,course) SELECT * FROM applied_student WHERE percent > '80' "
            # here we are inserting data into merit list  table from applied student table by specifying the condition where percent >'80'
            cur.execute(m)
            result=cur.fetchall()
            for res in result:
                print(res)


            #shows merit list
            cur=mydb.cursor()
            l="SELECT *from merit_list"
            cur.execute(l)
            result=cur.fetchall()
            for rec in result:
                print(str(rec[0]) + " | " + str(rec[1]) + " | " + str(rec[2]) + " | " + str(rec[3]) + " | " + str(rec[4]) + " | " + str(rec[5]) + " | "  + str(rec[6]))
       

        elif staff_select == '3':
            #calling logout module
            logout()

        else:
            print("======= INVALID OPTION =========")
        staff()     # calling staff module so that if user put invalid option it will take back to staff menu again
    

#================ LOGOUT MENU ==============================

def logout():
    print("\n DO YOU WANT TO LOGOUT (yes/no) : ")
    choice = input(" ")
    if choice=='yes':
        print("====== LOGGED OUT ========")
        main()

    else:
        staff()
    
    
#=============== LOGIN MENU =======================
    
def main():
    while 1:
        print("\n\n WELCOME TO THE COLLEGE ADMISSION SYSTEM \n\n")
        print("1. Login as staff")
        
        print("2. Login as student")

        user_option = input("ENTER OPTION : ")

        if user_option == "1":
            print("============= staff Login ===============")
            
            
            #INSERTING staff DATA
            cur=mydb.cursor()
            s= "INSERT INTO staff(username, password) VALUES(%s, %s)"
            val1 = input("Enter your username: ")
            val2 = input("Enter your password: ")
            x=(val1, val2)
            cur.execute(s,x)
            mydb.commit()

            #calling staff module
            staff() 



        elif user_option == "2":
            print("============ student Login ==============")

           #INSERTING DATA INTO STUDENT TABLE
            cur=mydb.cursor()
            s= "INSERT INTO student(username, password) VALUES(%s, %s)"
            val1 = input("Enter your username: ")
            val2 = input("Enter your password: ")
            x=(val1, val2)
            cur.execute(s,x)
            mydb.commit()

            #calling student module
            student()  

        else:
            print("===== INVALID OPTION =======")
        break

main()


mydb.close() #closing database





        
