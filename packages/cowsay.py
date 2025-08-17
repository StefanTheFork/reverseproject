#cowsay v1 :fire:
def say(args=None):
    # if there aint no argument or its blank say moooooo
    if args is None or (len(args) == 1 and args[0].strip() == ""):
        print("the cow doesnt have a message to say...")
        message = "moo"
        length = len(message)
    else:
        message = ' '.join(args)
        length = len(message)

    print(' ' + '_' * (length + 2))
    print(f'< {message} >')
    print(' ' + '-' * (length + 2))
    print(r'''
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
                ''')
