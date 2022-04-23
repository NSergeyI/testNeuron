import pandas as pd
import matplotlib.pyplot as plt
import csv

# results = [fields for fields in csv.reader(open("result.csv", newline=''))]
results = pd.read_csv("result.csv", header=0, index_col=0)
results['loss'][:20].plot.line()
plt.show()

print(results)