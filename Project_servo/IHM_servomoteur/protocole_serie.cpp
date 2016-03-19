#include "protocole_serie.h"

protocole_serie::protocole_serie()
{

}

void protocole_serie::LaserON()
{
    trametoSend.clear();
    trametoSend.append(Laser);
    trametoSend.append(ON);
    trametoSend.append('\0');
}

void protocole_serie::LaserOFF()
{
    trametoSend.clear();
    trametoSend.append(Laser);
    trametoSend.append(OFF);
    trametoSend.append('\0');

}
void protocole_serie::Forme(int figure)
{
    trametoSend.clear();
    trametoSend.append(Forme);
    trametoSend.append(figure);
    trametoSend.append('\0'');
}

void protocole_serie::InitMoteur(void)
{
    trametoSend.clear();
    trametoSend.append(Move);
    trametoSend.append(init);
    trametoSend.append('\0');
}

void protocole_serie::MoveMoteur(int SensMoteur1, int SensMoteur2)
{
    trame.clear();
    trame.append(Move);
    switch(SensMoteur1)
    {
        case -1:trame.append(Gauche);break;
        case 0:trame.append(NoMove);break;
        case 1:trame.append(Droite);break;
    }
    switch(SensMoteur2)
    {
        case -1:trame.append(Gauche);break;
        case 0:trame.append(NoMove);break;
        case 1:trame.append(Droite);break;
    }
    trame.append('\0');
}
