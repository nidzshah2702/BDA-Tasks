
import json 
import collections
import pymysql
import xml.etree.ElementTree as ET
# Open database connection
db = pymysql.connect("localhost","root","","devtask" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT * from jd_branch_adm")

# Fetch a single row using fetchone() method.
data = cursor.fetchall()

# disconnect from server
db.close()

objects_list = []
for row in data:
    d = collections.OrderedDict()
    d['Branch_ID'] = row[0]
    d['Branch_CATEGORY'] = row[1]
    d['Branch_STREAM'] = row[2]
    objects_list.append(d)
j = json.dumps(objects_list)


objectarrays_file = 'branch_jsonfile.js'
#f = open(objectarrays_file,'w')
#f.write(j)
print(j)





# create the file structure
branches = ET.Element('branches')
for row in data:
    item=ET.SubElement(branches,'Branch')
    bid=ET.SubElement(item,'Branch_ID')
    bcategory=ET.SubElement(item,'Branch_CATEGORY')
    bstream=ET.SubElement(item,'Branch_STREAM')
    bid.text=str(row[0])
    bcategory.text=str(row[1])
    bstream.text=str(row[2])


# create a new XML file with the results
mydata = ET.tostring(branches)
print((mydata))
myfile = open("branches.xml", "w")
myfile.write(str(mydata))