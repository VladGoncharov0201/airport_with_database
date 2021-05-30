from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QWidget, QGridLayout
import MainPage
import PageThisTable
import AddInformationPage
import RemoveInformationPage
import UpdateInformationPage
import ClientsPage
import PilotsPage
import StewardessPage
import AddPilotPage
import AddStewardessPage
import AddClientPage
import AddAirplanePage
from db import connection


class addairplanepage(QtWidgets.QMainWindow, AddAirplanePage.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.new_window = None
        self.setupUi(self)

        self.showtable()

        self.back.clicked.connect(self.gotomainwindow)

    def showtable(self):
        try:
            connect = connection()
            cursor = connect.cursor()

            select = "select * from airport.airplanes"
            cursor.execute(select)

            records = cursor.fetchall()
            rows = len(records)

            self.tableWidget.setColumnCount(3)
            self.tableWidget.setRowCount(rows)

            col = 0
            for i in records:
                for a in i:
                    self.tableWidget.setItem(0, col, QTableWidgetItem(str(a)))
                    col += 1

            cursor.close()
            connect.close()
        except:
            print("Произашла ошибка, попробуйет позже")

    def gotomainwindow(self):
        self.new_window = addInformation()
        self.new_window.show()
        self.close()


class addclientpage(QtWidgets.QMainWindow, AddClientPage.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.new_window = None
        self.setupUi(self)

        self.showtable()

        self.back.clicked.connect(self.gotomainwindow)

    def showtable(self):
        try:
            connect = connection()
            cursor = connect.cursor()

            select = "select * from airport.passengers"
            cursor.execute(select)

            records = cursor.fetchall()
            rows = len(records)

            self.tableWidget.setColumnCount(4)
            self.tableWidget.setRowCount(rows)

            col = 0
            for i in records:
                for a in i:
                    self.tableWidget.setItem(0, col, QTableWidgetItem(str(a)))
                    col += 1

            cursor.close()
            connect.close()
        except:
            print("Произашла ошибка, попробуйет позже")

    def gotomainwindow(self):
        self.new_window = addInformation()
        self.new_window.show()
        self.close()


class addstewardesspage(QtWidgets.QMainWindow, AddStewardessPage.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.new_window = None
        self.setupUi(self)

        self.showtable()

        self.back.clicked.connect(self.gotomainwindow)

    def showtable(self):
        try:
            connect = connection()
            cursor = connect.cursor()

            select = "select * from airport.stewardesses"
            cursor.execute(select)

            records = cursor.fetchall()
            rows = len(records)

            self.tableWidget.setColumnCount(5)
            self.tableWidget.setRowCount(rows)

            col = 0
            for i in records:
                for a in i:
                    self.tableWidget.setItem(0, col, QTableWidgetItem(str(a)))
                    col += 1

            cursor.close()
            connect.close()
        except:
            print("Произашла ошибка, попробуйет позже")

    def gotomainwindow(self):
        self.new_window = addInformation()
        self.new_window.show()
        self.close()


class addpilotpage(QtWidgets.QMainWindow, AddPilotPage.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.new_window = None
        self.setupUi(self)

        self.showtable()

        self.ok.clicked.connect(self.add)
        self.back.clicked.connect(self.gotomainwindow)

    def showtable(self):
        try:
            connect = connection()
            cursor = connect.cursor()

            select = "select * from airport.pilots"
            cursor.execute(select)

            records = cursor.fetchall()
            rows = len(records)

            self.tableWidget.setColumnCount(6)
            self.tableWidget.setRowCount(rows)

            col = 0
            for i in records:
                for a in i:
                    self.tableWidget.setItem(0, col, QTableWidgetItem(str(a)))
                    col += 1

            cursor.close()
            connect.close()
        except:
            print("Произашла ошибка, попробуйет позже")

    def add(self):
        pilot_id = self.lineEdit.text()
        surname = self.lineEdit_2.text()
        name = self.lineEdit_3.text()
        education = self.lineEdit_4.text()
        experience = self.lineEdit_5.text()
        phone = self.lineEdit_6.text()

        connect = connection()
        cursor = connect.cursor()

        insert = "insert into airport.pilots" \
                 " (pilot_id, surname, name, education, experience, phone_number) VALUES (%s, %s, %s, %s, %s, %s)"
        value = (pilot_id, surname, name, education, experience, phone)

        cursor.execute(insert, value)

        connect.commit()

        cursor.close()
        connect.close()

        self.showtable()

    def gotomainwindow(self):
        self.new_window = addInformation()
        self.new_window.show()
        self.close()


class stewardesspage(QtWidgets.QMainWindow, StewardessPage.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.new_window = None
        self.setupUi(self)

        self.workthisdb()

        self.back.clicked.connect(self.gotomainwindow)

    def workthisdb(self):
        try:
            connect = connection()
            cursor = connect.cursor()

            select = "select stewardesses.stewardess_id, stewardesses.surname, stewardesses.name," \
                     " stewardesses.experience, flights.flight_id, flights.departure, flights.arrival," \
                     " flights.flight_time, flights.number_of_transfers, flights.state " \
                     "from airport.stewardesses inner join airport.flight_information" \
                     " on airport.stewardesses.stewardess_id = airport.flight_information.stewardess_id" \
                     " inner join airport.flights on airport.flights.flight_id = airport.flight_information.flight_id"
            cursor.execute(select)

            records = cursor.fetchall()
            rows = len(records)

            self.tableWidget.setColumnCount(10)
            self.tableWidget.setRowCount(rows)

            col = 0
            for i in records:
                for a in i:
                    self.tableWidget.setItem(0, col, QTableWidgetItem(str(a)))
                    col += 1

            self.tableWidget.resizeColumnsToContents()

            cursor.close()
            connect.close()
        except:
            print("Произашла ошибка, попробуйет позже")

    def gotomainwindow(self):
        self.new_window = viewTable()
        self.new_window.show()
        self.close()


class pilotspage(QtWidgets.QMainWindow, PilotsPage.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.new_window = None
        self.setupUi(self)

        self.workthisdb()

        self.back.clicked.connect(self.gotomainwindow)

    def workthisdb(self):
        try:
            connect = connection()
            cursor = connect.cursor()

            select = "select pilots.pilot_id, pilots.surname, pilots.name, pilots.education, pilots.experience," \
                     " flights.flight_id, flights.departure, flights.arrival, flights.flight_time," \
                     " flights.number_of_transfers from airport.pilots inner join airport.flight_information" \
                     " on airport.pilots.pilot_id = airport.flight_information.pilot_id" \
                     " inner join airport.flights on airport.flights.flight_id = airport.flight_information.flight_id"
            cursor.execute(select)

            records = cursor.fetchall()
            rows = len(records)

            self.tableWidget.setColumnCount(10)
            self.tableWidget.setRowCount(rows)

            col = 0
            for i in records:
                for a in i:
                    self.tableWidget.setItem(0, col, QTableWidgetItem(str(a)))
                    col += 1

            self.tableWidget.resizeColumnsToContents()

            cursor.close()
            connect.close()
        except:
            print("Произашла ошибка, попробуйет позже")

    def gotomainwindow(self):
        self.new_window = viewTable()
        self.new_window.show()
        self.close()


class clientpage(QtWidgets.QMainWindow, ClientsPage.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.new_window = None
        self.setupUi(self)

        self.workthisdb()

        self.back.clicked.connect(self.gotomainwindow)

    def workthisdb(self):
        try:
            connect = connection()
            cursor = connect.cursor()

            select = "select passengers.passenger_id, passengers.surname, passengers.name," \
                     " passengers.passport_data,flights.flight_id, flights.departure, flights.arrival," \
                     " flights.flight_time, flights.number_of_transfers, flights.state from airport.passengers " \
                     "inner join airport.tickets on airport.passengers.passenger_id = airport.tickets.passenger_id " \
                     "inner join airport.flights on airport.flights.flight_id = airport.tickets.flight_id"
            cursor.execute(select)

            records = cursor.fetchall()
            rows = len(records)

            self.tableWidget.setColumnCount(10)
            self.tableWidget.setRowCount(rows)

            col = 0
            for i in records:
                for a in i:
                    self.tableWidget.setItem(0, col, QTableWidgetItem(str(a)))
                    col += 1

            self.tableWidget.resizeColumnsToContents()

            cursor.close()
            connect.close()
        except:
            print("Произашла ошибка, попробуйет позже")

    def gotomainwindow(self):
        self.new_window = viewTable()
        self.new_window.show()
        self.close()


class viewTable(QtWidgets.QMainWindow, PageThisTable.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.new_window = None
        self.setupUi(self)

        self.back.clicked.connect(self.gotomainwindow)
        self.info_about_client.clicked.connect(self.open_info_about_client)
        self.inf_about_pilot.clicked.connect(self.open_info_about_pilot)
        self.inf_about_stewardess.clicked.connect(self.open_info_about_stewardess)

    def open_info_about_client(self):
        self.new_window = clientpage()
        self.new_window.show()
        self.close()

    def open_info_about_pilot(self):
        self.new_window = pilotspage()
        self.new_window.show()
        self.close()

    def open_info_about_stewardess(self):
        self.new_window = stewardesspage()
        self.new_window.show()
        self.close()

    def gotomainwindow(self):
        self.new_window = mainPage()
        self.new_window.show()
        self.close()


class addInformation(QtWidgets.QMainWindow, AddInformationPage.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.new_window = None
        self.setupUi(self)

        self.back.clicked.connect(self.gotomainwindow)
        self.add_pilot.clicked.connect(self.addpilot)
        self.add_stewardess.clicked.connect(self.addstewardess)
        self.add_client.clicked.connect(self.addclient)
        self.add_airplane.clicked.connect(self.addairplane)

    def gotomainwindow(self):
        self.new_window = mainPage()
        self.new_window.show()
        self.close()

    def addpilot(self):
        self.new_window = addpilotpage()
        self.new_window.show()
        self.close()

    def addstewardess(self):
        self.new_window = addstewardesspage()
        self.new_window.show()
        self.close()

    def addclient(self):
        self.new_window = addclientpage()
        self.new_window.show()
        self.close()

    def addairplane(self):
        self.new_window = addairplanepage()
        self.new_window.show()
        self.close()


class removeInformation(QtWidgets.QMainWindow, RemoveInformationPage.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.new_window = None
        self.setupUi(self)

        self.back.clicked.connect(self.gotomainwindow)

    def gotomainwindow(self):
        self.new_window = mainPage()
        self.new_window.show()
        self.close()


class updateInformation(QtWidgets.QMainWindow, UpdateInformationPage.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.new_window = None
        self.setupUi(self)

        self.back.clicked.connect(self.gotomainwindow)

    def gotomainwindow(self):
        self.new_window = mainPage()
        self.new_window.show()
        self.close()


class mainPage(QtWidgets.QMainWindow, MainPage.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.new_window = None
        self.setupUi(self)

        self.exit.clicked.connect(self.closeproject)
        self.viewTable.clicked.connect(self.viewalltable)
        self.addInformayionInTable.clicked.connect(self.addinfo)
        self.removeInformationInTable.clicked.connect(self.removeinfo)
        self.updateInformationInTable.clicked.connect(self.updateinfo)

    def closeproject(self):
        self.close()

    def viewalltable(self):
        self.new_window = viewTable()
        self.new_window.show()
        self.close()

    def addinfo(self):
        self.new_window = addInformation()
        self.new_window.show()
        self.close()

    def removeinfo(self):
        self.new_window = removeInformation()
        self.new_window.show()
        self.close()

    def updateinfo(self):
        self.new_window = updateInformation()
        self.new_window.show()
        self.close()

    def workthisdb(self):
        try:
            connect = connection()
            cursor = connect.cursor()

            select = "select * from airport.pilots"
            cursor.execute(select)

            records = cursor.fetchall()

            for i in records:
                print(i)

            cursor.close()
            connect.close()
        except:
            print("Произашла ошибка, попробуйет позже")


app = QtWidgets.QApplication([])
window = mainPage()
window.show()
app.exec_()
