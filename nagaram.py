# my method
def dic_ana(pork, monkey):
    dic = {}
    sor_p = "".join(sorted(pork.replace(" ", "").lower()))
    sor_m = "".join(sorted(monkey.replace(" ", "").lower()))
    dic[sor_p] = sor_m
    dic[sor_m] = sor_p
    return dic[sor_p] == dic[sor_m]

# solution
def freq_ana(pork, monkey):
    freq_table = {}
    for i in pork:
        if i in freq_table:
            freq_table[i] += 1
        else:
            freq_table[i] = 1
    
    for i in monkey:
        if i not in freq_table:
            return False
        else:
            freq_table[i] -= 1
            if freq_table[i] < 0:
                return False

    for key, value in freq_table.items():
        if value != 0:
            return False

    return True

pork = "Red Rum"
monkey = "Murder"
print(dic_ana(pork, monkey))