from riotwatcher import TftWatcher
import pandas as pd
import plotly.graph_objects as go
import numpy as np

api_key = 'RGAPI-199c2cc1-385f-49b0-977f-7c84adcbeffe'
watcher = TftWatcher(api_key)
my_region = 'na1'
summoner_name = 'Mikulll#NA1'

me = watcher.summoner.by_name(my_region, summoner_name)

for key in me:
    print(key, ':', me[key])