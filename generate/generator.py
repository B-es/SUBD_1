from faker import Faker
from random import randint, choice, choices

faker = Faker(locale="ru_RU")

def create_users(count:int):
    result = []
    for _ in range(count):
        name = faker.unique.first_name()
        surname = faker.unique.last_name()
        age = randint(14, 70)
        email = faker.unique.email()
        password = faker.unique.password()
        result.append({
            "name":name,
            "surname":surname,
            "age":age,
            "email":email,
            "password":password,
            })
    return result

def create_messages(count:int):
    result = []
    for _ in range(count):
        message = faker.text()
        date = faker.date()
        result.append({
                "message":message,
                "date":date,
                })
    return result

def create_chats(count:int, userIds:list, messageIds:list):
    result = []
    for _ in range(count):
        userId1 = choice(userIds)
        userId2 = choice(userIds)
        part_messageIds = choices(messageIds, k=4)
        result.append({
                "userId1":userId1,
                "userId2":userId2,
                "messages":part_messageIds,
                })
    return result

def get_random_chats(count:int, chatIds:list):
    result = []
    for _ in range(count):
        part_chatIds = choices(chatIds, k=4)
        result.append(part_chatIds)
    return result