from . import db
from datetime import datetime

class Todo(db.Model):
    __tablename__ = 'todo'

    todo_id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(255), nullable=False)
    created = db.Column(db.DateTime, default=lambda: datetime.now())
    status = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'"{self.task}" task created on {self.created}'