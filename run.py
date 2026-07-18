from database.database import SessionLocal, create_tables
from engine.player.player_service import create_player


create_tables()

db = SessionLocal()


player = create_player(
    db,
    telegram_id="123456",
    username="Amir",
    country_name="Novera Empire"
)


print("Player Created:")
print(player.username)
print(player.country.name)
print(player.country.gold)


db.close()