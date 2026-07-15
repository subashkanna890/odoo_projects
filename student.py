
# class Student:
#     def __init__(self, name):
#         self.name = name

# student = Student("Subash")
# print(student.name)

# class Student:
#     def __init__(self, name):
#         self.name = name

#     def display(self):
#         print("Name:", self.name)

# s1 = Student("Subash")
# s1.display()



# a=17
# b=36
# print(a+b)


# a="hello"
# b="world"
# print(a+b)




# class tamil:
#     def greeting(self):
#         print("vanakkam !")
# class english:
#     def greeting(self):
#         print("hello !")
# class malayalam:
#     def greeting(self):
#         print("namaskaram !") 

# anbu=tamil()
# john=english()
# kalyani=malayalam()

# def sayhello(obj):
#     return obj.greeting()

# sayhello(anbu)

# class student:
#     def  __init__(self,mark):
#         self.mark=26

#     def __add__(self, other):
#         return self.mark+other.mark
    
#     def __eq__(self, other):
#         return self.mark == other.mark

# s1=student(1)
# s2=student(2)

# print(isinstance(s2,student))


# print(s1+s2)
# print(s1==s2)

# a="hello"
# b="world"

# # print(a+b)
# print(isinstance(a,str))



# class payment:
#     def __init__(self,amount):
#         self.amount=amount

#     def pay(self):
#         print(" processing payment")

# class creditcard(payment):
#     def pay(self):
#         print(f"paid ₹{self.amount} using credit card !")
# class UPI (payment):
#     def pay(self):
#         print(f"paid ₹{self.amount} using UPI !")
# class netbanking(payment):
#     def pay(self):
#         print(f"paid ₹{self.amount} using netbanking !")

# payments=[
#     creditcard(6000),
#     UPI(7000),
#     netbanking(1000)
# ]

# for payment in payments:
#     payment.pay()


# class Bankaccount:
#     def __init__(self,owner,balance):
#         self.owner= owner
#         self.bankname="sbi"
#         self.__balance= balance

#     def get_balance(self):
#         return self.__balance
#     def set_balance(self,new_balance):
#         self.__balance = new_balance

# p1=Bankaccount("subash",100000)
# # print(p1.get_balance())
# p1.set_balance(2000000)
# print(p1.get_balance())


        

# accounts = [
#     {"owner": "subash", "balance": 170000},
#     {"owner": "vishnupriya", "balance": 200000}
# ]

# for account in accounts:
#     print(f"Owner   : {account['owner']}")
#     print(f"Balance : {account['balance']}")
#     print("-" * 20)




class employee:
    def __init__(self,name,emp_id,salary):
        self.name=name
        self.emp_id=emp_id
        self.salary=salary

    def get_salary(self):
        return self.__salary
    
    def set_salary(self, value):
        if value < 0:
            print(" ❌ Aiyo! Salary negative irukka mudiyathu ")
        elif value > 500000
            print(" ❌ Aiyo! Salary limit exceed aachu !")
        else:
            self._salary = value
            print(f" ✅️ Salary updated: {self._salary}")

emp=employee("subash","A101",15000)
emp.display()
