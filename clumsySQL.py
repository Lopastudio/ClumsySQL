import sqlite3


class Database:
	def __init__(self, db_name):
		self.db_name = db_name
		self.connection = None
		self.cursor = None
		
	def connect(self):
		try:
			self.connection = sqlite3.connect(self.db_name)
			self.cursor = self.connection.cursor()
			print(f"Connected to database: {self.db_name}")
		except Exception as e:
			print(f"Connection failed: {e}")
			
	def disconnect(self):
		if self.connection:
			self.connection.close()
			print(f"Disconnected from database: {self.db_name}")
		else:
			print("No connection to database")
			
	def create_table(self):
		if self.connection:
			try:
				self.cursor.execute("""
					CREATE TABLE IF NOT EXISTS users (
						id INTEGER PRIMARY KEY,
						name TEXT,
						age INTEGER
					)
				""")
				print(f"Created table: {self.db_name}")
			except Exception as e:
				print(f"Error creating table: {e}")
		else:
			print("No connection to database")
			
	def insert_data(self, name, age):
		if self.connection:
			try:
				self.cursor.execute("""
					INSERT INTO users (name, age) VALUES (?, ?)
				""", (name, age))
				self.connection.commit()
				print("Inserted data to the table")
			except Exception as e:
				print(f"Error inesrting data: {e}")
		else:
			print("No connection to database")
			
	def get_data(self):
		if self.connection:
			try:
				self.cursor.execute("SELECT * FROM users")
				data = self.cursor.fetchall()
				print("Data retrieved from the tabel")
				for row in data:
					print(row)
				return data
			except Exception as e:
				print(f"Error retrieving data: {e}")
		else:
			print("No connection to database") 