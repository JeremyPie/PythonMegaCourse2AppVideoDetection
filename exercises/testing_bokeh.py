from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas as pd

x = [1,2,3,4,5]
y = [6,7,8,9,10]

output_file('line.html')
f = figure()
f.line(x,y)
show(f)


df = pd.read_csv('data.csv')
x1 = df['x']
y1 = df['y']

output_file('line_from_csv.html')
f = figure()
f.line(x1,y1)
show(f)
