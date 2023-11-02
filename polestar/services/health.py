from sqlalchemy import select
from polestar.models import models
URL = '/health'

SQL_SESSION = None


def get_health_status(session):
    query = select(models.ships)
    output = session.execute(query).fetchone()
    session.close()
    if output:
        return "Health is good"
    else:
        return "Not in a good state"
