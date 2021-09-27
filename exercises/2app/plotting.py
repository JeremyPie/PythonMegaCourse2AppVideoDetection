from motion_detector import df
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSoruce

df['Start_str'] = df['Start'].dt.strftime("%Y-%m-%d %H:%M%S")
df['End_str'] = df['End'].dt.strftime("%Y-%m-%d %H:%M%S")

cds = ColumnDataSoruce(df)

f = figure(x_axis_type = 'datetime', heigh = 100, width = 500, sizing_mode = 'scale_both')
f.yaxis.minor_tick_line_color = None
f.ygrid[0].ticker_desired_num_ticks = 1
hover = HoverTool(tooltips = [('Start', '@Start_str'), ('End', '@End_str')])
f.add_tools(hover)
                  

q = f.quad(left = 'Start', right = 'End', bottom = 0, top = 1, color = 'green', source = cds)
output_file('Graph.html')
show(q)
