from sqlalchemy import select, desc
from polestar.models import models

URL = '/positions/<imo>'


def get_ship_position(session, imo):
    try:
        query = (
            select(models.locations)
                .where(models.locations.c.IMO_number == imo)
                .order_by(desc(models.locations.c.timestamp))
        )

        output = session.execute(query).fetchall()

        result = [
            {
                "IMO_number": int(ship.IMO_number),
                "latitude": str(ship.latitude),
                "longitude": str(ship.longitude),
            }
            for ship in output
        ]

        return result

    except Exception as e:
        # We can log this error
        print(f"Error fetching ship position: {e}")
        return {"error": "Internal Server Error"}, 500

    finally:
        session.close()
