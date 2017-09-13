import os
import hashlib 
import sqlite3

def removeOggHead():
    md5_head_pub = None
    oggs_path = "oggs" 
    if not os.path.exists( oggs_path ) :
        return  
    for f in os.listdir( oggs_path ) :
        _name , _ext = os.path.splitext(f)
        path_f = os.path.join( oggs_path, f )
        # print path_f

        with open( path_f ) as fp :
            data = fp.read()

            head_private = data[:84]
            head_pub = data[84: 213*16 ]
            assert head_pub[-1] == '\x53'
            body = data[ 213*16: ]
                
            m = hashlib.md5()     
            m.update( head_pub)
            hex_md5 = m.hexdigest() 
            
            if md5_head_pub is None:
                with open( "head_pub.bin" , "wb" ) as f_pub:
                    f_pub.write( head_pub ) 
                    
                md5_head_pub = hex_md5
            else:
                assert md5_head_pub == hex_md5


            c.execute("INSERT or replace INTO pron VALUES ( ?,?)" , ( _name .decode( "utf8" ) , head_private + body   ) )
    pass
                     


if __name__ == '__main__' :

    db_file = "pron.db" 
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
        
    c.execute( '''create table if not exists pron
                    ( word text primary key ,  voice BLOB NOT NULL  ) ''' )
    removeOggHead()

    conn.commit()
    conn.close()
