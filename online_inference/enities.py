"""Enities"""
from pydantic import BaseModel, validator
from fastapi.exceptions import HTTPException



class HeartDiseaseResponse(BaseModel):
    id: int
    condition: int


class HeartDisease(BaseModel):
    id: int
    age: float
    sex: int
    cp: int
    trestbps: float
    chol: float
    fbs: int
    restecg: int
    thalach: float
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

    @validator("age")
    def validation_age(cls, v):
        if v < 0 or v > 130:
            raise HTTPException(
                status_code=400,
                detail=[{"msg": "ValueError: invalid age value"}]
            )
        return v

    @validator("sex")
    def validation_sex(cls, v):
        if v not in [0, 1]:
            raise HTTPException(
                status_code=400,
                detail=[{"msg": "ValueError: invalid sex value"}]
            )
        return v

    @validator("cp")
    def validation_cp(cls, v):
        if v not in [0, 1, 2, 3]:
            raise HTTPException(
                status_code=400,
                detail=[{"msg": "ValueError: invalid cp value"}]
            )
        return v


    @validator("trestbps")
    def validation_trestbps(cls, v):
        if v < 0 or v > 300:
            raise HTTPException(
                status_code=400,
                detail=[{"msg": "ValueError: invalid trestbps value"}]
            )
        return v

    @validator("chol")
    def validation_chol(cls, v):
        if v < 0 or v > 600:
            raise HTTPException(
                status_code=400,
                detail=[{"msg": "ValueError: invalid chol value"}]
            )
        return v

    @validator("fbs")
    def validation_fbs(cls, v):
        if v not in [0, 1]:
            raise HTTPException(
                status_code=400,
                detail=[{"msg": "ValueError: invalid fbs value"}]
            )
        return v
    
    @validator("restecg")
    def validation_restecg(cls, v):
        if v not in [0, 1, 2]:
            raise HTTPException(
                status_code=400,
                detail=[{"msg": "ValueError: invalid restecg value"}]
            )
        return v

    @validator("thalach")
    def validation_thalach(cls, v):
        if v < 0 or v > 300:
            raise HTTPException(
                status_code=400,
                detail=[{"msg": "ValueError: invalid thalach value"}]
            )
        return v

    @validator("exang")
    def validation_exang(cls, v):
        if v not in [0, 1, 2, 3]:
            raise HTTPException(
                status_code=400,
                detail=[{"msg": "ValueError: invalid exang value"}]
            )
        return v

    @validator("oldpeak")
    def validation_oldpeak(cls, v):
        if v < 0 or v > 10:
            raise HTTPException(
                status_code=400,
                detail=[{"msg": "ValueError: invalid oldpeak value"}]
            )
        return v

    @validator("slope")
    def validation_slope(cls, v):
        if v not in [0, 1, 2]:
            raise HTTPException(
                status_code=400,
                detail=[{"msg": "ValueError: invalid slope value"}]
            )
        return v

    @validator("ca")
    def validation_ca(cls, v):
        if v not in [0, 1, 2, 3]:
            raise HTTPException(
                status_code=400,
                detail=[{"msg": "ValueError: invalid ca value"}]
            )
        return v

    @validator("thal")
    def validation_thal(cls, v):
        if v not in [0, 1, 2]:
            raise HTTPException(
                status_code=400,
                detail=[{"msg": "ValueError: invalid cp value"}]
            )
        return v
