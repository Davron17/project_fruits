def get_cheapest_fruit(data: str) -> str:
    """
    This function returns the name of the cheapest fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the cheapest fruit
    """
    # your code here
    from csv import reader 
    f=reader(data)
    mx = 35415665
    c =0
    for i in f:
        c+=1
        if i[0]=="name":
            continue
        if mx>float(i[1]):
            mx = float(i[1])
    print(mx)
f=open("fruits.csv")
get_cheapest_fruit(f)