import uuid


class CreateUser:
    def __init__(self, user_form) -> None:
        self.user_form = user_form
        self.user_id = uuid.uuid1()
        self.formated_birthday = Format_barthday(user_form.birthday)

    def get_created_user(self) -> User:
        user: User = User()
        user.code = self.user_id
        user.name = self.user_form.name
        user.cpf = self.user_form.cpf
        user.birthday = self.formated_birthday
        return user
