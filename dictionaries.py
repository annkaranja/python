Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> customer1={"name":"chesang","balance":1000}
>>> customer2={"name":"charity","balance":2000}
>>> customer3={"name":"lucian","balance":4800}
>>> customer4={"name":"asha","balance":3600}
>>> 
>>> customers=[customer1,customer2,customer3,customer4]
>>> customers
[{'name': 'chesang', 'balance': 1000}, {'name': 'charity', 'balance': 2000}, {'name': 'lucian', 'balance': 4800}, {'name': 'asha', 'balance': 3600}]
>>> for customer in customers:
	msg="hello {}, your balance is {}".format(customer["name"],customer["balance"])
	print(msg)

	
hello chesang, your balance is 1000
hello charity, your balance is 2000
hello lucian, your balance is 4800
hello asha, your balance is 3600
>>> for customer in customers:
	for customer in customers:
		msg="hello {}, your balance is {} and you qualify for a loan of {}".format(customer["name"],customer["balance"],customer["balance//2.6"])
		print(msg)

		
Traceback (most recent call last):
  File "<pyshell#14>", line 3, in <module>
    msg="hello {}, your balance is {} and you qualify for a loan of {}".format(customer["name"],customer["balance"],customer["balance//2.6"])
KeyError: 'balance//2.6'
>>> for customer in customers:
	for customer in customers:
		msg="hello {}, your balance is {} and you qualify for a loan of {}".format(customer["name"],customer["balance"],customer["balance"]//2.6)
		print(msg)

		
hello chesang, your balance is 1000 and you qualify for a loan of 384.0
hello charity, your balance is 2000 and you qualify for a loan of 769.0
hello lucian, your balance is 4800 and you qualify for a loan of 1846.0
hello asha, your balance is 3600 and you qualify for a loan of 1384.0
hello chesang, your balance is 1000 and you qualify for a loan of 384.0
hello charity, your balance is 2000 and you qualify for a loan of 769.0
hello lucian, your balance is 4800 and you qualify for a loan of 1846.0
hello asha, your balance is 3600 and you qualify for a loan of 1384.0
hello chesang, your balance is 1000 and you qualify for a loan of 384.0
hello charity, your balance is 2000 and you qualify for a loan of 769.0
hello lucian, your balance is 4800 and you qualify for a loan of 1846.0
hello asha, your balance is 3600 and you qualify for a loan of 1384.0
hello chesang, your balance is 1000 and you qualify for a loan of 384.0
hello charity, your balance is 2000 and you qualify for a loan of 769.0
hello lucian, your balance is 4800 and you qualify for a loan of 1846.0
hello asha, your balance is 3600 and you qualify for a loan of 1384.0
>>> 
