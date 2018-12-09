from app import conn
from sqlalchemy.sql import select


def pesquisa_primeiros(Tab):
    #SELECT column_name FROM information_schema.columns WHERE TABLE_NAME = 'loja'

    s = select([Tab]).limit(10)
    result = conn.execute(s)
    return result