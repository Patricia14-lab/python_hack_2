"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""

def fn_hack_9(result):  
    result.pop("bar",None)
    result = {k.capitalize(): v.capitalize() for k, v in result.items()}
    for i in result:
        result[i] = result[i].replace("k", "")
    return result
