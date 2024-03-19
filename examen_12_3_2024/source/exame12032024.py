import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget,
                             QLabel, QListWidget, QPushButton, QComboBox,  QLineEdit,
                             QRadioButton, QGroupBox, QTableView, QAbstractItemView)
from modeloTaboa import ModeloTaboa
from conexionBD   import ConexionBD



class FiestraPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exame 12-03-2024")

        self.estado= 'None'


        caixaV = QVBoxLayout()
        grid = QGridLayout()


        gpbCliente = QGroupBox("Cliente")
        gpbCliente.setLayout(grid)
        caixaV.addWidget(gpbCliente)

        lblNumeroCliente = QLabel("Número Cliente")
        lblNomeCliente = QLabel("Nome")
        lblApelidosCliente = QLabel("Apelidos")
        lblDirección = QLabel("Dirección")
        lblCidade = QLabel("Cidade")
        lblProvinciaEstado = QLabel("Provincia")
        lblCodigoPostal = QLabel("Código postal")
        lblTelefono = QLabel("Teléfono")
        lblPais = QLabel ("País")
        lblAxenteComercial = QLabel("AxenteComercial")
        self.txtNumeroCliente = QLineEdit()
        self.txtNomeCliente = QLineEdit()
        self.txtApelidosCliente = QLineEdit()
        self.txtDireccion = QLineEdit()
        self.txtCidade = QLineEdit()
        self.txtProvinciaEstado = QLineEdit()
        self.txtCodigoPostal = QLineEdit()
        self.txtTelefono = QLineEdit()
        self.txtPais = QLineEdit()
        self.txtAxenteComercial = QLineEdit()


        grid.addWidget(lblNumeroCliente, 0,0,1,1)
        grid.addWidget(self.txtNumeroCliente, 0, 1, 1, 1)
        grid.addWidget(lblNomeCliente, 0,2,1,1)
        grid.addWidget(self.txtNomeCliente, 0, 3, 1, 1)
        grid.addWidget(lblApelidosCliente, 2,0,1,1)
        grid.addWidget(self.txtApelidosCliente, 2,1,1,3)
        grid.addWidget(lblDirección, 3,0,1,1)
        grid.addWidget(self.txtDireccion, 3,1,1,3)
        grid.addWidget(lblCidade,4, 0, 1,1)
        grid.addWidget(self.txtCidade, 4, 1, 1,1)
        grid.addWidget(lblProvinciaEstado, 4,2, 1,1)
        grid.addWidget(self.txtProvinciaEstado, 4,3, 1,1)
        grid.addWidget(lblCodigoPostal, 5,0,1,1)
        grid.addWidget(self.txtCodigoPostal, 5,1,1,1)
        grid.addWidget(lblTelefono, 5, 2, 1, 1)
        grid.addWidget(self.txtTelefono, 5, 3, 1, 1)
        grid.addWidget(lblPais,6,0,1,1)
        grid.addWidget(self.txtPais,6,1,1,1)
        grid.addWidget(lblAxenteComercial,6,2,1,1)
        grid.addWidget(self.txtAxenteComercial,6,3,1,1)


        caixaHTaboa = QHBoxLayout()


        self.tvwClientes = QTableView()
        self.tvwClientes.verticalHeader().hide()
        self.tvwClientes.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tvwClientes.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        caixaHTaboa.addWidget(self.tvwClientes)
        conxBD = ConexionBD("modelosClasicos.dat")
        conxBD.conectaBD()
        conxBD.creaCursor()

        clientes = conxBD.consultaSenParametros("Select * from clientes")
        conxBD.pechaBD()

        self.modelo = ModeloTaboa(clientes)
        self.tvwClientes.setModel(self.modelo)
        self.seleccion = self.tvwClientes.selectionModel()
        self.seleccion.selectionChanged.connect(self.on_modelo_selectionChanged)



        self.btnEngadir = QPushButton("Engadir")
        self.btnEngadir.setEnabled(True)
        self.btnEngadir.pressed.connect(self.on_btnEngadir_pressed)
        self.btnEditar = QPushButton("Editar")
        self.btnEditar.setEnabled(False)
        self.btnEditar.pressed.connect(self.on_btnEditar_pressed)
        self.btnBorrar = QPushButton("Borrar")
        self.btnBorrar.setEnabled(False)
        self.btnBorrar.pressed.connect(self.on_btnBorrar_pressed)

        caixaBotonsCorreo = QVBoxLayout()
        caixaBotonsCorreo.setAlignment(Qt.AlignmentFlag.AlignTop)
        caixaBotonsCorreo.addWidget(self.btnEngadir)
        caixaBotonsCorreo.addWidget(self.btnEditar)
        caixaBotonsCorreo.addWidget(self.btnBorrar)

        caixaHTaboa.addLayout(caixaBotonsCorreo)

        caixaV.addLayout(caixaHTaboa)

        caixaBtnAceptar = QHBoxLayout()
        self.btnAceptar = QPushButton("Aceptar")
        self.btnAceptar.pressed.connect(self.on_btnAceptar_pressed)
        self.btnCancelar = QPushButton("Cancelar")
        self.btnCancelar.pressed.connect(self.on_btnCancelar_pressed)
        caixaBtnAceptar.setAlignment(Qt.AlignmentFlag.AlignRight)
        caixaBtnAceptar.addWidget(self.btnCancelar)
        caixaBtnAceptar.addWidget(self.btnAceptar)
        caixaV.addLayout(caixaBtnAceptar)


        contedor = QWidget()

        contedor.setLayout(caixaV)

        self.setCentralWidget(contedor)

        #self.setFixedSize (400,300)
        self.show()

    def on_btnEngadir_pressed(self):
        self.estado = 'Engadir'
        self.borrarCampos()
        self.btnEngadir.setEnabled(False)
        self.btnEditar.setEnabled(False)
        self.btnBorrar.setEnabled(False)


    def on_btnEditar_pressed(self):

        if self.seleccion.hasSelection():
            self.estado = 'Editar'
            self.cargarCamposDendeSeleccion()
            self.btnEngadir.setEnabled(False)
            self.btnEditar.setEnabled(False)
            self.btnBorrar.setEnabled(False)

    def on_btnBorrar_pressed(self):

        if self.seleccion.hasSelection():
            self.estado ="Borrar"
            self.cargarCamposDendeSeleccion()
            self.btnEngadir.setEnabled(False)
            self.btnEditar.setEnabled(False)
            self.btnBorrar.setEnabled(False)


    def on_btnAceptar_pressed(self):
        if self.estado == 'Engadir':
            conxBD = ConexionBD("modelosClasicos.dat")
            conxBD.conectaBD()
            conxBD.creaCursor()
            conxBD.engadeRexistro("""INSERT INTO clientes (numeroCliente, nomeCliente, apelidosCliente, telefono, direccion, cidade, provinciaEstado, codigoPostal, pais, axenteComercial)
                                           VALUES (?,?,?,?,?,?,?,?,?,?)""",
                                  int(self.txtNumeroCliente.text()),
                                  self.txtNomeCliente.text(),
                                  self.txtApelidosCliente.text(),
                                  self.txtTelefono.text(),
                                  self.txtDireccion.text(),
                                  self.txtCidade.text(),
                                  self.txtProvinciaEstado.text(),
                                  self.txtCodigoPostal.text(),
                                  self.txtPais.text(),
                                  int(self.txtAxenteComercial.text()))
            self.modelo.datos.append((int(self.txtNumeroCliente.text()),
                                      self.txtNomeCliente.text(),
                                      self.txtApelidosCliente.text(),
                                      self.txtTelefono.text(),
                                      self.txtDireccion.text(),
                                      self.txtCidade.text(),
                                      self.txtProvinciaEstado.text(),
                                      self.txtCodigoPostal.text(),
                                      self.txtPais.text(),
                                      int(self.txtAxenteComercial.text())))
            self.modelo.layoutChanged.emit()

        elif self.estado == 'Borrar':
            filas = self.seleccion.selectedRows()
            for fila in filas:
                i = fila.row()
                conxBD = ConexionBD("modelosClasicos.dat")
                conxBD.conectaBD()
                conxBD.creaCursor()
                conxBD.borraRexistro("DELETE FROM clientes WHERE numeroCliente = ?", self.modelo.datos[i][0] )
                del (self.modelo.datos[i])
                self.modelo.layoutChanged.emit()

        elif self.estado == 'Editar':
            filas =self.seleccion.selectedRows()
            for fila in filas:
                i = fila.row()
                conxBD = ConexionBD("modelosClasicos.dat")
                conxBD.conectaBD()
                conxBD.creaCursor()
                conxBD.actualizaRexistro("""UPDATE clientes SET 
                                                nomeCliente = ?,
                                                apelidosCliente = ?,
                                                telefono = ?,
                                                direccion = ?,
                                                cidade = ?,
                                                provinciaEstado = ?,
                                                codigoPostal = ?,
                                                pais = ?,
                                                axenteComercial = ?
                                            Where numeroCliente = ?""",
                                              self.txtNomeCliente.text(),
                                              self.txtApelidosCliente.text(),
                                              self.txtTelefono.text(),
                                              self.txtDireccion.text(),
                                              self.txtCidade.text(),
                                              self.txtProvinciaEstado.text(),
                                              self.txtCodigoPostal.text(),
                                              self.txtPais.text(),
                                              int(self.txtAxenteComercial.text()),
                                              int(self.txtNumeroCliente.text())
                                            )
                self.modelo.datos [i] = (
                self.modelo.datos[i][0],
                self.txtNomeCliente.text(),
                self.txtApelidosCliente.text(),
                self.txtTelefono.text(),
                self.txtDireccion.text(),
                self.txtCidade.text(),
                self.txtProvinciaEstado.text(),
                self.txtCodigoPostal.text(),
                self.txtPais.text(),
                int(self.txtAxenteComercial.text())
                )
                self.modelo.layoutChanged.emit()

        self.seleccion.clear()
        self.borrarCampos()
        self.estado= 'None'
        self.btnEngadir.setEnabled(True)
    def on_btnCancelar_pressed(self):
        self.seleccion.clear()
        self.btnEngadir.setEnabled(True)
        self.btnEditar.setEnabled (False)
        self.btnBorrar.setEnabled(False)
        self.borrarCampos()


    def on_modelo_selectionChanged(self):
        self.btnEngadir.setEnabled(True)
        self.btnBorrar.setEnabled (True)
        self.btnEditar.setEnabled(True)


    def cargarCamposDendeSeleccion(self):
        filas = self.seleccion.selectedRows()
        for fila in filas:
            i = fila.row()
            self.txtNumeroCliente.setText(str(self.modelo.datos[i][0]))
            self.txtNomeCliente.setText(self.modelo.datos[i][1])
            self.txtApelidosCliente.setText(self.modelo.datos[i][2])
            self.txtTelefono.setText(self.modelo.datos[i][3])
            self.txtDireccion.setText(self.modelo.datos[i][4])
            self.txtCidade.setText(self.modelo.datos[i][5])
            self.txtProvinciaEstado.setText(self.modelo.datos[i][6])
            self.txtCodigoPostal.setText(self.modelo.datos[i][7])
            self.txtPais.setText(self.modelo.datos[i][8])
            self.txtAxenteComercial.setText(str(self.modelo.datos[i][9]))

    def borrarCampos(self):
        self.txtNumeroCliente.setText('')
        self.txtNomeCliente.setText('')
        self.txtApelidosCliente.setText('')
        self.txtTelefono.setText('')
        self.txtDireccion.setText('')
        self.txtCidade.setText('')
        self.txtProvinciaEstado.setText('')
        self.txtCodigoPostal.setText('')
        self.txtPais.setText('')
        self.txtAxenteComercial.setText('')


if __name__=="__main__":

    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()

    aplicacion.exec()