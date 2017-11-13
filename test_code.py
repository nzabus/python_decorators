
'''
def decorator_fct(original_fct):
    def wrapper_fct():
        print("run this decorator exta code before running {}".format(original_fct.__name__))
        return original_fct()
    return wrapper_fct


@decorator_fct
def display():
    print("display function ran")


display()

'''

def decorator (fcnt):
    def wrapper(*args, **kwargs):
        print("Doing something before")
        return fcnt(*args, **kwargs)
    return wrapper


@decorator
def original_fcnt():
    print("{}".format("This is original fonction"))

@decorator
def another_fcnt(nom, age):
    print("calling function with arguments name: {} and age: {}".format( nom, age))

original_fcnt()

another_fcnt("Landry NZabus", 50)