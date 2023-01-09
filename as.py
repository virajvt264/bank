import mysql.connector as mysql
conn= mysql.connect(host='localhost', user='root', password='', database='bank')
Cur=conn.cursor()
Cur.execute("use bank")

def save():
    acc_number=input('Enter acc_number:')
    name=input('Enter name:')
    email=input('Enter email:')
    contact=input('Enter contact:')
    q="insert into acc_holders (acc_number,name,email,contact) values(%s, %s, %s, %s)"
    val=(acc_number, name, email, contact)
    Cur.execute(q, val)
    conn.commit()
    s="""CREATE TABLE {}(
         Date DATETIME DEFAULT CURRENT_TIMESTAMP,
         CheckBalance integer(10),
         Credit integer(10),
         Debit integer(10),
         Balance integer(10) 
         )""".format(name)
        
    Cur.execute(s)
    print('account has been created')
    
def balance():
    name=input('Enter customer name:')
    t="SELECT Balance  FROM {}".format(name)
    Cur.execute(t)
    r=Cur.fetchall()
    balance=[*r[-1]]
    v="insert into {}(Balance) values({})".format(name, *balance)
    Cur.execute(v)
    conn.commit()
    print('Balance :',*balance)

def checkbalance():
  name=input('Enter customer name:')
  t="SELECT Balance  FROM {}".format(name)
  Cur.execute(t)
  r=Cur.fetchall()
  if r==list():
    ebal=0
  else:
    ebal=[*r[-1]]
      
  bal='{}'.format(*ebal)
  balance='{}'.format(*ebal)
  v="insert into {} (CheckBalance, Balance) values({}, {})".format(name, bal, balance)
  Cur.execute(v)
  conn.commit()
  print("Save Successfully")
  
def credit():
    ename=input('Enter customer name:')
    t="SELECT Balance  FROM {}".format(ename)
    Cur.execute(t)
    r=Cur.fetchall()
    if r==list():
      ebal=0
    else:
      ebal=[*r[-1]]
      
    ebalance='{}'.format(*ebal)
    eCredit=int(input('Enter Amount:'))
    bal=int(ebalance)+eCredit
    v="insert into {}(Credit, Balance) values({}, {})".format(ename, eCredit, bal)
    Cur.execute(v)
    conn.commit()
    print('Balance :' ,bal)
    print("Credit Successfully")

def debit():
     name=input('Enter customer name:')
     t="SELECT Balance  FROM {}".format(name)
     Cur.execute(t)
     r=Cur.fetchall()
     ebalance=[*r[-1]]
     edebit=int(input('Enter Amount:'))
     balance=int(*ebalance)-edebit
     print(balance)
     v="insert into {}(Debit, Balance) values({}, {})".format(name, edebit, balance)
     Cur.execute(v)
     conn.commit()
     print("Debit Successfully")


while(1):
    choice=int(input('''Enter Choice:
                     \r1:Create Account :
                     \r2:Check Balance  :
                     \r3:Credit         :
                     \r4:Debit          :
                     \r5:Balance        :
                     \r6:Exit           :
                     '''))
    
    if(choice==1):
        print('Entered Choice:')
        save()
    if(choice==2):
        checkbalance()
    if(choice==3):
        credit()
    if(choice==4):
        debit()
    if(choice==5):
        balance()
    if(choice==6):
        break
