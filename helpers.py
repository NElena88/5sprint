from faker import Faker

faker = Faker()

def generate_registration_account():
    login = faker.random_int(min=100, max=999)
    email = f"{login}@ya.ru"
    password = faker.password(length=6, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return email, password  # Возвращаем кортеж (email, password)