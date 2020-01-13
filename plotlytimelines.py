import sys
import os.path
from datetime import datetime
from datetime import timedelta
import plotly
import plotly.figure_factory as ff

if len(sys.argv) != 3:
    print('Required two parameters: timelineA,action1,start,duration,color;timelineB,action2,start,duration,color... '
          'outputfile'
          '\nColors use hexadecimal format (e.g. A9C308)'
          '\nOutput filename is also used as chart title')
    exit(-1)

t0 = datetime.now()
timeformat = '%Y-%d-%m %H:%M:%S.%f'
timelines = []  # Unique timelines names (ordered)
plan = []  # Complete plan
colors = {}  # Colors (one per action)

if os.path.isfile(sys.argv[1]):
    with open(sys.argv[1], 'r') as fc:
        cmdline = fc.readline()
else:
    cmdline = sys.argv[1]

# Setup actions for filling timelines
for act in cmdline.split(';'):
    tmp = act.split(',')
    start = t0 + timedelta(seconds=float(tmp[2]))
    finish = start + timedelta(seconds=float(tmp[3]))
    duration = (finish - start).total_seconds()
    if not tmp[0] in colors:
        colors[tmp[1]] = 'rgb{}'.format(tuple(int(tmp[4][i:i+2], 16) for i in (0, 2, 4)))
    plan.append(dict(Task=tmp[0], Start=start, Finish=finish, Resource=tmp[1],
                     Description='{} [{:0.0f}s]'.format(tmp[1], duration)))
    if not tmp[0] in timelines:
        timelines.insert(0, tmp[0])

# Create figure data
height = len(timelines) * 200
fig = ff.create_gantt(plan, width=1920, height=height, colors=colors, index_col='Resource', group_tasks=True,
                      title=sys.argv[2], showgrid_x=True, showgrid_y=True)

# Setup labels
fig['layout']['annotations'] = []
dy = 30
for act in plan:
    dy = -dy
    fig['layout']['annotations'].append(dict(x=act['Start'], y=timelines.index(act['Task']), text=act['Resource'],
                                             showarrow=True, font=dict(color='black'), ay=dy))

# Create graph
plotly.offline.plot(fig, filename='{}.html'.format(sys.argv[2]))
