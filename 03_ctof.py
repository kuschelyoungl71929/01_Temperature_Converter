def to_f(from_c): 
    fahr = (from_c * 9/5) + 32
    return fahr


temperatures = [0, 40, 100]
converted = []

for item in temperatures:
    answer = to_f(item)
    ans_statement = "{} degrees C is {} degrees F".format(item, answer)
    converted.append(ans_statement)

print(converted)