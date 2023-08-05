




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



