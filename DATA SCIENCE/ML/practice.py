lst='YES'
while lst=='YES':
    try:
        user=input("Enter the color on signal:")
        clear=user.replace(" ","").lower()
        print(clear)
        if not clear.isalpha():
            raise ValueError("Invalid input. Only alphabets allowed.")
    except ValueError as e:
            print(e)
    else:
        match clear :
            case 'red':
                 print('stop')
            case 'green':
                    print('Goo')
            case 'yellow':
                 print('see here and there and go')
            case __:
                    print('no such color in present traffic light.')
        lst=input('if you want try again(YES/NO):').upper()
    finally:
     print('Thanks for using this program')

