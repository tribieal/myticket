import MySQLdb
import traceback
from DBUtils.PooledDB import PooledDB

class QueryResult:
    def __init__(self):
        self.lastrowid = 0
        self.res = None
        self.ret = 0

class Task:
    def __init__(self, taskName = "normal"):
        self.name = taskName
        self.sqlQueue = []
    
    
    def append(self, sql):
        self.sqlQueue.append(sql)

class log_fun:
    def __init__(self):
        pass
    def func( self, type, msg ):
        print type + '\t' + msg
    def __getattr__(self, funname):
        def foo( msg ):
            return self.func( funname, msg )
        return foo
         


class DBOperator:
    def __init__(self, app, pool_size, host, user, passwd, db, port = 3306):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.port = port 
        self.pool_size = pool_size
        self.app = app
      #  self.log = log_fun()
        self.FloodPool()


    def FloodPool(self):
        args = (0, self.pool_size, 0, 0, True, None, None, None)
        kwargs = {'host' : self.host, 'port': self.port, 'user' : self.user, 'passwd' : self.passwd, 'db' : self.db}
        try:
            self.pool = PooledDB(MySQLdb, *args, **kwargs) 
        except:
       #     self.log.critical("SQLFATAL Failed to connect MYSQL Server")
            return 0
     #   self.log.info("SUCC: Connecting to %s@%s " %(self.db, self.host))
        return 1
    
    
    def execute(self, sql):
        db = self.pool.connection()
        cursor = db.cursor()
        sqlRet = 0
        ret = QueryResult()
        try:
            sqlRet = cursor.execute(sql)
        except:
       #     self.log.error(traceback.print_exc())
        #    self.log.error("SQLERROR Failed to exec %s" %(sql))
            cursor.close()
            db.close()
            return ret
        msg = '%s: (%s) Return: %d' %(self.app, sql, sqlRet)
       # self.log.info(msg)
        ret.lastrowid = cursor.lastrowid
        ret.res = cursor.fetchall()
        ret.ret = sqlRet
        db.commit()
        cursor.close()
        db.close()
        return ret


    def __hasMissSomeone(self, value):
        sensitive = "\"\'\\"
        ll = len(value)
        i = 0
        while i < ll:
            if value[i] == '\\':
                i = i+2
                continue
            if value[i] in sensitive:
                return True
            i = i+1
        return False

    def escapeString(self, val, force = False):
        if force or self.__hasMissSomeone(val):
            return MySQLdb.escape_string(val)
        return val
    
