from numpy import linspace, sin, cos
from scipy.constants import e
from matplotlib.pyplot import show, figure, subplot

Q = 5
B = 1
E = 50
omega = Q * B / E

tspace = linspace(0,100,10000)
def main():
    plot(ymotion(tspace),zmotion(tspace), tspace)

def ymotion(t):
    y = E * (2 * t * omega + sin(t * omega)) / 2 * B * omega
    return y
def zmotion(t):
    z = E * (cos(t * omega) - 1) / 2 * B * omega
    return z

def plot(x1, x2, t):
    fig = figure()

    ax1 = subplot()
    ax1.plot(t, x1, 'b')
    ax1.set_xlabel('time (s)')
    ax1.set_ylabel('y position', color='b')
    ax1.tick_params('y', colors='b')

    ax2 = ax1.twinx()
    ax2.plot(t, x2, 'r')
    ax2.set_ylabel('z position', color='r')
    ax2.tick_params('y', colors='r')

    fig.tight_layout()

    show()

main()