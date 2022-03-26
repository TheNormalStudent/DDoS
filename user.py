from the_ddoser import KILEM

class info:
    def what_to_ddos():
        wtd = input('What to DDoS?\n')
        return wtd
    def get_port():
        port = int(input("Choose if you would like to give port by yourself(1) or to scan ports(2)\n"))
        if port == 1:
            port = int(input("Enter your port...\n"))
        else:
            pass
        return port
    
    def h_many_thr():
        num_of_threads = int(input("How many threads would you like?"))
        return num_of_threads