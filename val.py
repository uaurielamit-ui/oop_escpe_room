def val_int(text):
    legal = False
    while not legal:
        try:
            client_choice = int(input(text))
            if client_choice >0:
                legal = True
        except ValueError:
            print("only positiv numbers ")
    return client_choice

def val_str(text):
    legal = False
    while not legal:
        client_choice = input(text).strip()
        if client_choice != "":
            legal = True
        else:
            print("enter a text")
    return client_choice