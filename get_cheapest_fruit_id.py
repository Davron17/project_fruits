def get_cheapest_fruit_id(data: str) -> int:
    """
        This function returns the index of the cheapest fruit

    args:
        data (str): CSV file with the fruits data
    returns:
        int: id of the cheapest fruit
    """
    # your code here
    from csv import reader 
    f=reader(data)
    mx = -24545446
    c =0
    for i in f:
        c+=1
        if i[0]=="name":
            continue
        if mx<float(i[1]):
            s=c
            mx = float(i[1])
    print(s)
f=open("fruits.csv")
get_cheapest_fruit_id(f)