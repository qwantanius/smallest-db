import sqlite3,json,copy

user_tmp = dict({
  "tg_id": "NULL",
  "name": "NULL",
  "login": "NULL",
  "pwd": "NULL",
  "phone": "NULL",
  "status": "NULL",
  "passport_id": "NULL",
  "pesel_id": "NULL",
  "contract_starts_at": "NULL",
  "contract_ends_at": "NULL",
  "visa_created_at": "NULL",
  "visa_expires_at": "NULL",
  "vocation_start_at": "NULL",
  "vocation_ends_at": "NULL",
  "is_admin": "NULL",
  "is_on_vocation": "NULL",
  "is_vocation_allowed_by_admin": "NULL",
  "vocation_allowed_by_admin_starts_at": "NULL",
  "vocation_allowed_by_admin_ends_at": "NULL",
  "cadence_starts_at": "NULL",
  "cadence_ends_at": "NULL",
  "statements_data": []
})



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
SAVE_USER =   lambda su,tgid:SQL(INSERT_TMP.format(su,tgid))
GET_USER =    lambda tgid: SQL(SELECT_TMP.format(tgid))
GET_UTGID =   lambda fobj: fobj[0][1]
GET_UOBJ =    lambda fobj: DES(fobj[0][0])
UPDATE_USER = lambda u,tgid:SQL(UPDATE_TMP.format(u,tgid))
DELETE_USER = lambda tgid:SQL(DELETE_TMP.format(tgid))
DUMP =        lambda: SQL("select * from users")


def USER(u):
    _user = copy.deepcopy(user_tmp)
    _user.update(u)
    return _user

try:
    MIGRATE()
    COMMIT()
except:
    print("No migration needed")

