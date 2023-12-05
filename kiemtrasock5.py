import socket
import threading
import socks 
def check_proxy(proxy, target_host, target_port, output_file):
    # try:
    #     # Tách địa chỉ proxy và cổng
    #     proxy_ip, proxy_port = proxy.split(":")
    #     socks.set_default_proxy(socks.SOCKS5, proxy_ip, int(proxy_port))
    #     socket.socket = socks.socksocket
    #     proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     proxy_socket.settimeout(0.2)
    #     proxy_socket.connect((target_host, target_port))
    #     thread_count = threading.active_count()
    #     #print(f"Attack by socks4 to {target_host}:{target_port} through {proxy} co {thread_count} proxy dang chay")
    #     print(f"Kiem tra thanh cong through {proxy}")
    #     # Nếu kết nối thành công, ghi proxy vào tệp sock4ss.txt
    #     output_file.write(proxy +'\n')
    #     # Đóng kết nối với proxy
    #     proxy_socket.close()
    #     #return True
    # except:

    #     #print(f"Attack that bai by socks4 to {target_host}:{target_port} through {proxy}")
    #     #return True
    #     pass
    if len(proxy) == 4:
        proxy_host, proxy_port = proxy[0], int(proxy[1])
        proxy_username = proxy[2]
        proxy_password = proxy[3]
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
            proxy_socket.connect((target_host, target_port))
            thread_count = threading.active_count()
            print(f"Kiem tra thanh cong through {proxy}")
    #     # Nếu kết nối thành công, ghi proxy vào tệp sock4ss.txt
            output_file.write(proxy_host + ':' + proxy_port + ':'+ proxy_username + ':'+ proxy_password +'\n')
            proxy_socket.close()
        except Exception as e:
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
            proxy_socket.connect((target_host, target_port))
            print(f"Kiem tra thanh cong through {proxy}")
    #     # Nếu kết nối thành công, ghi proxy vào tệp sock4ss.txt
            output_file.write(proxy +'\n')
            proxy_socket.close()
        except Exception as e:
            pass
            #return

# Đọc danh sách proxy từ tệp sock4s.txt
with open("socks5.txt", "r") as f:
    proxies = f.read().splitlines()

# Tạo kết nối đến máy chủ 103.82.36.115 qua cổng 1449
target_host = "103.195.237.74"
target_port = 12345

# Tạo một tệp mới sock4ss.txt để lưu proxy kết nối được
with open("sock5ss.txt", "a") as output_file:
    threads = []
    
    # Tạo một luồng cho mỗi proxy và bắt đầu chạy chúng
    for proxy in proxies:
            
        thread = threading.Thread(target=check_proxy, args=(proxy, target_host, target_port, output_file))
        thread.daemon = True
        threads.append(thread)
        thread.start()
    
    #Chờ cho tất cả các luồng hoàn thành
    for thread in threads:
        thread.join()

print("Kiểm tra và ghi proxy xong.")
