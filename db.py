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
        return answer
    except Exception as e:
        print(e)

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
            id = request_db(sql_insert)
            return id[0][0]
        return answer[0][0]


    except Exception as e:
        print(e)


def insert_phone(phone):
    try:
        sql_check = "select id from phone where phone='{}'".format(phone)
        sql_insert = "insert into phone(phone) values('{}') returning id".format(phone)

        answer = request_db(sql_check)
        if int(len(answer)) == 0:
            id = request_db(sql_insert)
            return id[0][0]
        return answer[0][0]
    except Exception as e:
        raise

def insert_date(name, surname, id_email, password, id_phone):
    try:
        sql_check = "select id from file_vk where name='{}' and surname='{}' and email='{}' and password='{}' and phone='{}' ".format(name, surname, id_email, password, id_phone)
        sql_insert = "insert into file_vk(name, surname, email, password, phone) values('{}', '{}', '{}', '{}','{}') returning id".format(name, surname, id_email, password, id_phone)

        answer = request_db(sql_check)
        if int(len(answer)) == 0:
            id = request_db(sql_insert)
            return id[0][0]
        return answer[0][0]
    except Exception as e:
        raise

def main():
    vershion()



if __name__ == '__main__':
    main()
