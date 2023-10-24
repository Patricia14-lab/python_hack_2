"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(result):
    
    largo = len(result)
    result = result.replace('a','@').replace('e','3').replace('i','¡').replace('o','0').replace('u','v')
    result = result.capitalize()
    if largo == 2 and result [-1:] =="v":
        result = result [:largo-1] + result [-1:]  
    else:
        result = result [:largo-1] + result [-1:].upper()
    return result

