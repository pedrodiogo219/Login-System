from app import conn
from sqlalchemy.sql import select
from random import randint

def pesquisa_primeiros(Tab):
    #SELECT column_name FROM information_schema.columns WHERE TABLE_NAME = 'loja'

    s = select([Tab]).limit(10)
    result = conn.execute(s)
    return result


def shufflecards():
    x = randint(1, 8)
    if x == 1:
        return "card text-white bg-primary mb-3"
    if x == 2:
        return "card text-white bg-secondary mb-3"
    if x == 3:
        return "card text-white bg-success mb-3"
    if x == 4:
        return "card text-white bg-danger mb-3"
    if x == 5:
        return "card text-white bg-warning mb-3"
    if x == 6:
        return "card text-white bg-info mb-3"
    if x == 7:
        return "card bg-light mb-3"
    if x == 8:
        return "card text-white bg-dark mb-3"

    return "card bg-light mb-3"