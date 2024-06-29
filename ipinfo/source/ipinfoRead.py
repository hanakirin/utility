import requests

def get_ip_info(ip_address, token):
    url = f"https://ipinfo.io/{ip_address}/json"
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == "__main__":
    ip_address = input("Enter an IP address: ")
    token = "xxx"  # ここにIPinfoのAPIキーを入力してください
    ip_info = get_ip_info(ip_address, token)
    
    if ip_info:
        print("IP Information:")
        for key, value in ip_info.items():
            print(f"{key}: {value}")
    else:
        print("Failed to retrieve information for the IP address.")