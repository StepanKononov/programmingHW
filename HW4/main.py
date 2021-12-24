import sys
import requests
import json
import plotly.express as px

INPUT_FILE = "input.txt"
COUNTRY = 'country'
CITY = 'city'
REGION = 'region'

sys.stdin = open(INPUT_FILE)

ar_ip = []

for line in sys.stdin:
    ar_ip.append(line.rstrip())

data = dict(country=[], region=[], city=[])

for i in range(len(ar_ip)):
    response = requests.get(f"https://ipinfo.io/{ar_ip[i]}?token=00c2c415b236e4")
    if response.ok:
        response_data = json.loads(response.content.decode())
        if response_data.keys() & {COUNTRY, CITY, REGION}:
            data[COUNTRY].append(response_data[COUNTRY])
            data[CITY].append(response_data[CITY])
            data[REGION].append(response_data[REGION])
        else:
            print("Incorrect IP")
    else:
        print("Some error =(")

fig = px.sunburst(
    data,
    path=[COUNTRY, REGION, CITY],
)
fig.show()

# region Description
tem = []
for j in range(len(data['country'])):
    tem.append([data['country'][j], data['city'][j], data['region'][j]])
tem.sort()

for elem in tem:
    print(*elem)
# endregion
