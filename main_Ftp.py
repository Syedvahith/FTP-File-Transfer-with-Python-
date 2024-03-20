import ftplib
FTP_HOST="ftp.dlptest.com"
FTP_USER="dlpuser"
FTP_PASS = "rNrKYTX9g7z3RgJRmxWuGHbeu"

#connect to the FTP server
ftp=ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
#force UTF-8 encoding
ftp.encoding="utf-8"

# Local file nome you want to upload
filename="test_FTP.jpg"
with open(filename, "rb") as file:
#use FTP's STOR command to upload the file 
	ftp.storbinary("STOR test_FTP.jpg", file)

#List current files and directory
ftp.dir()

#the name of file you want to download from the FTP server
filename = 'test_FTP.jpg'
with open(filename, "wb") as file:
# use FTP's RETR command to download the file
	ftp.retrbinary("RETR test_FTP.jpg", file.write)
