#ifndef SERIAL_CONFIG_H
#define SERIAL_CONFIG_H

#include <QDialog>
#include <QtSerialPort/QSerialPort>
#include <QtSerialPort/QSerialPortInfo>
#include <QList>

namespace Ui {
class serial_config;
}

class serial_config : public QDialog
{
    Q_OBJECT

public:
    explicit serial_config(QWidget *parent = 0);
    ~serial_config();
signals:
    void ConfigurationSerialConnection(QString config);

private slots:

    void on_ButtonOk_clicked();

    void on_ButtonAnnuler_clicked();

    void on_ButtonRefresh_clicked();

private:
    Ui::serial_config *ui;
};

#endif // SERIAL_CONFIG_H
