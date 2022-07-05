from fastapi import APIRouter
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import Response, RequestItem

import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("s/")
async def get_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _items = crud.get_item(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_items)

@router.get("/{itemId}")
async def get_item(itemId, db: Session = Depends(get_db)):
    _items = crud.get_item_by_id(db, item_id=itemId)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_items)

@router.post("/create")
async def create_item_service(request: RequestItem, db: Session = Depends(get_db)):
    crud.create_item(db, item=request.parameter)
    return Response( status="Ok", code="200", message="Item created successfully").dict(exclude_none=True)

@router.patch("/update")
async def update_item(request: RequestItem, db: Session = Depends(get_db)):
    _item = crud.update_item(db, item_id=request.parameter.id,
    title=request.parameter.title, description=request.parameter.description)
    return Response(status="Ok", code="200", message="Success update data", result=_item)

@router.delete("/delete")
async def delete_item(request: RequestItem,  db: Session = Depends(get_db)):
    crud.remove_item(db, item_id=request.parameter.id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)

