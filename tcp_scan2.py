import socket
from datetime import datetime
import threading
from queue import Queue

#it prevents duolicate entries from shared variables
print_lock = threading.Lock()

host=input("Enter the host address to scan: ")
ip=socket.gethostbyname(host) # translate host name to ipv4 address format

num1=int(input("Enter the starting port number: "))
num2=int(input("Enter the ending port number: "))

print("-"*80)
print("                      Please wait,Scanning the host-------------->",ip)
print("-"*80)

#starting time

t1=datetime.now()
def scan(port):

    try:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
        result = sock.connect_ex((ip,port))
        if result==0:
            #if socket is listening it will print socket number
            print("\n Port %d is OPEN-------->"%(port))
            sock.close()
        else:
            print("\nPort %d is CLOSE:-"%(port))
    except:
        pass


#create threader function

def threader():
    while True:
        worker=q.get() #get an worker from queue
        scan(worker) #scan is funstion and it run the job with the available worker in queue
        q.task_done() #complete with the job

#create a queue

q=Queue()

#writing for loop for number of thread to allow

for x in range(60):
    t=threading.Thread(target=threader)
    t.daemon=True
    t.start()

for worker in range(num1,num2+1):
    q.put(worker)

#thread will join after thread termination

q.join()

#calculate end of execution time
t2 = datetime.now()
#calculate the difference
total = t2-t1
#pirnt the difference 
print("Total Scanning Time : ",total)



