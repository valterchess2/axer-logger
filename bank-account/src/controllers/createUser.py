from datetime import date
from utils.exceptions.userInvalidException import UserInvalidException
from entities.userEntity import UserEntity

class CreateUser:
    def __init__(self, user_form) -> None:
        self.user_form: str = user_form
        self.date_format: DateFormat = DateFormat(user_form.birthday)
        self.verify_user = VerifyUser(self.user_form)
        self.user_repository = UserRepository()

    def get_created_user(self) -> UserEntity:
        user: UserEntity = UserEntity()
        user.code = self.user_id
        user.name = self.user_form.name
        user.cpf = self.user_form.cpf
        user.birthday: date = self.date_format.get_birthDay()
        # verify if user exists in dataBase
        if self.verify_user.is_valid():
            self.user_repository.insert(user)
            return user
        else:
            raise UserInvalidException("User is already registered")

