import mintapi
import pandas
import pickle
import datetime
 #--- PW stuffs
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import pw
#--- PW Stuffs

ius_session = '0D729971F8014D46AFAE78535BA5EE5F'
thx_guid = 'ECA2581CD1B3B676'
hashPass = '$2a$12$uYo5vRt16.l62v2RsuHeJ.p0VG4IG558i/R5XDdmyDBpWzBt.vxJO'
salt = 	   '$2a$12$uYo5vRt16.l62v2RsuHeJ.'

def outpt():
	filehandler = open('mint.pi', 'r') 
	mintObj = pickle.load(filehandler)
	print mintObj.get_net_worth()

def getAccounts():
	filehandler = open('accounts.pi', 'r') 
	accts = pickle.load(filehandler)
	print len(accts)
	for account in accts:
		print account['accountName'] + ':' + str(account['currentBalance'])

def code(doneBefore):
	if not doneBefore:
		mint = mintapi.Mint(pw.getUser(), pw.getPass())#, ius_session, thx_guid)
		filehandler = open('accounts.pi', 'w') 
		pickle.dump(mint.get_accounts(), filehandler)
	getAccounts()
try:
	 code(True)
except Exception as e:
 	print e
