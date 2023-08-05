


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

### cplusplus

0723,0728<br>
```
class Solution{
pubilc:
  int getImportance(vector<Employee*> employees,int id){
    unorder_map<int,Employee*> es;
    for (auto& e:employees){
      es.emplace(e->id,e);
    }

    return dfs(id,es);
  }
private:
  int dfs(int id,const unorder_map<int,Employee*>& es){
    const auto e=es.at(id);
    int sum=e->importance;
    for(auto& rid:e->subordinates){
      sum+=dfs(rid,es);
    }
    return sum;
  }
}

```
<br>

```
class Solution{
pubilc:
  int getImportance(vector<Employee*> employees,int id){
    unorder_map<int,Employee*> es;
    for (auto& e:employees){
      es.emplace(e->id,e);
    }

  }
}
```

ToLearn:<br>
[LearningWayOfEmbededSystem](https://github.com/SSHeRun/LearningWayOfEmbededSystem)<br>
[wifi-cracking](https://github.com/brannondorsey/wifi-cracking)<br>

<br>
Javascript:<br>
[pac-man及其他](https://www.zhihu.com/answer/2263313024)<br>
[line-bot-chatgpt-api](https://github.com/Hans-Tsai/my-chatgpt/tree/main)<br>



