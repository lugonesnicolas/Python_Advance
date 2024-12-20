from modules.models import Person
from modules.db import create_session
from datetime import date

with create_session() as db:
    persona_test = Person(name="Nicolas", last_name="Lugones", age=28, birth_date=date(1996,1,27))
    db.add(persona_test)
    db.commit()

    all_person = db.query(Person).all()
    for person in all_person:
        print(person.name, person.last_name)