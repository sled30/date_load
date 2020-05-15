import psycopg2

def open_conn():
    conn = psycopg2.connect(dbname='postgres', user='postgres',
                            password='test', host='localhost')
    return conn.cursor()
def close_conn(conn):
    conn.close()
def vershion():
    conn = open_conn()

    conn.execute('select version()')
    rows = conn.fetchall()
    print(rows)



def main():
    vershion()



if __name__ == '__main__':
    main()
