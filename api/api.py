import os
import sys
from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime
import logging
import json
import traceback
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.debug = True
CORS(app)
logging.basicConfig(level=logging.INFO)

db_connect_str = 'postgres://postgres:postgres@db-container:15432/test_db'
engine = create_engine(db_connect_str, convert_unicode=True)
print(f'connected to {db_connect_str}')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

@app.route('/insert', methods=['POST'])
def insert():
    return jsonify({'ok': True})

if __name__ == '__main__':
    host = sys.argv[1] if len(sys.argv) >= 2 else "localhost"
    port = int(sys.argv[2]) if len(sys.argv) >= 3 else 7000
    app.run(host=host, port=port)