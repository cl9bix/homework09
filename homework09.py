contacts = {}


def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Not enough params. Print help"
    return inner


@input_error
def add_contact(name, phone_number):
    contacts[name] = phone_number


def phone(name):
    if name in contacts:
        return f'Phone number for user {name}: {contacts[name]}'
    else:
        return f'Contact with name: {name} is not found!'


def change(name, new_phone_number):
    if name in contacts:
        contacts[name] = new_phone_number
        return f'Phone number for user {name} is changed to {new_phone_number}.'
    else:
        return f'User with name: {name} is not found!'


def showall():
    result = 'List of all contacts:\n'
    for name, phone_number in contacts.items():
        result += f'{name}: {phone_number}\n'
    return result


def hello(*args):
    return 'How can I help you?'


def exit(*args):
    return 'Goodbye!'


def no_command(*args):
    return 'Unknown command, try again!'


COMMANDS = {hello: 'hello',
            add_contact: 'add',
            change: 'change',
            phone: 'phone',
            showall: 'show all',
            exit: 'goodbye',
            exit: 'close',
            exit: 'exit'
            }


def command_handler(text):
    for command, kword in COMMANDS.items():
        if text.startswith(kword):
            return command, text.replace(kword, '').strip()
    return no_command, None


def main():
    while True:
        user_input = input('>>>')
        command, data = command_handler(user_input)
        if command == exit:
            print(command())
            break
        elif command == no_command:
            print(command())
        elif data is not None:
            result = command(*data.split())
            if result:
                print(result)
        else:
            result = command()
            if result:
                print(result)


if __name__ == '__main__':
    main()
