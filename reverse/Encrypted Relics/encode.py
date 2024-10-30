import marshal

def execute():
    hex_string = "0374760553f6a6a5646787d367f38636471677f2d6f636e25626574757f697e2777777f2f2a33707474786"
    reversed_bytes = bytearray.fromhex(hex_string[::-1]).decode()
    
    part1 = "XkT9p"
    part2 = "3t_f"
    part3 = "p@ck"
    hex_code = '7069636b6c6564'
    part4 = "1l3"
    prefix = bytearray.fromhex('6e30785f').decode()

    mod1 = "an2u"
    mod2 = "va"
    modified_string = ""

    for char in mod1 + mod2:
        modified_string += chr(ord(char) - 2)

    combined = part1 + part3 + part2 + part4
    encoded_string = ""

    for char in combined:
        encoded_string += chr(ord(char) + 5)

    password = input("Enter Relics: ")
    
    if password == encoded_string[::-1][1:]:
        secret = "n3v@h"
        result = f"{prefix}{secret[::-1]}{modified_string}{bytearray.fromhex(hex_code).decode()}_{part3}{part2}{part4}_{encoded_string[::-1][:7]}"
        print(result)
    else:
        print("You missed it man!")

with open('enc.nocap', 'wb') as file_handle:
    file_handle.write(marshal.dumps(execute.__code__))

with open("enc.nocap", "rb") as file_handle:
    content = file_handle.read()
    
with open('enc.nocap', 'wb') as file_handle:
    file_handle.write(marshal.dumps(content))