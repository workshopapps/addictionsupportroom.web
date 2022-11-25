import datetime
import re
from sqlalchemy import (
    BIGINT,
    Column,
    DateTime,
    Integer,
)
from sqlalchemy.orm import (
    declarative_mixin,
    declared_attr,
    registry,
)
from sqlalchemy.orm.decl_api import (
    DeclarativeMeta,
)

mapper_registry = registry()


class Base(metaclass=DeclarativeMeta):
    __abstract__ = True

    registry = mapper_registry
    metadata = mapper_registry.metadata

    __init__ = mapper_registry.constructor


@declarative_mixin
class CommonMixin:
    """define a series of common elements that may be applied to mapped
    classes using this class as a mixin class."""

    __name__: str
    __table_args__ = {"mysql_engine": "InnoDB"}
    __mapper_args__ = {"eager_defaults": True}

    # Use this for MYSQL or Postgress
    # id: int = Column(BIGINT, primary_key=True, autoincrement=True)

    # Use this for sqlite
    id = Column(Integer, primary_key=True, index=True)

    @declared_attr
    def __tablename__(cls) -> str:
        split_cap = re.findall("[A-Z][^A-Z]*", cls.__name__)
        table_name = (
            "".join(map(lambda word: word.lower() + "_", split_cap[:-1]))
            + split_cap[-1].lower()
        )
        return table_name


@declarative_mixin
class TimestampMixin:
    creation_date: datetime = Column(DateTime, default=datetime.datetime.utcnow())
    modified_date: datetime = Column(DateTime)
