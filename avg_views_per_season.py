#!/usr/bin/env python3 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plot

plot.style.use("seaborn")
df = pd.read_csv("base.csv")

avg_views_per_season = []
for season in df.Season.unique():
    avg_views_per_season.append(np.mean(df.loc[df["Season"] == season]["US viewers(millions)"]))

plot.plot(df.Season.unique(), avg_views_per_season)
plot.title("Average number of views per season")
plot.xlabel("Season #")
plot.ylabel("avg no. of views (millions)")
plot.ylim(bottom=0)
plot.savefig("AvgViewsPerSeason.png", format="png", dpi=200)
plot.show()