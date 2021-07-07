import mysql.connector

mydb = mysql.connector.connect(
    host="167.71.84.108",
    user="usersql",
    password="#SQLqsenha123",
    database="pan"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS roteamento (id INT AUTO_INCREMENT PRIMARY KEY, ownerIdentity VARCHAR(50), identity VARCHAR(100), contactIdentity VARCHAR(100), messageId VARCHAR(100), storageDate TIMESTAMP, category VARCHAR(50), action VARCHAR(50), stateId VARCHAR(100), stateName VARCHAR(50), previousStateId VARCHAR(100), previousStateName VARCHAR(50));")

mycursor.execute("CREATE TABLE IF NOT EXISTS conversa (id INT AUTO_INCREMENT PRIMARY KEY, type VARCHAR(50), scope	VARCHAR(30), text TEXT, option1Text VARCHAR(30), option1Type VARCHAR(30), option1Value VARCHAR(30), option2Text	VARCHAR(30), option2Type VARCHAR(30), option2Value VARCHAR(30), option3Text	VARCHAR(30), option3Type VARCHAR(30), option3Value VARCHAR(30), idTake VARCHAR(100), `from` VARCHAR(100), `to`  VARCHAR(100), StateName VARCHAR(100), stateId VARCHAR(100), messageId VARCHAR(100), previousStateId VARCHAR(100), previousStateName VARCHAR(100), uber_trace_id	VARCHAR(100), uniqueId VARCHAR(100), tunnelOriginalFrom VARCHAR(100), tunnelOriginalTo VARCHAR(100), messageKind VARCHAR(30), storageDate TIMESTAMP, date_created TIMESTAMP);")

mycursor.execute("CREATE TABLE IF NOT EXISTS identidade (id INT AUTO_INCREMENT PRIMARY KEY, lastMessageDate TIMESTAMP, identity VARCHAR(100),	isNewUser BOOLEAN, name	VARCHAR(100), cpf VARCHAR(15),	email VARCHAR(50),	phone VARCHAR(15),	city VARCHAR(30), 	gender VARCHAR(30), faqOption VARCHAR(50), tunnelOwner VARCHAR(50), source VARCHAR(50));")
