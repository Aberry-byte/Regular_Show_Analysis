#!/usr/bin/env python3

import pandas as pd

link = "https://en.wikipedia.org/wiki/List_of_Regular_Show_episodes#Episodes"
for table in range(3, 11, 1):
    tables = pd.read_html(link,header=0)[table]
    tables["Season"] = table - 2
    tables["US viewers(millions)"] = tables["US viewers(millions)"].map(lambda s: str(s).split("[")[0])
    if table > 3:
        tables.to_csv("base.csv", sep=',', index=False, mode="a", header=False)
    else:
        tables.to_csv("base.csv", sep=',', index=False, mode="w")
