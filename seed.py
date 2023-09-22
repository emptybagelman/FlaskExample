from application import db
from application.characters.model import Character

db.drop_all()
print("Dropping database")
db.create_all()
print("Generating database")

print("Seeding database")
entry1 = Character(name="Phoebe",age=29,catch_phrase="Smelly cat")
entry2 = Character(name="Edward",age=22,catch_phrase="Who are you calling short?")

# db.session.add(entry1)
# db.session.add(entry2)

db.session.add_all([entry1,entry2])

db.session.commit()
print("Database seeded.")