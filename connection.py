import psycopg2
from psycopg2.extras import RealDictCursor


conn = psycopg2.connect("dbname=curso_mvcad user=postgres password=teste host=localhost")

conn.autocommit = True

cursor = conn.cursor(cursor_factory=RealDictCursor)