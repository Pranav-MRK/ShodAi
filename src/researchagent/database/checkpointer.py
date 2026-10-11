from psycopg import Connection

from langgraph.checkpoint.postgres import PostgresSaver

from researchagent.database.postgres import DATABASE_URL

def get_checkpointer():
    connection = Connection.connect(DATABASE_URL,autocommit=True)
    checkpointer = PostgresSaver(connection) # type: ignore

    checkpointer.setup()
    return checkpointer