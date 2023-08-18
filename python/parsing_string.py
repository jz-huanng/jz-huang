
import re

response = """
思考過程：
根據陳述句，需要找到一句關於"馮端的主要研究方向是原子排列具有隨機性結構的晶體"的證據句。根據目前已經檢索到的文章內容，我們需要找到包含這個信息的句子。根據目前文章內容的描述，我們無法確定是否有相關的句子存在。

根據目前檢索的文章：
文章：馮端，男，原籍浙江紹興，生於江蘇蘇州，中國物理學家，中國科學院院士，主要研究領域爲固體物理學。

可以看出該文章提到了馮端的主要研究領域是固體物理學，但是對於原子排列具有隨機性結構的晶體的具體研究方向並未提及。

根據目前的情況，無法通過現有資訊判斷是否還需要進一步檢索其他文章。因此我們將輸出目前已檢索到的證據句，標籤為"Not enough info"，下一步不再進行檢索其他文章。

輸出結果：
evidence:馮端，男，原籍浙江紹興，生於江蘇蘇州，中國物理學家，中國科學院院士，主要研究領域爲固體物理學。
doc:None
state:finish 
"""

keywords = """
我們的陳述句是 "中國人馮端的主要研究方向是原子排列具有隨機性結構的晶體。"
keyword:馮端
"""


def getAction(response):
    PARSER_START = "evidence:"
    # find(f'"{self.generation_marker}"')
    start_parsing = response.find(f"{PARSER_START}")
    if (start_parsing != -1):
        reponse = response[start_parsing:]

    LABEL_START_MARKER = "label:"
    DOC_START_MARKER = "doc:"
    STATE_START_MARKER = "state:"

    label_start = response.find(LABEL_START_MARKER)
    doc_start = response.find(DOC_START_MARKER)
    state_start = response.find(STATE_START_MARKER)

    evidence = response[:label_start]
    evidence = evidence.split("evidence: ")[-1].strip()
    label = response[label_start:doc_start]
    label = re.split(r"label:\n*\t*\s*", label)[-1].strip()
    doc = response[doc_start:state_start]
    doc = re.split(r"doc:\"*\n*\t*\s*", doc)[-1].split("或")[0].strip()
    state = response[state_start:]

    state = re.split(r"state:\n*\t*\s*", state)[-1].split("\n")[0]

    return evidence, label, doc, state


def keywordParser(keywords):
    # \s | Matches whitespace characters, which include the \t, \n, \r, and space characters.
    PATTERN = re.compile(r"((K|k)eywords?\s*):?\s*\'*\"*")
    keyword = re.split(PATTERN, keywords)[-1]
    return keyword.strip()


keyword = keywordParser(keywords)
print(keyword)


evidence, label, doc, state = getAction(response)
print(f"evidence:{evidence}label: {label}\tdoc: {doc}\tstate: {state}")
