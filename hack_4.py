"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""
def fn_hack_4(result):

    largo = len (result)
    if largo > 3:
        result = list(result)
        del result[largo-1]
        del result[0]
        result = "".join(result)
    return result


