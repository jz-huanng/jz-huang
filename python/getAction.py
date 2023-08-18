

import re


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
    label = re.split(r"label:\t*\s*", label)[-1].strip()
    doc = response[doc_start:state_start]
    doc = re.split(r"doc:\t*\s*", doc)[-1].strip()
    state = response[state_start:]
    state = re.split(r"state:\t*\s*", state)[-1].strip()

    return evidence, label, doc, state


response = """
思考過程:

1. 從文章中找出與陳述句相關的句子作為(補充的)證據句。

在文章中找到了與陳述句相關的句子，特別是提到藤子·F·不二雄（藤本弘）是藤本弘單飛後的作者名稱。

陳述句: 藤子·F·不二雄是藤本弘單飛後的作者名稱。
證據句: 後兩人於1987年正式分拆筆名，其中藤本弘稱爲「藤子不二雄Ⓕ」，F即其本名姓氏開頭首字母，1989年2月，經過藤本友人石之森章太郎先生的建議，將筆名改爲「藤子·F·不二雄」。

2. 檢查每一個觀念是否有在證據句中提及。

觀念1: 藤子·F·不二雄是藤本弘單飛後的作者名稱。 
在證據句中有提及：「後兩人於1987年正式分拆筆名，其中藤本弘稱爲『藤子不二雄Ⓕ』，F即其本名姓氏開頭首字母，1989年2月，經過藤本友人石之森章太郎先生的建議，將筆名改爲『藤子·F·不二雄』。」

綜合以上證據句可以得出結論：藤子·F·不二雄是藤本弘單飛後的作者名稱。

狀態：finish

最後整理答案:

evidence: 後兩人於1987年正式分拆筆名，其中藤本弘稱爲「藤子不二雄Ⓕ」，F即其本名姓氏開頭首字母，1989年2月，經過藤本友人石之森章太郎先生的建議，將筆名改爲「藤子·F·不二雄」。
label:        None    
doc:None
state: finish
"""

evidence, label, doc, state = getAction(response)
print(f"evidence:{evidence}\nlabel:{label}\tdoc:{doc}\tstate:{state}")
