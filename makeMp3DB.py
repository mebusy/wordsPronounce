import os
import hashlib 
import sqlite3

def makeDB():
    mp3_path = "words_pronounce" 
    if not os.path.exists( mp3_path ) :
        return  
    for f in os.listdir( mp3_path ) :
        _name , _ext = os.path.splitext(f)
        path_f = os.path.join( mp3_path, f )
        with open( path_f ) as fp :
            data = fp.read()

            c.execute("INSERT or replace INTO pron VALUES ( ?,?)" , ( _name .decode( "utf8" ) , buffer(data) ) )
    pass
                     


if __name__ == '__main__' :

    db_file = "pron.db" 
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
        

    c.execute( "drop table if exists pron "  )
    c.execute( '''create table if not exists pron
                    ( word text primary key ,  voice BLOB NOT NULL  ) ''' )

    makeDB()

    # c.execute( '''create UNIQUE index index_pron_word_voice on pron ( word , voice  ) ''' )
    c.execute( "vacuum" )

    conn.commit()
    conn.close()
