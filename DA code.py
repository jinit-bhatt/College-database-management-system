import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="root",database="college")
if mycon.is_connected():
    print("Successfully connected to MySQL database")
    cursor=mycon.cursor()
else :
    print("Unable to connect with Database")
def accept():
    count=1
    print ("What do you want to input?")
    print ("press 1 For Student Details ")
    print ("press 2 For Parent Details")
    print ("press 3 For Teacher Details")
    count=int(input("Your choice "))
    if count==1:
        x=1
        while x==1:
            mReg_no=int(input("Enter Reg Number :"))
            mF_name=input("Enter First name :")
            mL_name=input("Enter Last name :")
            mGender=input("Enter Gender code(M-Male/F-Female) :")
            mBlood_group=input("Enter Blood Group :")
            mContact_no=int(input("Enter Contact Number :"))
            mEmail=input("Enter Email ID :")
            mDob=input("Enter Date of Birth in YYYY-MM-DD Format :")
            mAddress=input("Enter Address :")
            mSem=int(input("Enter Semester :"))
            mSec=input("Section :")
            mTeacher_Guardian=input("Enter Teacher Guardian Code :")
            mSub_code=input("Enter the Subject Code :")
            st="""INSERT INTO student(Reg_No,First_Name,Last_Name,Gender,Blood_Group,Contact_No,Email_address,DOB,Address,Sem,Sec,Teacher_Guardian,Subject_code)
                  VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            recordTuple=(mReg_no,mF_name,mL_name,mGender,mBlood_group,mContact_no,mEmail,mDob,mAddress,mSem,mSec, mTeacher_Guardian,mSub_code)
            cursor.execute(st,recordTuple)
            mycon.commit()
            x=int(input("enter 1 to continue adding and 0  to stop"))
    elif count==2:
        dinsertOG="INSERT INTO parent VALUES("
        x=1
        while x==1:
            dinsert=dinsertOG
            n1=input("Enter Parent ID")
            n2=input("Enter Parent Name")
            n3=input("Enter the relation with ward (Father/Mother/Guardian)")
            n4=input("Enter contact No.")
            n5=input("Enter Email ID")
            n6=input("Enter Ocupation")
            n7=input("Enter Reg No. of the ward")
            dinsert=dinsert+'"'+n1+'"'+','+'"'+n2+'"'+','+'"'+n3+'"'+','+n4+','+'"'+n5+'"'+','+'"'+n6+'"'+','+'"'+n7+'"'+')'
            cursor.execute(dinsert)
            mycon.commit()
            x=int(input("enter 1 to continue adding and 0  to stop"))            
    elif count==3:
        dinsertOG="INSERT INTO teacher VALUES("
        x=1
        while x==1:
            dinsert=dinsertOG
            n1=input("Enter Teacher ID")
            n2=input("Enter Teacher Name")
            n3=input("Enter contact No.")
            n4=input("Enter Email ID")
            n5=input("Enter Designation")
            dinsert=dinsert+'"'+n1+'"'+','+'"'+n2+'"'+','+n3+','+'"'+n4+'"'+','+'"'+n5+'"'+')'
            cursor.execute(dinsert)
            mycon.commit()
            x=int(input("enter 1 to continue adding and 0  to stop"))
    else:
        print ("INVALID CHOICE")
def display():
    print ("Select the category you want to display")
    print ("1.-> Details of all Students.")
    print ("2.-> Details of all Parents.")
    print ("3.-> Details of all Class Teachers.")
    print ("4.-> All details of a Specific Student.")
    print ("5.-> Student details of a Specific Teacher Guardian.")
    print ("6.-> Parent details of a Specific Student.")
    print ("7.-> All student details of a Specific Suject.")
    print ("8.-> Student details of a Specific Sem.")
    count=int(input("Enter your Choice "))
    if count==1:
        cursor.execute("SELECT * FROM student")
        myresult=cursor.fetchall()
        for i in myresult:
            print(i)
    elif count==2:
        cursor.execute("SELECT * FROM parent")
        myresult=cursor.fetchall()
        for i in myresult:
            print(i)
    elif count==3:
        cursor.execute("SELECT * FROM teacher")
        myresult=cursor.fetchall()
        for i in myresult:
            print(i)
    elif count==4:
        input_var=int(input("Enter Reg No of the student"))
        cursor.execute("""SELECT * FROM student WHERE Reg_No = %s""" ,(input_var,))
        myresult=cursor.fetchall()
        for i in myresult:
            print(i)
    elif count==5:
        input_var=input("Enter Teacher Guardian ID")
        cursor.execute("""SELECT * FROM student WHERE Teacher_Guardian= %s""",(input_var,))
        myresult=cursor.fetchall()
        for i in myresult:
            print(i)
    elif count==6:
        input_var=int(input("Enter Reg No of the student"))
        cursor.execute("""SELECT * FROM parent WHERE Reg_No= %s""" ,(input_var,))
        myresult=cursor.fetchall()
        for i in myresult:
            print(i)
    elif count==7:
        input_var=input("Enter Subject code of the student")
        cursor.execute("""SELECT * FROM student WHERE Subject_code= %s""" ,(input_var,))
        myresult=cursor.fetchall()
        for i in myresult:
            print(i)
    elif count==8:
        input_var=int(input("Enter the Sem of the student"))
        cursor.execute("""SELECT * FROM student WHERE Sem=%s""" ,(input_var,))
        myresult=cursor.fetchall()
        for i in myresult:
            print(i)
    else:
        print("invalid choice")

def remove():
    count=1
    print ("What do you want to remove?")
    print ("press 1 For Student Details ")
    print ("press 2 For Parent Details")
    print ("press 3 For Teacher Details")
    count=int(input("Your choice "))
    if count==1:
        x=1
        while x==1:
            mGr_no=int(input("Enter Reg Number :"))
            cursor.execute("""DELETE FROM student WHERE Reg_No = %s""" ,(mGr_no,))
            mycon.commit()
            print("Successfully Deleted Record") 
            x=int(input("enter 1 to continue deleting and 0  to stop"))
    elif count==2:
        x=1
        while x==1:
            mpr_id=int(input("Enter Parent ID  :"))
            cursor.execute("""DELETE FROM Parent WHERE Parent_ID= %s""" ,(mpr_id,))
            mycon.commit()
            print("Successfully Deleted Record") 
            x=int(input("enter 1 to continue deleting and 0  to stop"))
    elif count==3:
        x=1
        while x==1:
            mtr_id=int(input("Enter Teacher ID :"))
            cursor.execute("""DELETE FROM teacher WHERE TeacherID = %s""" ,(mtr_id,))
            mycon.commit()
            print("Successfully Deleted Record") 
            x=int(input("enter 1 to continue deleting and 0  to stop"))
    
    else:
        print ("INVALID CHOICE")

def modify():
    print ("Enter Student Reg NO to promote in the next sem")
    mGr_no=int(input("Enter Reg Number :"))
    mStd=int(input("Enter new Sem :"))
    mDiv=input("Enter New Section :")    
    st="""UPDATE student SET Sem=%s,Sec=%s WHERE Reg_No=%s"""
    recordTuple=(mStd,mDiv,mGr_no)
    cursor.execute(st,recordTuple)
    mycon.commit()
    print(" Record modified Successfully") 
                    
#-----------------------------------------------------------------------
print ("WELCOME TO College MANAGMENT SYSYTEM")
n=1
while n==1:
    print ("press I to insert")
    print ("press D to display")
    print ("Press R to remove record")
    print ("press M to Modify")
    print ("press E to end")
    choice= input("Enter your choice ")
    if choice.lower()=="i":
        accept()
        n=1
    elif choice.lower()=="d":
        display()
        n=1
    elif choice.lower()=="r":
        remove()
        n=1
    elif choice.lower()=="m":
        modify()
        n=1
    elif choice.lower()=="e":
        print ("GOODBYE")
        n=0
    else:
        print ("INVALID CHOICE")
        n=1
mycon.close()
