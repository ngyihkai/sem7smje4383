import cgi, shelve, sys, os
shelvenames = 'class-shelve'
fieldnames = ('name', 'age', 'job', 'pay')

form = cgi.FieldStorage()
print('Content-type: text/html')
sys.path.insert(0, os.getcwd())

# main html template
replyhtml = """
<html>
<title>People Input Form</title>
<body>
<form method = POST action = "peoplecgi.py">
    <table>
    <tr><th>key<td><input type = text name = key value = "%(key)s">
    $ROWS$
    </table>
    <p>
    <input type = submit value = 'Fetch', name = action>
    <input type = submit value = 'Update', name = action>
</form>
</body></html>
"""

# insert html for data rows at $ROWS$
rowhtml = '<tr><th>%s<td><input type = text name = %s value = "%%(%s)s">\n'
rowshtml = ''
for fieldname in fieldnames:
    rowshtml += (rowhtml % ((fieldname,) * 3))
