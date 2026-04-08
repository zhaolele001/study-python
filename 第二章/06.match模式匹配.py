day = input("请输入（1-7）")

match day:
    case "1":
        print("1")
    case "2":
        print("2")
    case "3" | "4" | "5" | "6" | "7" if day!=0:
        print("7")
    case _:
        print("其他")
