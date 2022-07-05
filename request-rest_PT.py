import requests

base_url = "http://192.168.10.254/api/v1"
user = "sarah"
password = "p4ssw0rd"


def get_ticket():
    headers = {"content-type": "application/json"}
    data = {"username": user, "password": password}

    response = requests.post(base_url+"/ticket", headers=headers, json=data)
    ticket = response.json()
    service_ticket = ticket["response"]["serviceTicket"]
    return service_ticket

def get_network_health():
    ticket = get_ticket()
    headers = {"X-Auth-Token": ticket}
    response = requests.get(base_url+"/assurance/health", headers=headers)
    health = response.json()
    network_health = health['response'][0]['networkDevices']['totalPercentage']
    return network_health
        
if __name__ == "__main__":
    network_health = get_network_health()
    print("Persentase Network Health: "+ network_health +"%")