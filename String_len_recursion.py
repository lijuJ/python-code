def length_of_string(str):
    if str == "":
        return 0
    return 1 + length_of_string(str[1:])


str = "PrepInsta"
print("length of", str, "is", length_of_string(str))