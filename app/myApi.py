import json
import os
import psycopg2
import psycopg2.extras
import logging
from flask import Flask, request, jsonify
from flask.logging import create_logger
#install the "pip install flask-cor" module/library
from flask_cors import CORS, cross_origin #needed to install this over COR header issues


hostname = '10.0.14.10'
database = 'moviedotis'
username = 'root'
pwd = 'PostGres14'
port_id = 5432
conn = None
cur = None

app = Flask(__name__)
LOG = create_logger(app)
#Part of the CORS remediation initiative
CORS(app)


# Set up application and dynamically determine the path that this script is running in
script_dir = os.path.dirname(os.path.realpath(__file__))
logging.basicConfig(filename=f'{script_dir}/filename.log', level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
LOG.info(f"script directory: {script_dir}")
LOG.info(f"DB file: {script_dir}/db.txt")

# Create endpoints
# http://127.0.0.1:5000/


@app.route('/')
def index():
    response = jsonify({'Test transmission':'Let Nelson know it works',
                        'Favorite Ice Cream': 'Ben & Jerrys Americone Dream',
                        'Defaul Webite': 'www.google.com'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# GET http://127.0.0.1:5000/movies?name=Oscar


@app.route('/films', methods=['GET'])
def getRouter():
    try:
        movies = request.args.get('movies')
        print(movies)
        if (movies is None) or (movies == ""):
            LOG.warning('No specified movies, warning')
            raise ValueError
        records = json.loads(data)
        for record in records:
                if record['movies'] == movies:
                    LOG.info('Movies returned')
                    response = jsonify(record)
                    response.headers.add('Access-Control-Allow-Origin', '*')
                    return response, 200
        '''try:
        conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id)
    
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)'''
    except ValueError:
        LOG.error("NO HOSTNAME SPECIFIED, MAN")
        response = jsonify({'Message':'This World Is Awesome!'}) 
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 200
    except Exception as err:
        LOG.error(f'Error during GET {err}')
        response = jsonify({"error": err}), 500
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 500
    
# POST http://127.0.0.1:5000/routers



    
# Run the app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2000)



