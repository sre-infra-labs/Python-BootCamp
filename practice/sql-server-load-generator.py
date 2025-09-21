import pyodbc
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.delay = delay
    def run(self):
        #print ("Starting " + self.threadID)
        stall_sql_server(self.delay)
        #print ("Exiting " + self.threadID)

# Define a function for the thread
def stall_sql_server( delay ):
    cnxn = pyodbc.connect('Driver={SQL Server};'
                        'Server=localhost;'
                        'Database=StackOverflow;'
                        'Trusted_Connection=yes;'
                        'APP=sql-server-load-generator.py')
    cursor = cnxn.cursor()

    # Sample Query
    cursor.execute("SELECT @@version; WAITFOR DELAY '00:30:00'") 
    row = cursor.fetchone() 
    while row: 
        print(row[0])
        row = cursor.fetchone()

# Create 2 threads
#thread1 = myThread(1, 10)
#thread2 = myThread(2, 10)
counter = 1
while counter <= 40:
    myThread(counter, 10).start()
    counter += 1

# Start new Threads
#thread1.start()
#thread2.start()

print("Exiting Main Thread")