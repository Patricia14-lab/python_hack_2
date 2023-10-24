"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""


def fn_hack_1(result):

    largo = len(result)
    if largo >= 5:
            result = result[0]+result[1].upper()+result[2:4]+result[4].upper()+result[5:]
    if largo == 3:
        result = result[0]+result[1].upper()+result[2:]
    return result 



