
```
clss Graph():
    daf convolutional():
        pass
    def attentional():
        pass
    def message_passing():
        pass

class GraphNode():
    pass

class Agent(GraphNode):
    pass

class cooperation(GraphEdge):
    pass

class MAS(Graph):
    pass

```
<br>

```
A=random.rand(3,5)

from numpy.dual import svd;U,sVh=svd(A)

r=min(*A.shape);Sig=zeros_like(A)
Sig[:r,:r]=diag(s);print Sig

```
```
data=u"1,2,3\n4,5,6"
np.genfromtxt(StringIO(data),delimiter=",")#delimer=(4,3,2)

def f(i,j):
    return 10*i+j

b=np.fromfunction(f,(5,4),dtype=int);b
array([[0,1,2,3],
    [10,11,12,13],
    [20,21,22,23],
    [30,31,32,33],
    [40,41,42,43]]
    

```

```
import numpy as np
import matplotlib.pyplot as plt
def Bode():
    plt.subplot(2,1,1)
    w=np.arange(0.01,100,0.1)
    x=np.log10(w)
    y=-10*np.log10(1+w**2)
    plt.plot(x,y)
    plt.ylabel('Magnitude(dB)')
    plt.title('Bode Diagram')

    
    plt.subplot(212)
    y1=-np.arctan(w)
    plt.plot(x,y1)
    plt.xlabel('Frequency (rad/s)')
    plt.ylabel('Phase(deg)')
    plt.show()
    plt.subplot(212)

def Nichols():
    w=np.arange(0.01,80,0.1)
    x=-np.arctan(w/2)*180/np.pi
    y=-10*np.log10(1+w**2/4)
    plt.plot(x,y)
    plt.ylabel('Magnitude(dB)')
    plt.xlabel('φ(w)/(°)')
    plt.title('Nichols Diagram')
    

    
    plt.show()
    

    
def main():
    #Nichols()
    Bode()

main()
```

<br>
<br>

```
"""Conway's Game Of Life, Author Anurag Kumar(mailto:anuragkumarak95@gmail.com)

Requirements:
  - numpy
  - random
  - time
  - matplotlib

Python:
  - 3.5

Usage:
  - $python3 game_o_life <canvas_size:int>

Game-Of-Life Rules:

 1.
 Any live cell with fewer than two live neighbours
 dies, as if caused by under-population.
 2.
 Any live cell with two or three live neighbours lives
 on to the next generation.
 3.
 Any live cell with more than three live neighbours
 dies, as if by over-population.
 4.
 Any dead cell with exactly three live neighbours be-
 comes a live cell, as if by reproduction.
 """
import random
import sys

import numpy as np

from matplotlib import use as mpluse

#mpluse("TkAgg")
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap

usage_doc = "Usage of script: script_nama <size_of_canvas:int>"

choice = [0] * 100 + [1] * 10
random.shuffle(choice)


def create_canvas(size):
    canvas = [[False for i in range(size)] for j in range(size)]
    return canvas


def seed(canvas):
    for i, row in enumerate(canvas):
        for j, _ in enumerate(row):
            canvas[i][j] = bool(random.getrandbits(1))


def run(canvas):
    """This  function runs the rules of game through all points, and changes their status accordingly.(in the same canvas)
    @Args:
    --
    canvas : canvas of population to run the rules on.

    @returns:
    --
    None
    """
    canvas = np.array(canvas)
    next_gen_canvas = np.array(create_canvas(canvas.shape[0]))
    for r, row in enumerate(canvas):
        for c, pt in enumerate(row):
            # print(r-1,r+2,c-1,c+2)
            next_gen_canvas[r][c] = __judge_point(
                pt, canvas[r - 1 : r + 2, c - 1 : c + 2]
            )

    canvas = next_gen_canvas
    del next_gen_canvas  # cleaning memory as we move on.
    return canvas.tolist()


def __judge_point(pt, neighbours):
    dead = 0
    alive = 0
    # finding dead or alive neighbours count.
    for i in neighbours:
        for status in i:
            if status:
                alive += 1
            else:
                dead += 1

    # handling duplicate entry for focus pt.
    if pt:
        alive -= 1
    else:
        dead -= 1

    # running the rules of game here.
    state = pt
    if pt:
        if alive < 2:
            state = False
        elif alive == 2 or alive == 3:
            state = True
        elif alive > 3:
            state = False
    else:
        if alive == 3:
            state = True

    return state


if __name__ == "__main__":
    """
    if len(sys.argv) != 2:
        raise Exception(usage_doc)

    canvas_size = int(sys.argv[1])
    # main working structure of this module.
    """
    canvas_size=12
    c = create_canvas(canvas_size)
    seed(c)

    fig, ax = plt.subplots()
    fig.show()
    cmap = ListedColormap(["w", "k"])
    try:
        while True:
            c = run(c)
            ax.matshow(c, cmap=cmap)
            fig.canvas.draw()
            ax.cla()
    except KeyboardInterrupt:
        # do nothing.
        pass
```

<br>

[phasePortrait-python](https://github.com/phaseportrait/phaseportrait/blob/master/examples/examples.ipynb)<br><br><br>

[paper-reading](https://github.com/mli/paper-reading)<br>
ToLearn:<br>
[LearningWayOfEmbededSystem](https://github.com/SSHeRun/LearningWayOfEmbededSystem)<br>
[wifi-cracking](https://github.com/brannondorsey/wifi-cracking)<br>
[Two Dubious Ways to Solve A*X = X*B, part 1](https://blogs.mathworks.com/cleve/2020/10/09/two-dubious-ways-to-solve-ax-xb-part-1/)<br>
[陽明交通大學電機系物件導向程式設計](http://ocw.nctu.edu.tw/course_detail.php?bgid=8&gid=0&nid=343&page=4)<br>
[Eigen](https://eigen.tuxfamily.org/index.php?title=Main_Page)<br>
<br>
Javascript:<br>
[pac-man及其他](https://www.zhihu.com/answer/2263313024)<br>
[line-bot-chatgpt-api](https://github.com/Hans-Tsai/my-chatgpt/tree/main)<br>



