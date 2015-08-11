"""dosql"""
import sys
import psycopg2
import cgi

class doSql(object):
    """class doSql"""
    #attributes
    _cxn = ""
    _cur = ""
    errmsg = ""
    #methods
    def __init__(self): #constructor
        self._cxn = psycopg2.connect("dbname='myEskwela' \
            user='postgres' password='postgres' host='127.0.0.1' port='5432'")
        self._cur = self._cxn.cursor()

    def __del__(self): #destructor
        self._cur.close()
        self._cxn.close()

    def execqry(self, sql, apply_):
        """execqry"""
        rows = []
        try:
            self._cur.execute(sql)
            rows = self._cur.fetchall()
            if apply_:
                self._cxn.commit()
            if self._cur.rowcount == 0:
                rows.append(['None'])
        except:
            #errmsg = sys.exc_type + ":" + sys.exc_value
            errmsg = str(sys.exc_info()[1])
            rows.append([errmsg])
        return rows

    # From Ron Daryl Magno
    def buildqry(self, stored_proc, *args):
        """buildqry"""
        query = ''
        for arg in args:
            arg = cgi.escape(arg)
            query += "'" + arg + "',"

        # Remove the last character which is the comma ','
        query = query[:-1]
        query = stored_proc + '(' + query + ')'
        return query

    # From Ron Daryl Magno
    def parse_result(self, result):
        """parse_result"""
        rets = []
        for ret in result:
            stringed = map(str, ret)
            rets.append(stringed)

        return rets[0][0]



#a = doSql()
#f = a.execqry("select insupattendance\
    #('1321', 'CENG1-LEC', getcurrsem(),\
    # now()::timestamp without time zone, true)")[0][0]
#print f
#del a
