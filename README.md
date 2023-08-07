
```
A=random.rand(3,5)

from numpy.dual import svd;U,sVh=svd(A)

r=min(*A.shape);Sig=zeros_like(A)
Sig[:r,:r]=diag(s);print Sig

```
```
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



