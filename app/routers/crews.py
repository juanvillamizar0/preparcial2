from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas
router = APIRouter(prefix="/crews", tags=["Crews"])
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.post("/", response_model=schemas.CrewResponse)
def create_crew(crew: schemas.CrewCreate, db: Session = Depends(get_db)):
    new_crew = models.Crew(**crew.model_dump())
    db.add(new_crew)
    db.commit()
    db.refresh(new_crew)
    return new_crew
@router.get("/", response_model=list[schemas.CrewResponse])
def get_crews(db: Session = Depends(get_db)):
    return db.query(models.Crew).all()
@router.get("/{crew_id}", response_model=schemas.CrewResponse)
def get_crew(crew_id: int, db: Session = Depends(get_db)):
    crew = db.query(models.Crew).filter(models.Crew.id == crew_id).first()
    if not crew:
        raise HTTPException(status_code=404, detail="Crew not found")
    return crew
@router.patch("/{crew_id}", response_model=schemas.CrewResponse)
def update_crew(crew_id: int, crew_data: schemas.CrewUpdate, db: Session = Depends(get_db)):
    crew = db.query(models.Crew).filter(models.Crew.id == crew_id).first()
    if not crew:
        raise HTTPException(status_code=404, detail="Crew not found")
    for key, value in crew_data.model_dump(exclude_unset=True).items():
        setattr(crew, key, value)
    db.commit()
    db.refresh(crew)
    return crew
@router.delete("/{crew_id}")
def delete_crew(crew_id: int, db: Session = Depends(get_db)):
    crew = db.query(models.Crew).filter(models.Crew.id == crew_id).first()
    if not crew:
        raise HTTPException(status_code=404, detail="Crew not found")
    db.delete(crew)
    db.commit()
    return {"message": "Crew deleted successfully"}