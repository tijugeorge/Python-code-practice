#compression algorithm

def compress_s(string):
    if len(string) == 0:
        return None
    final_arr = []
    index = 0
    letter = string[0]
    for let in string:
        if let == letter and ord(let) == ord(letter):
            index += 1
        else:
            final_arr.append(repr(index)+letter)
            letter = let
            index = 1
    final_arr.append(repr(index)+letter)
    #print final_arr
    return "".join(final_arr)

print compress_s('AAABBCCCCCCAAAAA')
