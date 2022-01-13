from . import database
from sqlalchemy import String, Integer, Column

Base = database.Base


class Record(Base):
    __tablename__ = 'records'
    id = Column(Integer, primary_key=True, autoincrement=True)
    dbn = Column(String, nullable=False)
    school_name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    total_enrolments = Column(Integer, nullable=True)
    grade_k = Column(Integer, nullable=True)
    grade_1 = Column(Integer, nullable=True)
    grade_2 = Column(Integer, nullable=True)
    grade_3 = Column(Integer, nullable=True)
    grade_4 = Column(Integer, nullable=True)
    grade_5 = Column(Integer, nullable=True)
    grade_6 = Column(Integer, nullable=True)
    grade_7 = Column(Integer, nullable=True)
    grade_8 = Column(Integer, nullable=True)
    female = Column(Integer, nullable=True)
    male = Column(Integer, nullable=True)
    asian = Column(Integer, nullable=True)
    black = Column(Integer, nullable=True)
    hispanic = Column(Integer, nullable=True)
    white = Column(Integer, nullable=True)
    other = Column(Integer, nullable=True)
    ell_spanish = Column(Integer, nullable=True)
    ell_chinese = Column(Integer, nullable=True)
    ell_bengali = Column(Integer, nullable=True)
    ell_arabic = Column(Integer, nullable=True)
    ell_haitian_creole = Column(Integer, nullable=True)
    ell_french = Column(Integer, nullable=True)
    ell_russian = Column(Integer, nullable=True)
    ell_korean = Column(Integer, nullable=True)
    ell_urdu = Column(Integer, nullable=True)
    ell_other = Column(Integer, nullable=True)
    ela_takers = Column(Integer, nullable=True)
    ela_level_1 = Column(Integer, nullable=True)
    ela_level_2 = Column(Integer, nullable=True)
    ela_level_3 = Column(Integer, nullable=True)
    ela_level_4 = Column(Integer, nullable=True)
    math_takers = Column(Integer, nullable=True)
    math_level_1 = Column(Integer, nullable=True)
    math_level_2 = Column(Integer, nullable=True)
    math_level_3 = Column(Integer, nullable=True)
    math_level_4 = Column(Integer, nullable=True)

    def __repr__(self):
        return f"<Record dbn={self.dbn} school_name={self.school_name}>"
