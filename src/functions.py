def multiple_returns():
    val_v1 = "Python"

    if not val_v1:
        return 0

    match val_v1:
        case "Hello":
            print("Do logic v1")
            return 1
        case "world":
            return
        case _:
            print("Do uniform logic")


multiple_returns()