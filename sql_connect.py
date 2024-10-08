import pyodbc

connection = pyodbc.connect('DRIVER={SQL Server};'+
                            'Server=Yathish\\SQLEXPRESS;'+
                            'Database=master;'+
                            'Trusted_Connection=True')
print('connected to database')
