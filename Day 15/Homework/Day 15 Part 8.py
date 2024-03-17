
user_name = str(input("Please input a string: "))
while True:

        if len(user_name) > 0:
            (last_character) = user_name[-1]
            print (str(last_character))
            break

        else:
            print("Please input a correct variable! ")