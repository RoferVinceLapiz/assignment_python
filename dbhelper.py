from sqlite3 import connect, Row

database = 'db/school.db'

def getprocess(sql: str, vals: list) -> list:
    conn = connect(database)
    conn.row_factory = Row
    cursor = conn.cursor()                    
    cursor.execute(sql, vals)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data


def postprocess(sql: str, vals: list) -> bool:
    try:
        conn = connect(database)
        cursor = conn.cursor()                
        cursor.execute(sql, vals)
        conn.commit()
        success = cursor.rowcount > 0
    except Exception as e:
        print(f"Error: {e}")
        success = False
    finally:
        cursor.close()
        conn.close()
    return success


def getall(table: str) -> list:
    sql = f"SELECT * FROM {table}"
    return getprocess(sql, [])


def getrecord(table: str, **kwargs) -> list:
    keys = list(kwargs.keys())
    vals = list(kwargs.values())
    fields = " AND ".join([f"{k}=?" for k in keys])
    sql = f"SELECT * FROM {table} WHERE {fields}"
    return getprocess(sql, vals)


def addrecord(table:str,**kwargs)->bool:
    keys:list = list(kwargs.keys())
    vals:list = list(kwargs.values())
    dats:list = ['?']*len(keys)
    datstring:str = ",".join(flds)
    fields:str = "','".join(keys)
    sql:str = f"INSERT INTO '{table}'('{fields}') VALUES {datstring}"
    return postprocess(sql,vals)
    
def deleterecord(table:str,**kwargs)->bool:
    keys:list = list(kwargs.keys())
    vals:list = list(kwargs.values())
    flds:list = []
    for key in  keys:
        flds.append(f"'{key}'=?")
    fields:str = "AND".join(flds)
    sql:str = f"DELETE * FROM '{table}' WHERE {fields}"
    return postprocess(sql,vals)
    
def updaterecord(table:str,**kwargs)->bool:
    keys:list = list(kwargs.keys())
    vals:list = list(kwargs.values())
    newvals:list = []
    flds:list = []
    for index in range(1,len(keys)):
        flds.append(f"'{key}'=?")
        newvals.append(f"{vals[index]}")
    fields:str = ",".join(flds)
    sql:str = f"UPDATE '{table}' SET {fields} WHERE '{keys[0]}'= '{vals[0]}'"
    return postprocess(sql,vals)

    