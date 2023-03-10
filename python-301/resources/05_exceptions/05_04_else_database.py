# Write a script that demonstrates a try/except/else statement.
# For example, you can revisit the course module about database interactions
# and include a try/except/else statement based on what to do whether or not
# the database connection can be established.



import sqlalchemy as s
import os
from pprint import pprint


password = "1123"
database_name = "fmd-repo"
username = "root"


try:
    engine = s.create_engine(f"mysql+pymysql://{username}:{password}@localhost/{database_name}")
    connection = engine.connect()
    metadata = s.MetaData()

    actor = s.Table('project', metadata, autoload=True, autoload_with=engine)

    query = s.select([actor])
    result_proxy = connection.execute(query)
    result_set = result_proxy.fetchall()
    pprint(result_set)





except s.exc.OperationalError as e:
    print(f"exception occured during runtime : {e}")

except TypeError as e:
    print(f"Error:  {e}")

else:
    print("connection successful")




