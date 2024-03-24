<<<<<<< HEAD
class UserFactory:
    @staticmethod 
    def create_user(parser: UserInputParser) -> User:
        username = parser.parse("Enter a username: ")
        password = parser.parse("Enter a password: ")
        # Here you can add more logic as needed, e.g., validate input
        return User(parser, username=username, password=password)
=======
>>>>>>> 4be701d8b246c6138b13163a2276fbe97ec890a5
