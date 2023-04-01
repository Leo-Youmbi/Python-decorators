def say(func):
    def employer():
        print("Say something about you.")

    def say_name():
        print("My name is Youmbi Leo.")

    def say_nationality():
        print("I am from Cameroon.")

    def wrapper():
        employer()
        say_name()
        say_nationality()
        func()

    return wrapper


@say
def start_interview():
    print("Real interview Started...")


start_interview()
