from mysql.connector import Error
from hcl_database_connection import MysqlDatabaseConnection
class HclStoredProcedure(MysqlDatabaseConnection):
    def execute_str_procedure(self):
        try:
            self.cursor.callproc("get_cust")
            for r in self.cursor.stored_results():
                print(r.fetchall())
        except Exception as e:
            print(e)
        finally:
            if(self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()

connect_obj=HclStoredProcedure()
connect_obj.connect("localhost","root","root","hcl_vijayawada")
connect_obj.execute_str_procedure()
