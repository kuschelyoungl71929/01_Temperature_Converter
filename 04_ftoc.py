def to_c(from_f):
    cels = (from_f - 32) * 5/9 
    return cels


temperatures = [0, 40, 100]
converted = []

for item in temperatures:
    answer = to_c(item)
    ans_statement = "{} degrees F is {} degrees C".format(item, answer)
    converted.append(ans_statement)

print(converted)