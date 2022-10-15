from steam.client import SteamClient
import json
import os
username = ""
password = ""
client = SteamClient()

result = client.cli_login(username, password)
f = open("lastBetaBuild.txt","r")
lastBetaBuild = f.read()
f.close()

resp = client.get_product_info([1059990])
f = open('response.json','w')
json.dump(resp,f)
f.close()

g = open("response.json")
response = json.load(g)
g.close()
os.remove("response.json")
if response["apps"]["1059990"]["depots"]["branches"]["betatesting"]["buildid"] != lastBetaBuild:
    print("New build detected")
    os.system("dotnet DepotDownloader.dll -app 1059990 -beta betatesting")
    f = open("lastBetaBuild.txt","w")
    f.write(response["apps"]["1059990"]["depots"]["branches"]["betatesting"]["buildid"])
    f.close()