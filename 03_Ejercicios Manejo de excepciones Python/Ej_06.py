import pymysql

while True:
    connection = pymysql.connect(host='localhost', user='bdi', password='pepe1234', db='Exceptions')
    cursor=connection.cursor()
    code = input("Introduce la accion que desea realizar: ")
    try:
        cursor.execute(code)
    except pymysql.err.ProgrammingError as e:
        print("Error: ", e)
    except pymysql.err.IntegrityError as a:
        print("Error: ", a)
    except pymysql.err.DataError as b:
        print("Error: ", b)
    except pymysql.err.InternalError as c:
        print("Error: ", c)
    except pymysql.err.NotSupportedError as d:
        print("Error: ", d)
    except pymysql.err.OperationalError as f:
        print("Error: ", f)