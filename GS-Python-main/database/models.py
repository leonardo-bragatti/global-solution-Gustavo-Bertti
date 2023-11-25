from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from database.__init__ import Base
from sqlalchemy import Sequence


        

class Equipe(Base):
    __tablename__ = "EQUIPE"
    id = Column(Integer, Sequence('equipe_id_seq'), primary_key=True, autoincrement=True)
    nome_equipe = Column(String(258), nullable=False)
    senha_equipe = Column(String(16), nullable=False)
    enfermeiro_id = Column(Integer, ForeignKey("ENFERMEIRO.id"), nullable=False)
    enfermeiro = relationship("Enfermeiro", back_populates="equipes")
    tecnicos = relationship("EquipeTecnicoAssociation", back_populates="equipe")
    is_active = Column(Boolean, default=True)

class EquipeTecnicoAssociation(Base):
    __tablename__ = 'equipe_tecnico_association'
    equipe_id = Column(Integer, ForeignKey('EQUIPE.id'), primary_key=True)
    tecnico_id = Column(Integer, ForeignKey('TECNICO.id'), primary_key=True)
    equipe = relationship("Equipe", back_populates="tecnicos")
    tecnico = relationship("Tecnico", back_populates="equipes")


class Enfermeiro(Base):
    __tablename__ = "ENFERMEIRO"
    id = Column(Integer, Sequence('enfermeiro_id_seq'), primary_key=True, autoincrement=True)
    nome = Column(String(258), nullable=False)
    coren = Column(Integer, nullable=False, unique=True)
    senha = Column(String(100), nullable=False)
    equipes = relationship("Equipe", back_populates="enfermeiro")

class Tecnico(Base):
    __tablename__ = "TECNICO"
    id = Column(Integer, Sequence('tecnico_id_seq'), primary_key=True, autoincrement=True)
    nome = Column(String(258), nullable=False)
    coren = Column(Integer, nullable=False, unique=True)
    equipes = relationship("EquipeTecnicoAssociation", back_populates="tecnico")



class Paciente(Base):
    __tablename__ = "PACIENTE"
    id = Column(Integer, Sequence('paciente_id_seq'), primary_key=True, autoincrement=True)
    cpf = Column(String(11), nullable=False, unique=True)
    nome = Column(String(258), nullable=False)
    dataNascimento = Column(DateTime, nullable=False)
    idade = Column(Integer, nullable=False)
    telefone = Column(String(50), nullable=False, unique=True)
    nas = relationship("Nas", back_populates="paciente")  # Corrigido para "nas"

class Nas(Base):
    __tablename__ = 'NAS'
    id = Column(Integer, Sequence('nas_id_seq'), primary_key=True, autoincrement=True)
    paciente_id = Column(Integer, ForeignKey('PACIENTE.id'))
    nota_nas = Column(Integer)
    complexidade = Column(String(255))  # Especifique um tamanho adequado
    paciente = relationship("Paciente", back_populates="nas")


