class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_logged_in(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == False:
            print("Not logged in, Canceling")
        else:
            print("Logged in, proceeding")
            function(args[0])
    return wrapper

@is_logged_in
def create_post(user):
    print("Creating post")

new_user = User("John")
new_user.is_logged_in = True
create_post(new_user)