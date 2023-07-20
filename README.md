### langchain update and applications
[The problem of langchain](https://twitter.com/minimaxir/status/1677773088484909057?t=jltI8bmUWFoCZ_Y5Jq2dkw&s=19)<br>
<br>
[multiRetrievalQAChain](https://twitter.com/cristobal_dev/status/1678414640055742468?t=NUffRBJcwspavx_SosgnrQ&s=19)<br>

### jax
```
import jax.numpy as jnp
from jax import grad,vmap,jit

def predict(params,inputs):
  for w,b in params:
    outputs=jnp.dot(inputs,w)+b
    ouputs=jnp.tanh(outputs)
  return outputs

def loss(params,batch):
  inputs,targets=batch
  preds=predict(params,inputs)
  return(jnp.sum(preds-targets)**2)

gradient=jit(grad(loss))#loss.backward(),caculate gradient and release computational graph)
perexample_grads=jit(vmap(grad(loss),in_axes=(None,0)))

```
