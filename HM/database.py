import datetime
import mysql.connector

class database:
    #source: https://www.youtube.com/watch?v=xgyVilYfJEo, https://dev.mysql.com/doc/connector-python/en/connector-python-api-errors-error.html
    def __init__(self):
        self.conn = 0
        self.mycursor = 0
        self.working = False
        try:
            self.conn = mysql.connector.connect(user='karenws',password='eiR4eiyi',host='mysql.eecs.ku.edu',database='karenws',charset='utf8')
            self.mycursor = self.conn.cursor(buffered=True)
            self.working = True
            print("HERE")
        except ImportError:
            print("database() error: MySQL-Connector could not be imported")
        except mysql.connector.Error as err:
            print("database() error: {}".format(err))
    
    def login(self, doctor_id, password):
        """ 
        Check user credential 
        
        Param:
        - username (str)
        - password (str)
        Return:
        - (bool)
        """
        if (self.working):
            
            self.mycursor.execute(f"SELECT * from doctor where DOCTOR_ID={doctor_id}")
            result = self.mycursor.fetchall()

            if len(result) == 1:
                # Check if password match
                if (result[0][1] == password ):
                    return True
                else:
                    return False # Wrong Password
            else:
                return False
            
        else:
            return False # Have not set the mysql connector
    def number_dict(self):
        """ 
        Check the number of type(patient,doctor,bed, treatment)
        
        Param:
        - type (str)
        Return:
        - number (negative values are not possible unless mysql.connector not connected)
        """
        if (self.working):
            self.mycursor.execute("SHOW TABLES")
            table_name_list = self.mycursor.fetchall()

            print(table_name_list)
            result_dict = {}
            print("result_dcit ist")
            print(result_dict)

            for table_name_tuple in table_name_list:
                table_name = table_name_tuple[0]
                if (table_name == "Posts"):
                    continue
                self.mycursor.execute(f"SELECT COUNT(*) FROM {table_name}")
                result_dict[table_name] = self.mycursor.fetchone()[0]
            
            return result_dict
        else:
            return -1



