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
        except ImportError:
            print("database() error: MySQL-Connector could not be imported")
        except mysql.connector.Error as err:
            print("database() error: {}".format(err))
    
    def login(self, username, password):
        """ 
        Check user credential 
        
        Param:
        - username (str)
        - password (str)
        Return:
        - (bool)
        """
        if (self.working):
            
            self.mycursor.execute(f"SELECT * from doctor where USERNAME='{username}'")
            result = self.mycursor.fetchall()
            print("HERE")
            if len(result) == 1:
                # Check if password match
                if (result[0][2] == password ):
                    return result
                else:
                    return False # Wrong Password
            else:
                return False
            
        else:
            return False # Have not set the mysql connector
    def number_dict(self):
        if (self.working):
            self.mycursor.execute("SHOW TABLES")
            table_name_list = self.mycursor.fetchall()

            result_dict = {}
            
            for table_name_tuple in table_name_list:
                table_name = table_name_tuple[0]
                if (table_name=="bed" or table_name=="doctor" or table_name=="patient" or table_name=="treatment"):
                    self.mycursor.execute(f"SELECT COUNT(*) FROM {table_name}")
                    result_dict[table_name] = self.mycursor.fetchone()[0]     

            return result_dict
        else:
            return False
    def get_all_patient_info_list(self):
        if (self.working):
            self.mycursor.execute(f"SELECT * FROM patient")
            result = self.mycursor.fetchall()
            
            result_list = []
            
            for patient_id, name, sex, blood, heart, temp, pulse, bed, room, doctor in result:
                temp_dict = {}
                temp_dict["PATIENT_ID"] = patient_id
                temp_dict["NAME"] = name
                temp_dict["SEX"] = sex
                temp_dict["BLOOD"] = blood
                temp_dict["HEART_RATE"] = heart
                temp_dict["TEMPERATURE"] = temp
                temp_dict["PULSE"] = pulse
                # temp_dict["BED_ID"] = bed
                # temp_dict["ROOM_ID"] = room
                # temp_dict["DOCTOR_ID"] = doctor
                result_list.append(temp_dict) 
            return result_list
            
        else:
            return False

    # def register(self, username, password, fullname, admin=False):



