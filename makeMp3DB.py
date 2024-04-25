#!python3
import os
# import hashlib
import sqlite3


def makeDB():
    mp3_path = "words_pronounce"
    if not os.path.exists(mp3_path):
        return
    for f in os.listdir(mp3_path):
        _name, _ext = os.path.splitext(f)
        path_f = os.path.join(mp3_path, f)
        with open(path_f, 'rb') as fp:
            data = fp.read()

            c.execute("INSERT or replace INTO pron VALUES ( ?,?)",
                      (_name, data))
    pass


if __name__ == '__main__':
    db_file = "pron.db"
    # if exists, remove
    if os.path.exists(db_file):
        os.remove(db_file)

    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    c.execute("drop table if exists pron ")
    c.execute('''create table if not exists pron
                    ( word text primary key ,  voice BLOB NOT NULL  ) ''')

    makeDB()
    conn.commit()

    c.execute("vacuum")

    conn.commit()
    conn.close()
