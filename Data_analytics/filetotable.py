import pandas as pd
from sqlalchemy import create_engine
connection_string = 'mysql+pymysql://root:root@localhost:3306/pandasexample1r'
engine = create_engine(connection_string)
files = ['artist', 'canvas_size', 'image_link', 'museum_hours', 'museum', 'product_size', 'subject', 'work']
for file in files:
    pat = rf"C:\Users\ALWIN JOSHUA\PycharmProjects\pythonProject\Data_analytics\famous_paintings\{file}.csv"
    df = pd.read_csv(pat)
    df.to_sql(file, con=connection_string, if_exists='replace',index=False)