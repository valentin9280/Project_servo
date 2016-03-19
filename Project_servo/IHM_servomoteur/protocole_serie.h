#ifndef PROTOCOLE_SERIE_H
#define PROTOCOLE_SERIE_H

#include <QByteArray>

class protocole_serie
{
public:

    void LaserON(void);
    void LaserOFF(void);
    void MoveMoteur(int SensMoteur1 , int SensMoteur2);
    void Dessiner(int figure);
    void InitMoteur();
    QByteArray GetTrame(void);
     protocole_serie();
  private:


    enum Commande{Move =31,Laser,Forme,init};
    enum Figure{ carre =31, cercle , triangle};
    enum Laser{OFF=31,ON};
    enum deplacement{NoMove = 31,Gauche , Droite};


    QByteArray trametoSend;


};

#endif // PROTOCOLE_SERIE_H
