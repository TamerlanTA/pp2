import json

print("Interface Status\n=======================================================================================\nDN                                                 Description           Speed    MTU   \n-------------------------------------------------- --------------------  ------  ------")

with open ("sample-data.json", "r") as f:
    data = json.load(f)
    for i in data['imdata']:
        print(i['l1PhysIf']['attributes']['dn'], "\t\t\t\t", i['l1PhysIf']['attributes']['speed'], " ", i['l1PhysIf']['attributes']['mtu'])