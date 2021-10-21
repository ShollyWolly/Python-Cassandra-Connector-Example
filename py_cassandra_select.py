import pandas as pd
from cassandra.cluster import Cluster

clstr=Cluster(contact_points = ['192.168.16.1'], port=9042, protocol_version=4)

session=clstr.connect('sensorkeyspace')

## Selecting the whole table an putting it into a Pandas DF for further analysis.

def pandas_factory(colnames, rows):
    return pd.DataFrame(rows, columns=colnames)

session.row_factory = pandas_factory
session.default_fetch_size = None

query = "SELECT * from timeseries;"
rslt = session.execute(query, timeout=None)
df = rslt._current_rows

print(df)


