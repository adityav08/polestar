from sqlalchemy import select
from polestar.models import models

URL = '/ships'

def get_all_ships(session):
    try:
        query = select(models.ships)
        output = session.execute(query).fetchall()

        result = [
            {
                "IMO_number": int(ship.IMO_number),
                "ship_name": ship.ship_name,
            }
            for ship in output
        ]

        return result

    except Exception as e:
        # We can log this error
        print(f"Error fetching all ships: {e}")
        return {"error": "Internal Server Error"}, 500

    finally:
        session.close()
