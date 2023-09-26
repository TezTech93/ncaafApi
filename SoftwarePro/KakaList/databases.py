import sqlite3 as sql
import datetime as dt
import pandas as pd

now = dt.datetime.now()
today = dt.date(now.year,now.month,now.day)

#Get Jobs
def getJobs(location):
    con = sql.connect("jobs.db")
    cur = con.cursor()
    rows =cur.execute("SELECT * from jobs where Location=?",([location]))
    df = pd.DataFrame(rows)
    print(df)
    return df

#Post Jobs
def postJobs(postClient,datetime,postContent,location):
    con =sql.connect("jobs.db")
    cur =con.cursor()
    try:
        cur.execute("CREATE TABLE jobs(ClientId text,PostTime text,Content text,Location text)")
    except:
        pass
    cur.execute("INSERT into jobs (ClientId,PostTime,Content,Location) VALUES(?,?,?,?)",(postClient,datetime,postContent,location))
    con.commit()
    con.close()

#Get Services
def getServices(location):
    con = sql.connect("Services.db")
    cur = con.cursor()
    cur.fetchall("SELECT from Services where location=()")

#Post Services
def postServices(postClient,datetime,postContent,location):
    con =sql.connect("Services.db")
    cur =con.cursor()
    try:
        cur.execute("CREATE table Services(ClientId text,PostTime text,Content text,Location text)")
    except:
        pass
    cur.execute("INSERT into Services (ClientId,PostTime,Content,Location) VALUES(?,?,?,?)",(postClient,datetime,postContent,location))
    con.commit()
    con.close()

#Get Events
def getEvents(location):
    con = sql.connect("Events.db")
    cur = con.cursor()
    rows = cur.fetchall("SELECT * Events")
    print(rows)
    

#Post Events
def postEvents(postClient,datetime,postContent,location):
    con =sql.connect("Events.db")
    cur =con.cursor()
    try:
        cur.execute("CREATE table Events(ClientId text,PostTime text,Content text,Location text)")
    except:
        pass
    cur.execute("INSERT into Events (ClientId,PostTime,Content,Location) VALUES(?,?,?,?)",(postClient,datetime,postContent,location))
    con.commit()
    con.close()

getJobs("money")