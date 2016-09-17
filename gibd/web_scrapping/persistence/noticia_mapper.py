from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import mapper

from web_scrapping.model.noticia import Noticia
from web_scrapping.persistence.base import Base

metadata = Base.metadata

noticia = Table('noticia', metadata,
                Column('id', Integer, primary_key=True),
                Column('url', String),
                Column('texto', String),
                Column('titulo', String),
                Column('fecha', String),
                Column('imagen', String)
                )

mapper(Noticia, noticia)
