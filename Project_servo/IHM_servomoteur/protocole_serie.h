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
     protocole_serie();
     QByteArray trametoSend;

    enum Commande{Move =49,Laser,Forme,init};
    enum Figure{ carre =49, cercle , triangle};
    enum Laser{OFF=49,ON};
    enum deplacement{NoMove = 49,Gauche , Droite};





};

#endif // PROTOCOLE_SERIE_H
