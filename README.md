### TODO introduce langchain LLM intergted framework in notebook

### langchain update and applications
[The problem of langchain](https://twitter.com/minimaxir/status/1677773088484909057?t=jltI8bmUWFoCZ_Y5Jq2dkw&s=19)<br>
<br>
[multiRetrievalQAChain](https://twitter.com/cristobal_dev/status/1678414640055742468?t=NUffRBJcwspavx_SosgnrQ&s=19)<br>


### self-deiving car
- car and controller
- road
- sensor
- collision
- neural network
- genetic algorithm


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

### python

```
def call(func):
  return func()

def add(x,y):
  return x+y

call(add,3,4)

```

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

### langchain application-chain,agent
[Video tutorial link](https://www.youtube.com/watch?v=PJcGkI1m9jQ&list=LL&index=11&t=21s)<br>
[github reppos](https://github.com/databricks-academy/large-language-models/tree/published)
```
# Okay now that's ready we need to make the randomized sentiment
random_sentiment = "nice"
if np.random.rand() < 0.3:
    random_sentiment = "mean"
# We'll also need our social media post:
social_post = "I can't believe I'm learning about LangChain in this MOOC, there is so much to learn and so far the instructors have been so helpful. I'm having a lot of fun learning! #AI #Databricks"

model_id = "EleutherAI/gpt-neo-2.7B"
tokenizer = AutoTokenizer.from_pretrained(model_id, cache_dir=DA.paths.datasets)
model = AutoModelForCausalLM.from_pretrained(model_id, cache_dir=DA.paths.datasets)
pipe = pipeline(
    "text-generation", model=model, tokenizer=tokenizer, max_new_tokens=512, device_map='auto'
)
jekyll_llm = HuggingFacePipeline(pipeline=pipe)

#with output key
jekyll_chain = LLMChain(
    llm=jekyll_llm,
    prompt=jekyll_prompt_template,
    output_key="jekyll_said",
    verbose=False,
)  # Now that we've chained the LLM and prompt, the output of the formatted prompt will pass directly to the LLM.

# To run our chain we use the .run() command and input our variables as a dict
jekyll_said = jekyll_chain.run(
    {"sentiment": random_sentiment, "social_post": social_post}
)

#SequentialChain
jekyllhyde_chain = SequentialChain(
    chains=[jekyll_chain, hyde_chain],
    input_variables=["sentiment", "social_post"],
    verbose=True,
)

# We can now run the chain with our randomized sentiment, and the social post!
jekyllhyde_chain.run({"sentiment": random_sentiment, "social_post": social_post})

#ZERO_SHOT_REACT_DESCRIPTION
# For DaScie we need to load in some tools for it to use, as well as an LLM for the brain/reasoning
from langchain.agents import load_tools  # This will allow us to load tools we need
from langchain.agents import initialize_agent
from langchain.agents import (
    AgentType,
)  # We will be using the type: ZERO_SHOT_REACT_DESCRIPTION which is standard
from langchain.llms import OpenAI

# For OpenAI we'll use the default model for DaScie
llm = OpenAI()
tools = load_tools(["wikipedia", "serpapi", "python_repl", "terminal"], llm=llm)
# We now create DaScie using the "initialize_agent" command.
dascie = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

dascie.run(
    "Create a dataset (DO NOT try to download one, you MUST create one based on what you find) on the performance of the Mercedes AMG F1 team in 2020 and do some analysis. You need to plot your results."
)

# Let's try to improve on these results with a more detailed prompt.
dascie.run(
    "Create a detailed dataset (DO NOT try to download one, you MUST create one based on what you find) on the performance of each driver in the Mercedes AMG F1 team in 2020 and do some analysis with at least 3 plots, use a subplot for each graph so they can be shown at the same time, use seaborn to plot the graphs."
)

```

<br>

### creat_pandas_dataframe_agent
```
from langchain.agents import create_pandas_dataframe_agent
import pandas as pd

datasci_data_df = pd.read_csv(f"{DA.paths.datasets}/salaries/ds_salaries.csv")
# world_data
dascie = create_pandas_dataframe_agent(
    OpenAI(temperature=0), datasci_data_df, verbose=True
)

# COMMAND ----------

# Let's see how well DaScie does on a simple request.
dascie.run("Analyze this data, tell me any interesting trends. Make some pretty plots.")

# COMMAND ----------

# Not bad! Now for something even more complex.... can we get out LLM model do some ML!?
dascie.run(
    "Train a random forest regressor to predict salary using the most important features. Show me the what variables are most influential to this model"
)
```

<br>
Use huggingface:

```
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader

# We have some fake laptop reviews that we can load in
file_path=""
loader = TextLoader(
    file_path, encoding="utf8"
)
document = loader.load()

from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

# First we split the data into manageable chunks to store as vectors. There isn't an exact way to do this, more chunks means more detailed context, but will increase the size of our vectorstore.
text_splitter = CharacterTextSplitter(chunk_size=250, chunk_overlap=10)
texts = text_splitter.split_documents(document)
# Now we'll create embeddings for our document so we can store it in a vector store and feed the data into an LLM. We'll use the sentence-transformers model for out embeddings. https://www.sbert.net/docs/pretrained_models.html#sentence-embedding-models/
model_name = "sentence-transformers/all-MiniLM-L6-v2"
embeddings = HuggingFaceEmbeddings(
    model_name=model_name, cache_folder=DA.paths.datasets
)  # Use a pre-cached model
# Finally we make our Index using chromadb and the embeddings LLM
chromadb_index = Chroma.from_documents(
    texts, embeddings, persist_directory=DA.paths.working_dir
)

from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline

# We want to make this a retriever, so we need to convert our index.  This will create a wrapper around the functionality of our vector database so we can search for similar documents/chunks in the vectorstore and retrieve the results:
retriever = chromadb_index.as_retriever()
hf_llm = HuggingFacePipeline.from_model_id(
    model_id="google/flan-t5-large",
    task="text2text-generation",
    model_kwargs={
        "temperature": 0,
        "max_length": 128,
        "cache_dir": DA.paths.datasets,
    },
)

chain_type = "stuff"  # Options: stuff, map_reduce, refine, map_rerank
laptop_qa = RetrievalQA.from_chain_type(
    llm=hf_llm, chain_type="stuff", retriever=retriever
)

laptop_name = laptop_qa.run("What is the full name of the laptop?")


```

```
from langchain.document_loaders import GutenbergLoader

loader = GutenbergLoader(
    "https://www.gutenberg.org/cache/epub/100/pg100.txt"
)  # Complete works of Shakespeare in a txt file

all_shakespeare_text = loader.load()

```
