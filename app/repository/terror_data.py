# 1. The deadliest attack types. "Deadliest" =
# the types with the highest number of casualties,
# killed and injured, where a casualty = 1 point and a kill is worth 2 points for
# the calculation. a. Filter option by -5Top or All
from app.db.database import session_maker


def deadliest_attack_types():
    with session_maker() as session:
        result = session.execute("SELECT attacktype1, SUM(nkills*2 + nwounds) as casualties FROM terror GROUP BY attacktype1 ORDER BY SUM(casualties) DESC LIMIT 5")
        return [row[0] for row in result]

print(deadliest_attack_types())