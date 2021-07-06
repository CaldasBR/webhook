import mysql.connector

mydb = mysql.connector.connect(
    host="167.71.84.108",
    user="usersql",
    password="#SQLqsenha123",
    database="pan"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE roteamento (id INT AUTO_INCREMENT PRIMARY KEY, ownerIdentity VARCHAR(50), identity VARCHAR(100), contactIdentity VARCHAR(100), messageId VARCHAR(100), storageDate TIMESTAMP DEFAULT 0, category VARCHAR(50), action VARCHAR(50), stateId VARCHAR(100), stateName VARCHAR(50), previousStateId VARCHAR(100), previousStateName VARCHAR(50);")
