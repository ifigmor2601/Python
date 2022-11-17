import cx_Oracle

# Realizamos la conexión con la base de datos
dsn = cx_Oracle.makedsn(host='localhost', port=1521, sid='xe')
conn = cx_Oracle.connect(user='PY_USER', password='PY_USER', dsn=dsn)

# Declaramos un cursor para recorrer los resultados
c = conn.cursor()

# Establecemos el formato en que se mostrará la fecha en Oracle


# Función que crea una tabla de productos
def crearTabla():
    # Generamos la sentencia que crea la tabla
    sentencia = "CREATE TABLE PRODUCTOS (ID_PRODUCTO CHAR(9) NOT NULL, NOMBRE VARCHAR2(50) NOT NULL, PRECIO FLOAT, STOCK NUMBER(6), FIN_OFERTA DATE, DESCRIPCION LONG, CONSTRAINT PRODUCTOS_PK PRIMARY KEY  (ID_PRODUCTO))"
    
    # Ejecutamos la sentencia
    c.execute(sentencia)
    
    # Realizamos un commit para confirmar los cambios
    conn.commit()
    
    print("TABLA CREADA")
    
    
# Función que inserta un producto en la tabla productos
def insertar(id_prod,nombre,precio,stock,fin_oferta,descripcion):
    
    #Ejecutamos la sentencia correspondiente
    sentencia = "insert into productos values(:id_prod , :nombre, :precio, :stock, :fin_oferta, :descripcion)"
    c.execute(sentencia,[id_prod,nombre,precio,stock,fin_oferta,descripcion])
    conn.commit()
    
    print("INSERTADO")
    
def alter():
    c.execute("alter session set nls_date_format = 'DD/MM/YYYY hh24:mi'")


    