
import psycopg2 as pg

def connection():
	# Connect to an existing database
	conn = pg.connect("""host=localhost 						
                       dbname=aceh40db 						
                       user=aceh40user 						
                       password=pass""")

	# Open a cursor to perform database operations
	cur = conn.cursor()
	return cur, conn