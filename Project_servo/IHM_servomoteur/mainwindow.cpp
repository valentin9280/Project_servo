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
       connect(SerialPort, SIGNAL(bytesWritten(qint64)), this,SLOT(DataWritten(qint64)));

    }
    else
    {
        SerialPort->close();
       ui->Log->append("Impossible de se connecter à : " + PortName);
    }

}

void MainWindow::DataWritten(qint64)
{
    ui->Log->append("Trame envoyée : " + Protocole->GetTrame());
}

void MainWindow::on_SerialButton_clicked()
{
   WindowSerial->show();
}

void MainWindow::on_CarreButton_clicked()
{
     Protocole -> Dessiner(31);
}

void MainWindow::on_TriangleButton_clicked()
{
 Protocole -> Dessiner(33);
}

void MainWindow::on_RondButton_clicked()
{
  Protocole -> Dessiner(32);
}

void MainWindow::on_ButtonHaut_clicked()
{
 Protocole-> MoveMoteur(1,0);
}

void MainWindow::on_ButtonGauche_clicked()
{
 Protocole-> MoveMoteur(0,-1);
}

void MainWindow::on_ButtonBas_clicked()
{
  Protocole-> MoveMoteur(-1,0);
}

void MainWindow::on_ButtonDroit_clicked()
{
   Protocole->MoveMoteur(0,1);
}


void MainWindow::on_ButtonLaserON_clicked()
{
    Protocole->LaserON();
    //SerialPort->write(Protocole->GetTrame());
}

void MainWindow::on_ButtonLaserOFF_clicked()
{
    Protocole->LaserOFF();
    //SerialPort->write(Protocole->GetTrame());
}

void MainWindow::on_ButtonINIT_clicked()
{
    Protocole->InitMoteur();
}
