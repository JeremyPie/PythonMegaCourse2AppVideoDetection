import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, show

df = pd.read_csv('bachelors.csv')
x, y = df['Year'], df['Engineering']
f = figure()
f.line(x,y)
output_file('bachelors_linear.html')
show(f)
