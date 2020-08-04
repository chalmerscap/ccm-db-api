import mysql.connector


class CCM_db:

	def __init__(self, password)

		self.cnx, self.cursor = self.open_connection()


	def open_connection():
	    cnx = mysql.connector.connect(
	    host="185.51.226.6",
	    user="CCM",
	    passwd=password,
	    database="CCM"
	    )
	    cursor = cnx.cursor()

	    return cnx, cursor


	def close_connection(cnx, cursor, commit):
	    if commit == 1:
	        cnx.commit()
	    cursor.close()
	    cnx.close()
