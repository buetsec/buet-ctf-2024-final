string1='5"2#4#1,<2.#8"9;84<#?2$?6323#%"#?$<2;2#89$*'
string2="W"*100
result = [chr(ord(a) ^ ord(b)) for a,b in zip(string1, string2)]
print(''.join(result))