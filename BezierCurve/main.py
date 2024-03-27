import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.widgets import Slider,Button,TextBox

fig,ax = plt.subplots()
points = [1,1,2,2];
ax.plot()
line,=ax.plot()
plt.subplots_adjust(bottom=0.2,)
initial_text = "1,1;2,2"
text_box1 = TextBox(plt.axes((0.1, 0.05, 0.3, 0.075)), 'Enter (x,y) point 1:', initial=initial_text)
axfreq = fig.add_axes((0.25, 0.1, 0.65, 0.03))
slider = Slider(
    ax=axfreq,
    label='Value of T',
    valmin=0,
    valmax=1,
    valinit=0.5,
)
def submit(text):
    points = text.split(';')
    for point in points:
        x1,y1 = map(float,point.split(','))
        ax.plot(x1, y1, 'ro')
    
    plt.draw()

def lerpX(t,x1,x2):
    return x1+t(x2-x1)

def lerpY(t,y1,y2):
    return y1+t(y2-y1)

text_box1.on_submit(submit)
plt.show() 




