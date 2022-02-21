all_calculations = []


get_item = ""
while get_item != "xxx":
    get_item = input("Enter an item: ")

    if get_item == "xxx":
        break

all_calculations.append(get_item)


print()

if len(all_calculations) == 0:
    print("Make a conversion first!")

else:

    print()
    print("Full History")
    print(all_calculations)

    if len(all_calculations) >= 3:
        print("Recent History")
        for item in range(0,3):
            print(all_calculations[len(all_calculations) - item - 1])
