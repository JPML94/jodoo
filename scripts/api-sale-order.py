from xmlrpc import client

url = ""
db = ""
username = "admin"
password = "admin"

common = client.ServerProxy('{}/xmlrpc/2/common'.format(url))
common.version()
uid = common.authenticate(db, username, password, {})
models = client.ServerProxy('{}/xmlrpc/2/object'.format(url))

sale_order_id = models.execute_kw(db, uid, password, 'sale.order', 'create', [{
	'partner_id':7,
	'state':'draft',
  'note': 'TEST',
  'warehouse_id':2,
}])

print (sale_order_id) 
