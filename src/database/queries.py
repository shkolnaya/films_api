"""
SELECT QUERIES
"""
from sqlalchemy import and_

from src import db
from src.database import models

#all films ordered by rating from biggest
films = db.session.query(models.Film).order_by(models.Film.rating.desc()).all()

#first film with name 'shining'
the_shinig = db.session.query(models.Film).filter(
    models.Film.title == 'The Shining'
).first()

# first film by name
the_shadows = db.session.query(models.Film).filter_by(
    title='50 Shadows of Grey'
).first()


# all films with name AND rating
and_statement = db.session.query(models.Film).filter(
    models.Film.title != 'The Shining',
    models.Film.rating >= 7.5
).all()

# all films with name AND rating
and_statement_2 = db.session.query(models.Film).filter(
    and_(
        models.Film.title != 'The Shining',
        models.Film.rating >= 7.5
    )
).all()

# all films with 'twighlight' in title
twighlight = db.session.query(models.Film).filter(
    models.Film.title.like('%twighlight%')
).all()

# all films with 'twighlight' in title
twighlights = db.session.query(models.Film).filter(
    models.Film.title.ilike('%twighlight%')
).all()


# all films NOT with length 92 or 108
sorted_by_length = db.session.query(models.Film).filter(
    ~models.Film.length.in_([92, 108])).all()


# 2 films with length 92 or 108
sorted_by_slice = db.session.query(models.Film).filter(
    models.Film.length.in_([92, 108]))[:2]

"""
QUERING WITH JOINS
"""

films_with_actors = db.session.query(models.Film).join(models.Film.actors).all()
