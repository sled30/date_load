import psycopg2

def open_conn():
    conn = psycopg2.connect(dbname='postgres', user='postgres',
                            password='test', host='localhost')
    return conn
def request_db(sql):
    conn = open_conn()
    cur = conn.cursor()
    with conn:
        cur.execute(sql)
        answer = cur.fetchall()
        cur.close
        conn.close

    return answer
def insert_db(sql):
    try:
        print(sql)
        conn = open_conn()
        cur = conn.cursor()
        with conn:
            cur.execute(sql)
            answer = cur.lastrowid()
            cur.close
            conn.close
            # pint(answer)
        return answer
    except Exception as e:
        raise

def version():
    conn = open_conn()

    conn.execute('select version()')
    rows = conn.fetchall()
    print(rows)
    conn.close()

def insert_email(email):
    try:

        sql_check = "select id from email where email='{}'".format(email)
        sql_insert = "insert into email(email) values('{}') returning id".format(email)

        answer = request_db(sql_check)
        if int(len(answer)) == 0:
            print(email)
            id = request_db(sql_insert)

    except Exception as e:
        print(e)


def insert_phone():
    pass

def insert_date():
    pass

def main():
    vershion()



if __name__ == '__main__':
    main()
