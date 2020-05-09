import datetime
import mysql.connector

class database:
    #source: https://www.youtube.com/watch?v=xgyVilYfJEo, https://dev.mysql.com/doc/connector-python/en/connector-python-api-errors-error.html
    def __init__(self):
        self.conn = 0
        self.mycursor = 0
        self.working = False
        try:
            self.conn = mysql.connector.connect(user='karenws',password='eiR4eiyi',host='mysql.eecs.ku.edu',database='karenws')
            self.mycursor = self.conn.cursor(buffered=True)
            self.mycursor.execute("SHOW TABLES")            
            print(self.mycursor.fetchall())
            self.working = True
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
                return True
            
            else:
                return False # User not found

