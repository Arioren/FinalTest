# 1. The deadliest attack types. "Deadliest" =
# the types with the highest number of casualties,
# killed and injured, where a casualty = 1 point and a kill is worth 2 points for
# the calculation. a. Filter option by -5Top or All
from sqlalchemy import func
from app.db.database import session_maker
from app.db.model import Event, Casualties, AttackType


def deadliest_attack_types(filter_option="Top 5"):
    with session_maker() as session:
        query = (
            session.query(
                Event.attack_type_id,
                AttackType.name,
                func.sum(Casualties.killed * 2 + Casualties.wounded).label("score")
            )
            .join(Casualties)
            .join(AttackType, Event.attack_type_id == AttackType.id)
            .group_by(Event.attack_type_id, AttackType.name)
            .order_by(func.sum(Casualties.killed * 2 + Casualties.wounded).desc())
        )

        if filter_option == "Top 5":
            query = query.limit(5)

        result = query.all()

        return [{"name": row[1], "score": row[2]} for row in result]