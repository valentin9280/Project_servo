#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "serial_config.h"
#include "protocole_serie.h"
#include <QtSerialPort/QSerialPort>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:
    void on_SerialButton_clicked();

    void on_CarreButton_clicked();

    void on_TriangleButton_clicked();

    void on_RondButton_clicked();

    void on_ButtonHaut_clicked();

    void on_ButtonGauche_clicked();

    void on_ButtonBas_clicked();

    void on_ButtonDroit_clicked();

    void on_ButtonLaser_clicked();

    void SerialConnect(QString PortName);

    void DataWritten(qint64);

private:
    Ui::MainWindow *ui;
    serial_config *WindowSerial;
    QSerialPort *SerialPort;
    protocole_serie *Protocole;

};

#endif // MAINWINDOW_H
