import psycopg2
from config import config

def connect(city,query1):
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        cur.execute(query1,(city,))
        data=cur.fetchall()

        data_dict=[]
        data_key=["ifsc","bank_id","branch","address","city","district","state"]
        for entry in data:
            data_dict.append({data_key[i]:entry[i] for i in range(len(data_key))})

        return data_dict

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

