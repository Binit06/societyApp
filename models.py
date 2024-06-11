from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    parkedCount = db.Column(db.Integer())
    livingstatus = db.Column(db.String())
    mainainencecharges = db.Column(db.Integer())

    def __init__(self, id, name, parkedCount, livingStatus, maintainencecharges):
        self.id = id
        self.name = name
        self.parkedCount = parkedCount
        self.livingStatus = livingStatus
        self.maintainenececharges = maintainencecharges

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, parkedCount={self.count}, livingStatus={self.livingstatus}, maintenanceCharges={self.mainainencecharges})>"
