#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
   // SerialWindow = new ConnexionSerie(this);
    //ProtocoleBeagleBone = new Protocole;
    QObject::connect(WindowSerial, SIGNAL(ConfigurationSerialConnection(QString)), this, SLOT(SerialConnect(QString)));
}

MainWindow::~MainWindow()
{
    delete ui;
    delete WindowSerial;
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
       // ui->textEditLog->append("Connecté à : " + PortName + " 9600Bds, 8 Data, NoParity, 1 Stop ");
       // ui->GroupBoxFormes->setEnabled(true);
       // ui->GroupBoxCommandeManuelle->setEnabled(true);
       // connect(SerialPort, SIGNAL(bytesWritten(qint64)), this,SLOT(DataWritten(qint64)));

    }
    else
    {
        SerialPort->close();
       // ui->textEditLog->append("Impossible de se connecter à : " + PortName);
    }

}

void MainWindow::on_SerialButton_clicked()
{
   WindowSerial->show();
}

void MainWindow::on_CarreButton_clicked()
{

}

void MainWindow::on_TriangleButton_clicked()
{

}

void MainWindow::on_RondButton_clicked()
{

}

void MainWindow::on_ButtonHaut_clicked()
{

}

void MainWindow::on_ButtonGauche_clicked()
{

}

void MainWindow::on_ButtonBas_clicked()
{

}

void MainWindow::on_ButtonDroit_clicked()
{

}

void MainWindow::on_ButtonLaser_clicked()
{
    Protocole->LaserON();
    //SerialPort->write(Protocole->GetTrame());
}
