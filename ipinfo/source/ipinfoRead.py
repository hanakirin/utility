import sys
import requests
import configparser

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
    config_ini = configparser.ConfigParser()
    config_ini.read('config.ini', encoding='utf-8')
    api_key = config_ini['IPINFO']['api_key']

    if len(sys.argv) == 2:
        ip_address = sys.argv[1]
    else:
        print("Argument Error: python ipinfoRead.py {IP Address}")
        sys.exit()

    ip_info = get_ip_info(ip_address, api_key)
    if ip_info:
        print("IP Information:")
        for key, value in ip_info.items():
            print(f"{key}: {value}")
    else:
        print("Failed to retrieve information for the IP address.")