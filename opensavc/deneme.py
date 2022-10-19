import pypyodbc

db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-AO5K0VF;'
    'Database=DbOkul;'
    'UID=sa;'
    'PWD=abc123;'
)

imlec = db.cursor()

numara = '12345678910'

query = f"INSERT INTO YOKLAMA1 (NUMARA, AD, BOLUM, FAKULTE, TARIH) SELECT  O.NUMARA, O.AD, O.BOLUM, O.FAKULTE, GETDATE() FROM OGRENCI O WHERE O.NUMARA = '{numara}'"

sonuc = imlec.execute(query)

db.commit()