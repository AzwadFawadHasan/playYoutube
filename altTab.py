import msvcrt
while True:
    char = char = msvcrt.getch()
    if char == b"\r":
        print("yay")
    else:
        print("nope")