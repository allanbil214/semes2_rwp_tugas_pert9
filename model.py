import mysql.connector

class Model:
    def connect(self):
        return mysql.connector.connect(
            host = "localhost", 
            user = "root", 
            password = "", 
            database = "crud_383")
    
    def read(self):
        con = Model.connect(self)
        cur = con.cursor()
        cur.execute("select * from armaments_383")
        return cur.fetchall()
    
    def add(self, id, name, rarity, affinity, itype, desc):
        con = Model.connect(self)
        cur = con.cursor()
        cur.execute("""insert into armaments_383(id_383, name_383, 
                    rarity_383, affinity_383, type_383, description_383) 
                    values(%s, %s, %s, %s, %s, %s);""", 
                    (id, name, rarity, affinity, itype, desc,))
        con.commit()
        return True
    
    def remove(self, id):
        con = Model.connect(self)
        cur = con.cursor()
        cur.execute("delete from armaments_383 where id_383=%s", (id,))
        con.commit()
        return True

    def edit(self, id):
        con = Model.connect(self)
        cur = con.cursor()
        cur.execute("select * from armaments_383 where id_383=%s", (id,))
        return cur.fetchall()

    def edit_save(self, id, name, rarity, affinity, itype, desc, oldID):
        con = Model.connect(self)
        cur = con.cursor()
        cur.execute("""update armaments_383 set id_383=%s, name_383=%s, 
                    rarity_383=%s, affinity_383=%s, type_383=%s, 
                    description_383=%s where id_383=%s;""", 
                    (id, name, rarity, affinity, itype, desc, oldID,))
        con.commit()
        return True
    