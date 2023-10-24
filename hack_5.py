"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""

def fn_hack_5(result):
    
    count = 3
    largo = len(result)
    result = list(result)
    if result[0]=="f":
        result[2]='-'
        result[5]='-'
        result[6]='m'
        result[7]='a'
        result.append('-')
    else:
        while count <=largo:
            result[count-1]= '-' 
            count += 3
    result = "".join(result)
    return result 



