from cassandra.cluster import Cluster
import json

clstr=Cluster(contact_points = ['192.168.16.1'], port=9042, protocol_version=4)

file = open("data.json","r")
ListOfDic = json.load(file)

session=clstr.connect('sensorkeyspace')

counter = 0

## In order for cassandra to understand a UDT that is defined in Python u need to declare it as a Object.

class CassandraUDT(object):
    def __init__(self, x, y, z, time):
        self.x = x
        self.y = y
        self.z = z
        self.time = time

for i in range(len(ListOfDic)):
    userid = ListOfDic[i]["userid"]
    starttime = ListOfDic[i]["starttime"]
    fahrtid = ListOfDic[i]["fahrtid"]
    coordinates = ListOfDic[i]["coordinates"]

    insertList = []
    for a in range(len(ListOfDic[i]["coordinates"])):
        tmp = CassandraUDT(ListOfDic[i]["coordinates"][0][0], ListOfDic[i]["coordinates"][0][1], ListOfDic[i]["coordinates"][0][2], ListOfDic[i]["coordinates"][0][3])
        insertList.append(tmp)

    qry = session.prepare("INSERT INTO timeseries (userid, starttime, fahrtid, coordinates) VALUES (?, ?, ?, ?);")
    session.execute(qry, [userid, starttime, fahrtid, insertList])
    print("Inserted!")
    print(counter + 1)
    counter = counter + 1