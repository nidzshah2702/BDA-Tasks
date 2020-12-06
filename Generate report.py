import pymysql
from fpdf import FPDF
# Open database connection
db = pymysql.connect("localhost","root","","devtask" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT * from jf_adm")

# Fetch a single row using fetchone() method.
data = cursor.fetchall()
print(data)
# disconnect from server
db.close()
#create pdf
pdf = FPDF()
pdf.set_font("Arial", size=12)
pdf.add_page()   
col_width = pdf.w / 6
row_height = pdf.font_size
#printing column names
column_name=['Branch_ID','Fellow_ID','Period_ID','Fact_No_Adm','Fact_Avg_Per']
for c in column_name:
    pdf.cell(col_width, row_height*2,txt=c, border=1)
pdf.ln(row_height*2)
#adding data
for row in data:
    for item in row:
        pdf.cell(col_width, row_height*1,txt=str(item), border=1)
    pdf.ln(row_height*1)
 #save pdf       
pdf.output('simple_table.pdf')