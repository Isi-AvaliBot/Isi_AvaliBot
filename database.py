import sqlite3
from sqlite3 import Error
import ezconf as ez

c = ez.config()
c.read('month_data.json')
print('Loaded servers:',c.get('servers'))
c.save()

# Создать соединение к дб 
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file, check_same_thread=False)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            return conn

# создать таблицу, используя соединение с этим именем
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

'''
данные таблиц для серверов, сообщений и данных бота

Таблица серверов содержит информацию об имени сервера, владельце, размере сервера и ссылку на таблицу, содержащую статистику сообщений.

Таблица сообщений содержит информацию о статистике и наиболее часто используемых командах.
'''

servers_table="""
CREATE TABLE IF NOT EXISTS servers (
    id integer PRIMARY KEY,
    name text NOT NULL,
    server_id int,
    owner int,
    users int
); 
"""

messages_table="""
CREATE TABLE IF NOT EXISTS msgs (
    id integer PRIMARY KEY,
    server_id int,
    all_time int,
    monthly int,
    daily int,
    total int,
    cur_day int,
    cur_month int,
    diff int,
    past_diff int
); 
"""
# создать соединение
conn = create_connection("main.db")
if conn is not None:
    # создать таблицу
    create_table(conn, servers_table)
    create_table(conn, messages_table)
    print('Connection established, ready for take off!')
else:
    # если не удается подключиться к базе данных, умереть
    print("Error! cannot create the database connection.")
    quit()

def get_all_servers():
  cur = conn.cursor()
  cur.execute("SELECT * FROM msgs")
  servers = cur.fetchall()
  x = []
  for lserver in servers:
    x.append(server(lserver[1]))
  return x

class server:

  def __init__(self,id,server=None):
    self.id = id
    self.conn = conn
    self.server = server
    if server == None:
      self.name = self.get_name()
      self.diff = self.get_diff()
    self.usage = {
      'monthly':self.get_monthly(self.conn,id),
      'daily':self.get_daily(self.conn,id),
      'total':self.get_total(self.conn,id)
    }
    print(f'Server ({self.id}) has finished loading...')

  def get_monthly(self,conn,id):
    cur = conn.cursor()
    cur.execute(str("SELECT monthly FROM msgs WHERE server_id ="+str(id)))
    monthly = cur.fetchone()
    return monthly
  
  def get_daily(self,conn,id):
    cur = conn.cursor()
    cur.execute(str("SELECT daily FROM msgs WHERE server_id ="+str(id)))
    daily = cur.fetchone()
    return daily
  
  def get_total(self,conn,id):
    cur = conn.cursor()
    cur.execute(str("SELECT total FROM msgs WHERE server_id ="+str(id)))
    total = cur.fetchone()
    return total
  
  def get_diff(self):
    cur = self.conn.cursor()
    cur.execute(str("SELECT diff FROM msgs WHERE server_id ="+str(self.id)))
    x = cur.fetchone()
    return x[0]
  
  def get_name(self):
    cur = self.conn.cursor()
    cur.execute(str("SELECT name FROM servers WHERE server_id ="+str(self.id)))
    name = cur.fetchone()
    print(name)
    if name is not None:
      return name[0]
    else:
      print('Server name is None???')
  
  def in_db(self):
    cur = self.conn.cursor()
    cur.execute(str("SELECT daily FROM msgs WHERE server_id ="+str(self.id)))
    daily = cur.fetchone()
    if not daily:
      return False
    else:
      return True
  
  def create(self):
    sql = "INSERT INTO servers(name,server_id,owner,users) VALUES(?,?,?,?)"
    mod = (self.server.name,self.id,self.server.owner_id,len(self.server.members))
    print(mod)
    cur = conn.cursor()
    cur.execute(sql, mod)
    conn.commit()

    sql = "INSERT INTO msgs(server_id,all_time,monthly,daily,total,cur_day,cur_month,diff,past_diff) VALUES(?,?,?,?,?,?,?,?,?)"
    mod = (self.server.id,0,0,0,0,0,0,0,0)
    print(mod)
    cur = conn.cursor()
    cur.execute(sql, mod)
    conn.commit()

class message:

  def __init__(self,dserver,user,test=True,month=None):
    self.server = dserver
    server_id = self.server.id
    # Check server!
    self.server = server(server_id,server=dserver)
    if not self.server.in_db():
      print('Server not in db :(\nAdding server :)')
      self.server.create()
    # Init
    self.server_id = server_id
    if month:
      self.month = month
    else:
      self.month = False
    self.user = user
    self.test = test
    self.conn = conn
    # DB
    self.add(self.conn)
    # Debug
    print('Created message entry!',self.inf)

  def add(self,conn):
    c.read('month_data.json')
    com = None
    from datetime import datetime
    datee = datetime.today().strftime('%Y%m%d')
    if self.month:
      if str(self.server_id) in c.get('servers'):
        c.get('servers')[str(self.server_id)]['monthly'][self.month] = self.get_monthly(self.conn)+1
        self.inf = "Test!"
      else:
        print('failed normal write?',c.get('servers'))
        c.datajson['servers'][self.server_id] = {}
        c.datajson['servers'][self.server_id]['monthly'] = {}
        c.datajson['servers'][self.server_id]['monthly'][self.month] = self.get_monthly(self.conn)+1
      c.save()
    elif str(self.check_date(self.conn)) == str(datee):
      sql = "UPDATE msgs SET total = ?, daily = ?, monthly = ? WHERE server_id = ?"
      com = (self.get_total(self.conn)+1,self.get_daily(self.conn)+1,self.get_monthly(self.conn)+1,self.server_id)
      if str(self.server_id) in c.get('servers'):
        c.get('servers')[str(self.server_id)]['monthly'][str(datee)[4:6]] = self.get_monthly(self.conn)+1
      else:
        print('failed normal write?',c.get('servers'))
        c.datajson['servers'][self.server_id] = {}
        c.datajson['servers'][self.server_id]['monthly'] = {}
        c.datajson['servers'][self.server_id]['monthly'][str(datee)[4:6]] = self.get_monthly(self.conn)+1
      c.save()
    else:
      print('Date differs?',str(self.check_date(self.conn)),str(datee))
      if str(self.check_date(self.conn))[4:6] == str(datee)[4:6]:
        sql = "UPDATE msgs SET daily = ?, cur_day = ? WHERE server_id = ?"
        com = (1,datee,self.server_id)
      elif self.check_date(self.conn) != 0:
        new_diff = get_change(self.get_diff(),self.get_past_diff())
        cur_diff = self.get_diff()
        past_diff = self.get_past_diff()
        sql = "UPDATE msgs SET daily = ?, monthly = ?, cur_day = ?, diff = ?, past_dif = ? WHERE server_id = ?"
        com = (1,1,datee,new_diff,cur_diff,self.server_id)
      else:
        sql = "UPDATE msgs SET total = ?, daily = ?, monthly = ?, cur_day = ? WHERE server_id = ?"
        com = (1,1,1,datee,self.server_id)
    if com:
      self.inf = com
      cur = conn.cursor()
      cur.execute(sql, com)
      conn.commit()
  
  def check_date(self,conn):
    cur = conn.cursor()
    cur.execute(str("SELECT cur_day FROM msgs WHERE server_id ="+str(self.server_id)))
    daily = cur.fetchone()
    return daily[0]

  def get_total(self,conn):
    cur = conn.cursor()
    cur.execute(str("SELECT total FROM msgs WHERE server_id ="+str(self.server_id)))
    x = cur.fetchone()
    return x[0]
  
  def get_daily(self,conn):
    cur = conn.cursor()
    cur.execute(str("SELECT daily FROM msgs WHERE server_id ="+str(self.server_id)))
    x = cur.fetchone()
    return x[0]
  
  def get_monthly(self,conn):
    cur = conn.cursor()
    cur.execute(str("SELECT monthly FROM msgs WHERE server_id ="+str(self.server_id)))
    x = cur.fetchone()
    return x[0]
  
  def get_diff(self):
    cur = self.conn.cursor()
    cur.execute(str("SELECT diff FROM msgs WHERE server_id ="+str(self.server_id)))
    x = cur.fetchone()
    return x[0]

  def get_past_diff(self):
    cur = self.conn.cursor()
    cur.execute(str("SELECT past_diff FROM msgs WHERE server_id ="+str(self.server_id)))
    x = cur.fetchone()
    return x[0]
    
def get_change(current, previous):
    if current == previous:
        return 100.0
    try:
        return (abs(current - previous) / previous) * 100.0
    except ZeroDivisionError:
        return 0

def get_from_config(ctype,server_id):
  if ctype == 'month':
    monthly = c.datajson['servers'][str(server_id)]['monthly']
    return monthly