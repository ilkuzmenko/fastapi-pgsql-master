from sqlalchemy.orm import Session
from models import Item
from schemas import ItemSchema


def get_item(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()


def get_item_by_id(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()


def create_item(db: Session, item: ItemSchema):
    _item = Item(day=item.day, date=item.date)
    db.add(_item)
    db.commit()
    db.refresh(_item)
    return _item


def remove_item(db: Session, item_id: int):
    _item = get_item_by_id(db=db, item_id=item_id)
    db.delete(_item)
    db.commit()


def update_item(db: Session, item_id: int, day: str, date: str):
    _item = get_item_by_id(db=db, item_id=item_id)

    _item.day = day
    _item.date = date

    db.commit()
    db.refresh(_item)
    return _item
