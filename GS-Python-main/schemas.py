import re
from typing import List
from datetime import datetime
from pydantic import BaseModel, validator

class EquipeLogin(BaseModel):
    email: str
    senha: str

    @validator('email')
    def validate_email(cls, value):
        if not re.match('^([a-z]|[0-9]|@)+$', value):
            raise ValueError('Email format invalid')
        return value

class PacienteCreate(BaseModel):
    cpf: str
    nome: str
    dataNascimento: datetime
    idade: int
    telefone: str

class NasCreate(BaseModel):
    data: datetime
    descricaoMedico: str
    valorResultado: float
    paciente: PacienteCreate

class EquipeCreate(BaseModel):
    id: int
    nome: str
    email: str
    enfermeiro: str
    tecnico: str
    senhaEquipe: str
    nas: NasCreate

class FuncionarioCreate(BaseModel):
    id: int
    nome: str
    coren: int

class EnfermeiroCreate(BaseModel):
    id: int
    nome: str
    coren: int
    senha: str

class TecnicoCreate(BaseModel):
    id: int
    nome: str
    coren: int

class EscalaCreate(BaseModel):
    id: int
    equipe: EquipeCreate

class Equipe(BaseModel):
    id: int
    nome: str
    email: str
    enfermeiro: str
    tecnico: str
    senhaEquipe: str
    nas: NasCreate
    is_active: bool

    class Config:
        orm_mode = True

class Diabetes(BaseModel):
    id: int
    glicemia: float
    frequenciaCardiaca: float
    pressaoArterialSistolica: float
    temperatura: float
