def get_frutis_name(data:str)->list:
    """
    This function returns the names of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        list: list of fruits names
    """
    from csv import reader 
    f=reader(data)
    c=0
    for i in f:
        if c==0:
            c+=1
            continue
        print(i[0])
f=open("fruits.csv")
get_frutis_name(f)

    