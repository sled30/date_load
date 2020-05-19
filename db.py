import psycopg2
import vk_load

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
        if len(phone) > 19:
            sql_check = "select id from phone where long='{}'".format(phone)
            sql_insert = "insert into phone(long) values('{}') returning id".format(phone)
        else:
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
<<<<<<< HEAD
        if id_email is None:
            email = '0'
=======
        if email is None:
            email = 'NULL'
>>>>>>> c9e2fa5dc8379a7f43a02f0ba07d3a35227f3afc
        sql_check = "select id from file_vk where name='{}' and surname='{}' and email='{}' and password='{}' and phone='{}' ".format(name, surname, id_email, password, id_phone)
        sql_insert = "insert into file_vk(name, surname, email, password, phone) values('{}', '{}', '{}', '{}','{}') returning id".format(name, surname, id_email, password, id_phone)

        answer = request_db(sql_check)
        if int(len(answer)) == 0:
            id = request_db(sql_insert)
            return id[0][0]
        return answer[0][0]
    except Exception as e:
        raise

def save_turn_vk_files(files):
    try:
        for file in files:
            if file != 'in' and file != 'load':
                sql_check = "select id from file where name='{}' and status='0' and source='vk_file'".format(file)
                sql_insert = "insert into file (name, status, source) values ('{}', '0', 'vk_file') returning id".format(file)
                check = request_db(sql_check)
                if int(len(check)) == 0:
                    id = request_db(sql_insert)

                    vk_load.rename_file_in(file)



    except Exception as e:

        print(e)

def get_turn_vk_files():
    try:
        sql_request="select name from file where status='0' and source='vk_file'"
        return request_db(sql_request)


    except Exception as e:
        print(e)

def main():
    vershion()



if __name__ == '__main__':
    main()
