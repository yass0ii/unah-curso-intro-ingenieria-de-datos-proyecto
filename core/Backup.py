# mysqldump --user user_name --password user_password --databases db_name

import subprocess

class Backup:
    """
        Realiza backup de una base de datos desde la instancia de Mysql
        @author: kenneth.cruz@unah.hn
        @date 2023/04/18
        @since 2023/04/18
    """
    
    def __init__(self, configConnection:dict, nameDB:str) -> None:
        self.nameDB = nameDB
        self.user = configConnection["user"]
        self.password = configConnection["password"]
        self.bashCommand = f"mysqldump --user {self.user} --password='{self.password}' --databases {self.nameDB} > ../{self.nameDB}/\"$(date +'%Y-%m-%d_%H:%M:%S').sql\""

    
    def backup(self):
        
        process = subprocess.Popen(self.bashCommand, shell=True)

        process.wait()

        if process.returncode == 0:
            print(f"'{self.nameDB}': El backup se creó correctamente.")
        else: 
            print(f"'{self.nameDB}': Se produjo un error al crear el backup.")