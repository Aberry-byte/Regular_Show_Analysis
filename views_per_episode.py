#!/usr/bin/env python3 

import pandas as pd
import matplotlib.pyplot as plot

plot.style.use("seaborn")
df = pd.read_csv("base.csv")

plot.plot(list(df["No.overall"]), list(df["US viewers(millions)"]))
plot.xlabel("Episode #")
plot.ylabel("no. of views (millions)")
plot.title("no. of views (millions) per episode")
plot.ylim(bottom=0)
plot.savefig("ViewsPerEpisode.png", format="png", dpi=200)
plot.show()
