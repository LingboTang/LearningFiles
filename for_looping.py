def change_list(arr):
    for i in range(len(arr)):
        if i < 5:
            pass
        else:
            arr[i][1] = str(int(arr[i][1]) * 2)
    return arr

array = [["afkj","12","234"],["adfa","2342", "slal"],["asd1fv","512", "sfjz"],["skgej", "928", "asdfjk"],["adfl","910", "adfjaksdf"]]
brray = map(list,array*2)
print(brray)
print(change_list(brray))
