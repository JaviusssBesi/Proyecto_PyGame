from PyQt5 import QtSql
import var
from datetime import date
from datetime import datetime

class Conexion():
    def db_connect(filename):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(filename)
        if not db.open():
            print('No se puede abrir la base de datos')
            return False
        else:
            print('Conexión Establecida')
        return True

    def altaJug(jugador):
        query = QtSql.QSqlQuery()
        query.prepare('insert into puntuacion (nombre, puntuacion, fecha)')
        query.bindValue(':nombre', str(jugador[0]))
        query.bindValue(':puntuacion', str(jugador[1]))
        query.bindValue(':fecha', str(jugador[2]))
        if query.exec_():
            print("Inserción Correcta")
        else:
            print("Error: ", query.lastError().text())

    def cargarJug():
        nombre = var.ui.editDni.text()
        query = QtSql.QSqlQuery()
        query.prepare('select * from puntuacion where nombre = :nombre')
        query.bindValue(':nombre', nombre)
        if query.exec_():
            while query.next():
                var.ui.lblCodcli.setText(str(query.value(0)))
                var.ui.editClialta.setText(query.value(4))
                var.ui.editDir.setText(query.value(5))
                var.ui.cmbProv.setCurrentText(str(query.value(6)))


    def mostrarClientes(self):
        '''
        Carga los datos principales del cliente en la tabla
        se ejecuta cuando lanzamos el programa, actualizamos, insertamos y borramos un cliente
        :return: None
        '''
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select dni, apellidos, nombre from clientes')
        if query.exec_():
            while query.next():
                #cojo los valores
                dni = query.value(0)
                apellidos = query.value(1)
                nombre = query.value(2)
                # crea la fila
                var.ui.tableCli.setRowCount(index+1)
                #voy metiendo los datos en cada celda de la fila
                var.ui.tableCli.setItem(index,0, QtWidgets.QTableWidgetItem(dni))
                var.ui.tableCli.setItem(index, 1, QtWidgets.QTableWidgetItem(apellidos))
                var.ui.tableCli.setItem(index, 2, QtWidgets.QTableWidgetItem(nombre))
                index += 1
        else:
            print("Error mostrar clientes: ", query.lastError().text())

