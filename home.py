import sys

def project1():
    import tcp_scan2
def project2():
    import cn_visualisation
    cn_visualisation.main()


while(True):
    num = int(input("Enter Your choice:\n 1: Port Scanner 2: Network visualisation in google maps 3:Exit : "))
    if(num==1):
        project1()
    elif(num==2):
        project2()
    elif(num==3):
        break
    else:
        print("Invalid choice: ")




