import sqlite3,json

#БАЗОВЫЕ ПРОЦЕДУРЫ И КОНФИГУРАЦИЯ
INSERT_TMP = """insert into users values('{}', '{}');"""
SELECT_TMP = """select * from users where users.tg_id={}"""
UPDATE_TMP = """update users SET json_dump='{}' where users.tg_id='{}'"""
DELETE_TMP = """delete from users where tg_id='{}'"""
TABLE_SCH  = "create table users (json_dump text, tg_id text)"
DATABASE =    sqlite3.connect("database.db")
CURSOR =      DATABASE.cursor()
SQL =         lambda text:CURSOR.execute(str(text))
FETCH =       lambda:CURSOR.fetchall()
SER =         lambda user:json.dumps(user)
DES =         lambda user:json.loads(user)
MIGRATE =     lambda:SQL(TABLE_SCH)
COMMIT =      lambda:DATABASE.commit()
SAVE_USER =   lambda tgid,u:SQL(INSERT_TMP.format(u,tgid))
GET_USER =    lambda tgid: SQL(SELECT_TMP.format(tgid))
GET_UTGID =   lambda fobj: fobj[0][1]
GET_UOBJ =    lambda fobj: DES(fobj[0][0])
UPDATE_USER = lambda tgid,u:SQL(UPDATE_TMP.format(u,tgid))
DELETE_USER = lambda tgid:SQL(DELETE_TMP.format(tgid))
DUMP =        lambda: SQL("select * from users")


