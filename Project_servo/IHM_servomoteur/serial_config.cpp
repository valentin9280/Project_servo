#include "serial_config.h"
#include "ui_serial_config.h"

serial_config::serial_config(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::serial_config)
{
    ui->setupUi(this);
    QList<QSerialPortInfo> list;
    list = QSerialPortInfo::availablePorts();

    for(int i = 0; i < list.size(); i++)
        ui->comboBoxCONN->addItem(list.at(i).portName());
}

serial_config::~serial_config()
{
    delete ui;
}


void serial_config::on_ButtonOk_clicked()
{
    emit ConfigurationSerialConnection(ui->comboBoxCONN->currentText());
    close();
}


void serial_config::on_ButtonAnnuler_clicked()
{
    close();
}


void serial_config::on_ButtonRefresh_clicked()
{

    ui->comboBoxCONN->clear();
    QList<QSerialPortInfo> list;
    list = QSerialPortInfo::availablePorts();

    for(int i = 0; i < list.size(); i++)
       ui->comboBoxCONN->addItem(list.at(i).portName());
}
