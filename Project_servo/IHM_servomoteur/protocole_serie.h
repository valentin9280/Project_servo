#ifndef PROTOCOLE_SERIE_H
#define PROTOCOLE_SERIE_H

#include <QByteArray>

class protocole_serie
{
public:




    void LaserON(void);
    void LaserOFF(void);
    void MoveMoteur(int SensMoteur1 , int SensMoteur2);
    void Forme(int figure);
    void InitMoteur();
     protocole_serie();
  private:


    enum Commande{Move,Laser,Forme};
    enum Figure{ carre , cercle , triangle};
    enum Laser{OFF,ON};
    enum deplacement{Gauche , Droite,init,NoMove};


    QByteArray trametoSend;


};

#endif // PROTOCOLE_SERIE_H
