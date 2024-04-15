
from itemadapter import ItemAdapter
import sqlite3

class JumiaPipeline:
    
    def __init__(self):
        self.conn = sqlite3.connect('jumia_products.db')
        
        self.cursor = self.conn.cursor()
        
        self.create_table()
    
    def create_table(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS products (name TEXT, link TEXT, price TEXT, review TEXT)')
        
        
    def process_item(self, item, spider):
        self.cursor.execute('INSERT OR IGNORE INTO products (name, link, price, review) VALUES (?,?,?,?)',(item['product_name'],item['link'],item['price'],item['review']))
        self.conn.commit()
        
        return item
#JumiaPipeline()