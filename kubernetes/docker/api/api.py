import os
import sys
from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import datetime
import logging
import json
import traceback
import time
import random
from sqlalchemy import create_engine
from sqlalchemy.schema import CreateTable
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Integer, String, Boolean, JSON
from sqlalchemy import func, ForeignKey, Sequence

#api setup
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.debug = True
CORS(app)
logging.basicConfig(level=logging.INFO)
#db connection
db_connect_str = 'postgres://postgres:postgres@db-svc:15432/test_db'
engine = None
db_session = None
#db table
Base = declarative_base()
class PersonModel(Base):
    __tablename__ = 'person'
    id = Column(Integer, Sequence('seq_person_id', start=1, increment=1), primary_key=True)
    name = Column(String)
try:
    time.sleep(5)
    engine = create_engine(db_connect_str, convert_unicode=True)
except:
    print(f'retry to {db_connect_str}')
    time.sleep(10)
    engine = create_engine(db_connect_str, convert_unicode=True)
print(f'connected to {db_connect_str}')
db_session = scoped_session(sessionmaker(autocommit=False,
                                        autoflush=False,
                                        bind=engine))
comment = '''
Base.metadata.create_all(bind=engine)
#CreateTable(PersonModel.__table__)
db_session.commit()
#db preset data
for i in range(20,30):
    db_session.add(PersonModel(
        name='preset',
        age=i
    ))
db_session.commit()
'''

iam = random.randint(0,1000)

@app.route('/api/whoami', methods=['GET'])
def whoami():
    return jsonify({'data':f'{iam}'})

@app.route('/api/update', methods=['POST'])
def insert():
    name = request.json['name']
    p = db_session.query(PersonModel).filter_by(id=1).first()
    p.name = name
    db_session.commit()
    return jsonify({'data':f'update {name}.'})

@app.route('/api/name', methods=['GET'])
def name():
    p = db_session.query(PersonModel).filter_by(id=1).first()
    return jsonify({'data':f'{p.name}'})

if __name__ == '__main__':
    host = sys.argv[1] if len(sys.argv) >= 2 else "localhost"
    port = int(sys.argv[2]) if len(sys.argv) >= 3 else 5000
    app.run(host=host, port=port)