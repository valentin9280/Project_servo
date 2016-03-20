#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
   WindowSerial = new serial_config(this);
   Protocole = new protocole_serie;
    QObject::connect(WindowSerial, SIGNAL(ConfigurationSerialConnection(QString)), this, SLOT(SerialConnect(QString)));
}

MainWindow::~MainWindow()
{
    delete ui;
    delete WindowSerial;
    delete Protocole;
}

void MainWindow::SerialConnect(QString PortName)
{
    SerialPort = new QSerialPort(this);
    SerialPort->setPortName(PortName);
    if (SerialPort->open(QIODevice::ReadWrite))
    {
        SerialPort->setBaudRate(QSerialPort::Baud115200);
        SerialPort->setDataBits(QSerialPort::Data8);
        SerialPort->setParity(QSerialPort::NoParity);
        SerialPort->setStopBits(QSerialPort::OneStop);
        SerialPort->setFlowControl(QSerialPort::NoFlowControl);
        ui->Log->append("Connecté à : " + PortName + " 115200Bds, 8 Data, NoParity, 1 Stop ");
        ui->groupBoxForme->setEnabled(true);
        ui->groupBoxCommande->setEnabled(true);
       //connect(SerialPort, SIGNAL(bytesWritten(qint64)), this,SLOT(DataWritten(qint64)));

    }
    else
    {
        SerialPort->close();
       ui->Log->append("Impossible de se connecter à : " + PortName);
    }

}

void MainWindow::on_SerialButton_clicked()
{
   WindowSerial->show();
   SerialPort->write(Protocole->trametoSend);
}

void MainWindow::on_CarreButton_clicked()
{
     Protocole -> Dessiner(49);
     SerialPort->write(Protocole->trametoSend);
}

void MainWindow::on_TriangleButton_clicked()
{
 Protocole -> Dessiner(51);
 SerialPort->write(Protocole->trametoSend);
}

void MainWindow::on_RondButton_clicked()
{
  Protocole -> Dessiner(50);
  SerialPort->write(Protocole->trametoSend);
}

void MainWindow::on_ButtonHaut_clicked()
{
 Protocole-> MoveMoteur(1,0);
 SerialPort->write(Protocole->trametoSend);
}

void MainWindow::on_ButtonGauche_clicked()
{
 Protocole-> MoveMoteur(0,-1);
 SerialPort->write(Protocole->trametoSend);
}

void MainWindow::on_ButtonBas_clicked()
{
  Protocole-> MoveMoteur(-1,0);
  SerialPort->write(Protocole->trametoSend);
}

void MainWindow::on_ButtonDroit_clicked()
{
   Protocole->MoveMoteur(0,1);
   SerialPort->write(Protocole->trametoSend);
}


void MainWindow::on_ButtonLaserON_clicked()
{
    Protocole->LaserON();
    SerialPort->write(Protocole->trametoSend);
}

void MainWindow::on_ButtonLaserOFF_clicked()
{
    Protocole->LaserOFF();
    SerialPort->write(Protocole->trametoSend);
}

void MainWindow::on_ButtonINIT_clicked()
{
    Protocole->InitMoteur();
    SerialPort->write(Protocole->trametoSend);
}
