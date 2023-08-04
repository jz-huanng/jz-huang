


```
y_list.append(x_list)

def compute_neighbours(Z):
    shape = len(Z), len(Z[0])
    N  = [[0,]*(shape[0]) for i in range(shape[1])]
    for x in range(1,shape[0]-1):
        for y in range(1,shape[1]-1):
            N[x][y] = Z[x-1][y-1]+Z[x][y-1]+Z[x+1][y-1] \
                    + Z[x-1][y]            +Z[x+1][y]   \
                    + Z[x-1][y+1]+Z[x][y+1]+Z[x+1][y+1]
    return N

def iterate(Z):
    N = compute_neighbours(Z)
    for x in range(1,shape[0]-1):
        for y in range(1,shape[1]-1):
             if Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3):
                 Z[x][y] = 0
             elif Z[x][y] == 0 and N[x][y] == 3:
                 Z[x][y] = 1
    return Z

---

N = np.zeros(Z.shape, dtype=int)
N[1:-1,1:-1] += (Z[ :-2, :-2] + Z[ :-2,1:-1] + Z[ :-2,2:] +
                 Z[1:-1, :-2]                + Z[1:-1,2:] +
                 Z[2:  , :-2] + Z[2:  ,1:-1] + Z[2:  ,2:])

# Flatten arrays
N_ = N.ravel()
Z_ = Z.ravel()

# Apply rules
R1 = np.argwhere( (Z_==1) & (N_ < 2) )
R2 = np.argwhere( (Z_==1) & (N_ > 3) )
R3 = np.argwhere( (Z_==1) & ((N_==2) | (N_==3)) )
R4 = np.argwhere( (Z_==0) & (N_==3) )

# Set new values
Z_[R1] = 0
Z_[R2] = 0
Z_[R3] = Z_[R3]
Z_[R4] = 1

# Make sure borders stay null
Z[0,:] = Z[-1,:] = Z[:,0] = Z[:,-1] = 0

Even if this first version does not use nested loops, it is far from optimal because of the use of the four argwhere calls that may be quite slow. We can instead factorize the rules into cells that will survive (stay at 1) and cells that will give birth. For doing this, we can take advantage of Numpy boolean capability and write quite naturally:

birth = (N==3)[1:-1,1:-1] & (Z[1:-1,1:-1]==0)
survive = ((N==2) | (N==3))[1:-1,1:-1] & (Z[1:-1,1:-1]==1)
Z[...] = 0
Z[1:-1,1:-1][birth | survive] = 1
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



