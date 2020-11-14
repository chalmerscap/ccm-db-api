import os
import pymysql
import logging
import traceback
import json


endpoint = os.environ['ENDPOINT']
dbuser = os.environ['DBUSER']
password = os.environ['PASSWORD']
port = os.environ['PORT']
database = os.environ['DATABASE']

logger=logging.getLogger()
logger.setLevel(logging.INFO)


def make_connection():
    return pymysql.connect(host=endpoint, user=dbuser, passwd=password,
        port=int(port), db=database, autocommit=True)


def log_err(errmsg):
    logger.error(errmsg)
    return {"body": errmsg , "headers": {}, "statusCode": 400,
        "isBase64Encoded":"false"}


logger.info("Cold start complete.") 


def handler(event,context):

    instrument = event["queryStringParameters"]['instrument']
    first = event["queryStringParameters"]['first']
    last = event["queryStringParameters"]['last']

    query =  '''SELECT * FROM Prices 
                WHERE instrumentId = (SELECT instrumentId FROM instruments WHERE (yahoo = '{}')) 
                AND (date >= STR_TO_DATE('{}', '%Y-%m-%d'))
                AND (date <= STR_TO_DATE('{}', '%Y-%m-%d'));'''.format(instrument, first, last)
                
    # query = "SELECT * FROM instruments"

    try:
        cnx = make_connection()
        cursor=cnx.cursor()
        
        try:
            cursor.execute(query)
            
        except:
            return log_err ("ERROR: Cannot execute cursor, check query.\n{}".format(
                traceback.format_exc()) )

        try:
            headers = [str(header[0]) for header in cursor.description]
            
            results_list=[]
            for result in cursor: 
                results_list.append(dict(zip(headers, result)))
            # print(results_list)
            cursor.close()
                   

        except:
            return log_err ("ERROR: Cannot parse query data.\n{}".format(
                traceback.format_exc()))


        return {"body": json.dumps(results_list, default=str), "headers": str(headers), "statusCode": 200,
        "isBase64Encoded":"false"}

    
    except:
        return log_err("ERROR: Cannot connect to database from handler.\n{}".format(
            traceback.format_exc()))


    finally:
        try:
            return fetched
            cnx.close()
        except: 
            pass 


if __name__== "__main__":
    handler(None,None)