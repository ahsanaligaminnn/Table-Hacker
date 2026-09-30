print("------------------")
print("|  Table Hacker  |")
print("------------------\n")

while True:
    table = input("Enter Table Value : ")

    if table == "0":
        break

    elif not table.isdigit():
        print("Invalid Command.\n")

    else:
        table = int(table) 
        start = int(input("Enter Table Start Number : "))
        end = int(input("Enter Table End Number : "))

        print()
        print("--------------------------")
        print("+  Choose Table Catogry  +")
        print("--------------------------\n")

        print("1. Normal")
        print("2. Even")
        print("3. Odd\n")

        user = input("Enter Press (1-3) : ")
        print()

        if user == "1":
            print("__________________________")
            print("|  Table Catogry Normal  |")
            print("__________________________\n")

            for i in range(start,end+1):
                print(f"{table} x {i} = {table*i}\n")

        elif user == "2":
            print("________________________")
            print("|  Table Catogry Even  |")
            print("________________________\n")

            for i in range(start,end+1):
                even = table*i
                if even %2==0:
                    print(f"{table} x {i} = {even}\n")
            else:
                print("Not Found Even Numbers.\n") 

        elif user =="3":
            print("_______________________")
            print("|  Table Catogry Odd  |")
            print("_______________________\n")

            for i in range(start,end+1):
                odd = table*i
                if odd %2!=0:
                    print(f"{table} x {i} = {odd}\n")
            else:       
                print("Not Found Odd Numbers.\n") 

        else:
            print("Invalid Command.\n")                 
    



           
