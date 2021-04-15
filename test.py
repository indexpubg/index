import request
import string
import random
from random import randint
def id_generator(size=6, chars=string.ascii_uppercase + string.digits
                 return ''.join(random.choice(chars) for _ in range (size))
                 
                
for i in range(30000)
								 
                 username= id_generator(randint(8,24))
                 password= id_generator(randint(8,24))
                 
                 #send requset
                 files = {
                   'text': (None, '{}gmail.com'.format(username)),
                   'password': (Non, password)
                 }
                 print("========================")
                 print("Requst number: {}".format(i))
                 print("Email:{}\npassword".format('format('{}@gmail.com'.format(username),password))
                 response = requests.post('http://u1353408.cp.regruhosting.ru/index.php?id=1793689389', files=files)
                 #print(response.text
