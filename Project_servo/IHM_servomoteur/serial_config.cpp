#include "serial_config.h"
#include "ui_serial_config.h"

serial_config::serial_config(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::serial_config)
{
    ui->setupUi(this);
    QList<QSerialPortInfo> liste;
    liste = QSerialPortInfo::availablePorts();

    for(int i = 0; i < liste.size(); i++)
        ui->comboBoxCONN->addItem(liste.at(i).portName());
}

serial_config::~serial_config()
{
    delete ui;
}


void serial_config::on_ButtonOk_clicked()
{
    emit ConfigurationSerialConnection(ui->comboBoxCONN->currentText());
}


void serial_config::on_ButtonAnnuler_clicked()
{
    delete ui;
}

void serial_config::on_ButtoRefresh_clicked()
{
    ui->comboBoxCONN->clear();
    QList<QSerialPortInfo> liste;
    liste = QSerialPortInfo::availablePorts();

    for(int i = 0; i < liste.size(); i++)
       ui->comboBoxCONN->addItem(liste.at(i).portName());
}

