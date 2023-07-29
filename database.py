import psycopg2

from models import *

conn = psycopg2.connect(
    database="jkemfsse",
    user='jkemfsse',
    password='fLURKFlMm5ZTztSNkC7oGKnh2wQvnRha',
    host='drona.db.elephantsql.com',
)


conn.autocommit = True

cur = conn.cursor()



def fetchUsers(query:str) -> User:
    cur.execute(query=query)
    return cur.fetchall()