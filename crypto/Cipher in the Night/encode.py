string1="buetctf{key_to_unlock_the_shaded_truth_skeletons}"
string2="W"*100
result = [chr(ord(a) ^ ord(b)) for a,b in zip(string1, string2)]
print(''.join(result))