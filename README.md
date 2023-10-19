# fastapi_postgres_connection
 Learning to connect postgres with fastapi.
 
 Start by installing following in venv:
    1. fastapi
    2. uvicorn
    3. sqlalchemy
    4. psycopg2
    5. alembic
      Initiate alembic: alembic init alembic (i.e. alembic init folder_name). A folder names alembic and an ini file with the same name will be created. 

   
 Set a connection url. Using sqlalchemy create an engine, a session and a base. For these purposes, a separate file called database.py aur config.py can be created.

 In model.py create a class which represents the table.
 
 In the alembic.ini file scroll down to 'sqlalchemy.url' and assign it the connection url created above.

 Under the alembic folder, open the pre-existing env.py file and add the following lines:
   from database import base
   from model import *
Scroll down in the same file to 'target_metadata' and assign it base.metadata.