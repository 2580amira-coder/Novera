from database.models.user import User
from database.models.country import Country


def create_player(
    db,
    telegram_id,
    username,
    country_name
):

    existing_user = db.query(User).filter_by(
        telegram_id=telegram_id
    ).first()

    if existing_user:
        return existing_user


    user = User(
        telegram_id=telegram_id,
        username=username
    )

    db.add(user)
    db.flush()


    country = Country(
        user_id=user.id,
        name=country_name
    )

    db.add(country)

    db.commit()

    db.refresh(user)

    return user