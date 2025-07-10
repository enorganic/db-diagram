from __future__ import annotations

from typing import TYPE_CHECKING, Any

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    ForeignKeyConstraint,
    Integer,
    String,
)
from sqlalchemy.orm import declarative_base

if TYPE_CHECKING:
    from datetime import datetime

Base: Any = declarative_base(name="Base")


class A(Base):
    __tablename__: str = "A"
    a_id: Column[int] = Column("A_ID", Integer, primary_key=True)
    name: Column[str] = Column("NAME", String)
    updated: Column[datetime] = Column("UPDATED", DateTime)


class B(Base):
    __tablename__: str = "B"
    b_id: Column[int] = Column("B_ID", Integer, primary_key=True)
    name: Column[str] = Column("NAME", String)
    updated: Column[datetime] = Column("UPDATED", DateTime)


class C(Base):
    __tablename__: str = "C"
    c_id: Column[int] = Column("C_ID", Integer, primary_key=True)
    name: Column[str] = Column("NAME", String)
    updated: Column[datetime] = Column("UPDATED", DateTime)


class A_B(Base):  # noqa: N801
    __tablename__: str = "A_B"
    a_id: Column[int] = Column(
        "A_ID", Integer, ForeignKey(A.a_id), primary_key=True
    )
    b_id: Column[int] = Column(
        "B_ID", Integer, ForeignKey(B.b_id), primary_key=True
    )
    name: Column[str] = Column("NAME", String)
    updated: Column[datetime] = Column("UPDATED", DateTime)


class B_C(Base):  # noqa: N801
    __tablename__: str = "B_C"
    b_id: Column[int] = Column(
        "B_ID", Integer, ForeignKey(B.b_id), primary_key=True
    )
    c_id: Column[int] = Column(
        "C_ID", Integer, ForeignKey(C.c_id), primary_key=True
    )
    name: Column[str] = Column("NAME", String)
    updated: Column[datetime] = Column("UPDATED", DateTime)


class A_B_C(Base):  # noqa: N801
    __tablename__: str = "A_B_C"
    a_id: Column[int] = Column("A_ID", Integer, primary_key=True)
    b_id: Column[int] = Column("B_ID", Integer, primary_key=True)
    c_id: Column[int] = Column("C_ID", Integer, primary_key=True)
    name: Column[str] = Column("NAME", String)
    updated: Column[datetime] = Column("UPDATED", DateTime)


ForeignKeyConstraint(
    columns=("A_ID", "B_ID"),
    refcolumns=(
        A_B.a_id,
        A_B.b_id,
    ),
    table=A_B_C.__table__,
    use_alter=True,
)


ForeignKeyConstraint(
    columns=("B_ID", "C_ID"),
    refcolumns=(
        B_C.b_id,
        B_C.c_id,
    ),
    table=A_B_C.__table__,
    use_alter=True,
)
