from datetime import date
from src import db
from src.database.models import Film, Actor


def populate_films():
    the_twighlight = Film(
        title="The Twighlight",
        release_date=date(2001, 11, 4),
        description="Vampires in love",
        distributed_by="Warner Bros. Pictures",
        length=152,
        rating=7.6
    )
    the_twighlight_2 = Film(
        title="The Twighlight 2",
        release_date=date(2005, 4, 4),
        description="Vampires in love 2",
        distributed_by="Warner Bros. Pictures",
        length=132,
        rating=5.6
    )
    shadows = Film(
        title="50 Shadows of Grey",
        release_date=date(2011, 1, 14),
        description="Not vampires in love",
        distributed_by="Warner Bros. Pictures",
        length=92,
        rating=0.6
    )
    the_shining = Film(
        title="The Shining",
        release_date=date(1991, 8, 17),
        description="Scary film",
        distributed_by="Warner Bros. Pictures",
        length=108,
        rating=9.6
    )

    daniel_radcliffe = Actor(name='Daniel Radcliffe', birthday=date(1989, 7, 23), is_active=False)
    jason_stathem = Actor(name='Jason Stathem', birthday=date(1969, 4, 13), is_active=True)
    alex_panin = Actor(name='Alexey Panin', birthday=date(1973, 10, 23), is_active=True)
    olivia_wild = Actor(name='Olivia Wild', birthday=date(1985, 2, 20), is_active=True)

    the_twighlight.actors = [alex_panin, olivia_wild]
    the_twighlight_2.actors = [daniel_radcliffe, alex_panin]
    shadows.actors = [alex_panin, jason_stathem, daniel_radcliffe]
    the_shining.actors = [olivia_wild, jason_stathem]

    db.session.add(the_twighlight)
    db.session.add(the_twighlight_2)
    db.session.add(shadows)
    db.session.add(the_shining)

    db.session.add(daniel_radcliffe)
    db.session.add(jason_stathem)
    db.session.add(alex_panin)
    db.session.add(olivia_wild)

    db.session.commit()
    db.session.close()


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    print('Populating db...')
    populate_films()
    print('Successfully populated!')
