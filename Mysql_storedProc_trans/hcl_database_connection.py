import mysql.connector
class MysqlDatabaseConnection:
    def connect(self,host,username,password,database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.connection = mysql.connector.connect(host=self.host, username=self.username, password=self.password,
                                                  database=self.database)
        self.cursor = self.connection.cursor()
