import sqlite3
import logging


def print_whitespace():
	print()
	print()
	print()


class Database:
	def __init__(self, db_name):
		self.db_name = db_name
		self.connection = None
		self.cursor = None
	
	def connect(self):
		try:
			with sqlite3.connect(self.db_name) as connection:
				self.connection = connection
				self.cursor = connection.cursor()
			print(f"Connected to database: {self.db_name}")
		except sqlite3.Error as e:
			logging.error(f"Connection failed: {e}")
	
	def disconnect(self):
		if self.connection:
			self.connection.close()
			print(f"Disconnected from database: {self.db_name}")
		else:
			print("Not connected to the database.")
	
	def create_table(self, columns, table_name):
		if not self.connection:
			print("Not connected to the database. Please connect first.")
			return
		
		try:
			columns_str = ', '.join([f'{col} TEXT' if col != 'id' else f'{col} INTEGER' for col in columns])
			query = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})'
			self.cursor.execute(query)
			print(f"Table {table_name} created successfully.")
		except sqlite3.Error as e:
			logging.error(f"Error creating table: {e}")
	
	def insert_data(self, data, table_name):
		if not self.connection:
			print("Not connected to the database. Please connect first.")
			return
		
		try:
			columns = ', '.join(data.keys())
			values = ', '.join(['?' for _ in data.values()])
			query = f'INSERT INTO users ({columns}) VALUES ({values})'
			self.cursor.execute(query, tuple(data.values()))
			self.connection.commit()
			print("Inserted data into the table.")
		except sqlite3.Error as e:
			logging.error(f"Error inserting data: {e}")
	
	def get_data(self, table_name):
		if not self.connection:
			print("Not connected to the database. Please connect first.")
			return
		
		try:
			self.cursor.execute('SELECT * FROM sqlite_master WHERE type="table" AND name = ?', (table_name,))
			data = self.cursor.fetchall()
			if not data:
				print(f"Table {table_name} does not exist.")
				return
			
			self.cursor.execute(f'SELECT * FROM {table_name}')
			data = self.cursor.fetchall()
			print("Data retrieved from the table")
			for row in data:
				print(row)
			return data
		except sqlite3.Error as e:
			logging.error(f"Error retrieving data: {e}") 