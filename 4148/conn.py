import ibm_db
from flask import *

conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=2d46b6b4-cbf6-40eb-bbce-6251e6ba0300.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=32328;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=qgr18899;PWD=UFh1hS3kzhMz4j7n",'','')
print(conn)

app = Flask(__name__)