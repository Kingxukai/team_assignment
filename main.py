import pyodbc

server = 'DESKTOP-BCQ7R0B\\MSSQL'
database = 'lucky_database'
username = 'wxk'
password = '12345678'

connection_string = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password}"
)

try:
    cnxn = pyodbc.connect(connection_string)
    print("Connection successful!")

    # 创建游标对象
    cursor = cnxn.cursor()

    # 执行查询
    cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'")

    # 获取查询结果（结果是一个二维数组）
    rows = cursor.fetchall()

    # 打印查询结果
    for row in rows:
        print(row[0])

    # 关闭游标和连接
    cursor.close()
    cnxn.close()

except Exception as e:
    print("Connection failed!")
    print(e)