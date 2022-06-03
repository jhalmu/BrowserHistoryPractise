
from datetime import datetime
import pandas as pd
# there is also urllib3 so load that is problems
from urllib.parse import urlparse
# pypi browser_history
from browser_history.browsers import Firefox

# see browser_history docs for browser compatility
# there is allso general, less for macos (as writing)
f = Firefox()
outputs = f.fetch_history()

# his is a list of (datetime.datetime, url) tuples
his = outputs.histories

# Lets put all in dataframe to show data
df = pd.DataFrame(his)
# Giving name for colums 
df = df.set_axis(['aika','osoite'], axis='columns')
# If wanted we can shorten original datetime presentation
df['aika'] = pd.to_datetime(df['aika']).dt.strftime('%Y-%m-%d %H:%M:%S')
# the magic of parsing hostname from long urls
df['osoite']= [urlparse(h[1]).hostname for h in his]
# Time to show enddata and continue 
print(df)