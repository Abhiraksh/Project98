def SwapData():
    source = input("Enter the source file:")
    destination = input("Enter the destination file:")
    with open(source, "r") as a:
        data_a = a.read()
    with open(destination, "r") as b:
        data_b = b.read()
    with open(source, "w") as a:
        a.write(data_b)
    with open(destination, "w") as b:
        b.write(data_a)     

SwapData()

