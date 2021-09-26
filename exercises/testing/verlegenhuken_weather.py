import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, show

df = pd.read_excel('verlegenhuken.xlsx')
x, y = df['Temperature'], df['Pressure']

output_file('verlegenhuken_bokeh.html')
f = figure()
f.title.text = 'Temperature and Air Pressure'
f.title.text_color = 'blue'
f.title.text_font = 'times'
f.title.text_font_style = 'bold'
f.xaxis.minor_tick_line_color = 'red'
f.yaxis.minor_tick_line_color = 'red'
f.xaxis.axis_label = 'Temperature (C)'
f.yaxis.axis_label = 'Pressure (hPa)'

f.dot(x/10,y/10, size = 6)
show(f)
