from cassandra.cluster import Cluster
clstr=Cluster(contact_points = ['192.168.16.1'], port=9042)

session=clstr.connect()

## Creating Cassandra Keyspace, type and tables in the DB itsself.

session.execute("create keyspace if not exists sensorkeyspace with replication = { 'class': 'SimpleStrategy', 'replication_factor' : 2 };")

print("Created Keyspace 'sensorkeyspace'!")

session=clstr.connect("sensorkeyspace")

session.execute("create type if not exists CassandraUDT (x float, y float, z float, time text);")

print("Created Type 'CassandraUDT'!")

qry= '''
create table if not exists timeseries (
   userid int,
   fahrtid int,
   starttime text,
   coordinates frozen<List<CassandraUDT>>,
   primary key(userid, starttime, fahrtid),
   ) with clustering order by (starttime desc);
   '''

session.execute(qry)

print("Created Table 'timeseries'!")





