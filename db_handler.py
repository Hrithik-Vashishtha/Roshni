import mysql.connector

class GameDatabase:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="09041997",
            database="chess"
        )   
        self.mycursor = self.mydb.cursor()
    
    def create_game(self, moves_list):
        query = "insert into game_data (moves_list) values (%s)"
        values = (moves_list,)
        self.mycursor.execute(query, values)
        self.mydb.commit()
    
    def get_moves(self, id):
        if id:
            query = "select * from game_data where id = %s"
            self.mycursor.execute(query, (id,))
            result = self.mycursor.fetchall()
            if result:
                return({"moves": result})
            return("id not found")
        return("id not provided")
