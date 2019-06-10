# =======================================================================================
# COMPLEXE
# =======================================================================================
""" Implementation de la classe Complexe et des fonctions opératoires entre complexes """
""" Code en Python 3.3 """
__author__  = "GILLIARD Tallulah / LABARCHEDE Melody"
__version__ = "1.0"
__date__    = "2015-11-19"
# =======================================================================================
from math import * 
import sys
    
class Complexe:

    def __init__(self, a, b, type=True):
        if type :
            #cartesien
            self.__dict__['reel'] = a
            self.__dict__['imag'] = b
        else:
            #polaire
            self.__dict__['module'] = a
            self.__dict__['argument'] = b


    def __abs__(self):
        if self.isCartesien:
            return sqrt(self.__dict__['reel']**2 + self.__dict__['imag']**2)
        else:
            return __abs__(self.polaireACartesien)

    def __add__(self, other):
        if self.isCartesien:
            if other.isCartesien:
                return Complexe( self.__dict__['reel'] + other.__dict__['reel'], \
                                 self.__dict__['imag'] + other.__dict__['imag'], \
                                 True )
            else :
                return self.__add__(other.polaireACartesien)  
        else:
            if other.isPolaire:
                return Complexe (sqrt(self.__dict__['module']**2 + other.__dict__['module']**2 + 2*self.__dict__['module']*other.__dict__['module']*cos(self.__dict__['argument']-other.__dict__['argument'])),
                                 atan( ( self.__dict__['module']*sin(self.__dict__['argument']) + other.__dict__['module']*sin(other.__dict__['argument']) / self.__dict__['module']*cos(self.__dict__['argument']) + other.__dict__['module']*cos(other.__dict__['argument']) ) ), \
                                 False)
            else:
                return self.__add__(other.cartesienAPolaire) 
                

    def __mul__(self, other):
        if self.isCartesien:
            if other.isCartesien:
                return Complexe( self.__dict__['reel']*other.__dict__['reel'] - self.__dict__['imag']*other.__dict__['imag'], \
                                 self.__dict__['reel']*other.__dict__['imag'] + self.__dict__['imag']*other.__dict__['reel'], \
                                 True )

            else:
                return self.__mul__(other.polaireACartesien)                 
        else:
            if other.isPolaire:
                return Complexe ( self.__dict__['module']*other.__dict__['module'], \
                                  self.__dict__['argument']+other.__dict__['argument'], \
                                  False)
            else:
                return self.__mul__(other.cartesienAPolaire)
            
    def __sub__(self, other):
        if self.isCartesien:
            if other.isCartesien:
                return self.__add__(other.oppose)
            else:
                return self.__add__(other.polaireACartesien.oppose)
        else:
            if other.isCartesien:           
                return self.polaireACartesien.__mul__(other) 
            else:
                return self.polaireACartesien.__mul__(other.polaireACartesien) 
                               
    def __truediv__(self, other): # truediv (division floatante) en Python 3 . div en Python 2 qui n'existe plus en Python3 (et non floordiv, division entiere en python 3)
        if self.isCartesien:
            if other.isCartesien:
                return self.__mul__(other.inverse)
            else :
                return self.__mul__(other.polaireACartesien.inverse) 
        else:
            if other.isCartesien:
                return self.polaireACartesien.__mul__(other.inverse)
            else :
                return self.polaireACartesien.__mul__(other.polaireACartesien.inverse) 

    def __pow__(self, other):
        if self.isCartesien:
            if other.isCartesien:
                n = other.__dict__['reel']
                r = pow(self.__abs__(), n)
                phi = n*(((pi/2.0) - atan2(self.__dict__['reel'], self.__dict__['imag'])) % (pi*2.0))
                return Complexe(cos(phi)*r, sin(phi)*r)
            else:
                n = other.polaireACartesien.__dict__['reel']
                r = pow(self.__abs__(), n)
                phi = n*(((pi/2.0) - atan2(self.__dict__['reel'], self.__dict__['imag'])) % (pi*2.0))
                return Complexe(cos(phi)*r, sin(phi)*r)
        else:
            if other.isCartesien:
                n = other.__dict__['reel']
                r = pow(self.polaireACartesien.__abs__(), n)
                phi = n*(((pi/2.0) - atan2(self.polaireACartesien.__dict__['reel'], self.polaireACartesien.__dict__['imag'])) % (pi*2.0))
                return Complexe(cos(phi)*r, sin(phi)*r)
            else:
                n = other.polaireACartesien.__dict__['reel']
                r = pow(self.polaireACartesien.__abs__(), n)
                phi = n*(((pi/2.0) - atan2(self.polaireACartesien.__dict__['reel'], self.polaireACartesien.__dict__['imag'])) % (pi*2.0))
                return Complexe(cos(phi)*r, sin(phi)*r)
                .840
        
    def __lt__(self, other): 
        if self.isCartesien:
            if other.isCartesien:
                if self.__dict__['reel'] < other.__dict__['reel'] \
                or ( self.__dict__['reel'] == other.__dict__['reel'] and self.__dict__['imag'] < other.__dict__['imag']):
                    return True
                else:
                    return False
            else:
                if self.__dict__['reel'] < other.polaireACartesien.__dict__['reel'] \
                or ( self.__dict__['reel'] == other.polaireACartesien.__dict__['reel'] and self.__dict__['imag'] < other.polaireACartesien.__dict__['imag']):
                    return True
                else:
                    return False
        else:
            if other.isCartesien:
                if self.polaireACartesien.__dict__['reel'] < other.__dict__['reel'] \
                or ( self.polaireACartesien.__dict__['reel'] == other.__dict__['reel'] and self.polaireACartesien.__dict__['imag'] < other.__dict__['imag']):
                    return True
                else:
                    return False
            else:
                if self.polaireACartesien.__dict__['reel'] < other.polaireACartesien.__dict__['reel'] \
                or ( self.polaireACartesien.__dict__['reel'] == other.polaireACartesien.__dict__['reel'] and self.polaireACartesien.__dict__['imag'] < other.polaireACartesien.__dict__['imag']):
                    return True
                else:
                    return False

    def __eq__(self, other): 
        if self.isCartesien:
            if other.isCartesien:
                return (self.__dict__['reel'], self.__dict__['imag']) == (other.__dict__['reel'], other.__dict__['imag'])
            else:
                return (self.__dict__['reel'], self.__dict__['imag']) == (other.polaireACartesien.__dict__['reel'], other.polaireACartesien.__dict__['imag'])
        else:
            if other.isPolaire:
                if( self.__dict__['module'] == other.__dict__['module'] \
                        and ( (self.__dict__['argument'] == other.__dict__['argument']) % pi*2.0 )):
                    return True
                else:
                    return False
            else:
                if ( self.__dict__['module'] == other.cartesienAPolaire.__dict__['module'] \
                        and ( (self.__dict__['argument'] == other.cartesienAPolaire.__dict__['argument']) % pi*2.0 )):
                    return True
                else:
                    return False

    @property
    def polaireACartesien(self):
        if self.isPolaire:
            return Complexe(cos(self.__dict__['argument'])*self.__dict__['module'], sin(self.__dict__['argument'])*self.__dict__['module'], True)

    @property
    def cartesienAPolaire(self):
        if self.isCartesien:
            return Complexe(self.__abs__(), atan(self.__dict__['imag'] / self.__dict__['reel']), False)

    @property
    def isCartesien(self):
        return hasattr(self, 'reel') and hasattr(self, 'imag')

    @property
    def isPolaire(self):
        return hasattr(self, 'module') and hasattr(self, 'argument')

    @property
    def cartesien(self):
        if self.isCartesien:
            return (self.__dict__['reel'],self.__dict__['imag'])
        else:
            return "n'est pas un cartesien"
        
    @property
    def polaire(self):
        if self.isPolaire:
            return (self.__dict__['module'],self.__dict__['argument'])
        else:
            return "n'est pas un polaire"

    @property
    def oppose(self):
        if self.isCartesien:
            return (Complexe(-self.__dict__['reel'], -self.__dict__['imag'], True))
        else:
            return self.polaireACartesien.oppose

    @property
    def inverse(self):
        if self.isCartesien :
            if self.__dict__['reel']!=0 and self.__dict__['imag']!=0:
                return (Complexe((self.__dict__['reel'])/(self.__dict__['reel']**2+self.__dict__['imag']**2), (-self.__dict__['imag'])/(self.__dict__['reel']**2+self.__dict__['imag']**2), True))
            else:
                return None 
        else:
            if self.__dict__['module']!=0 and self.__dict__['argument']!=0:
                return (Complexe(1/self.__dict__['module'], -self.__dict__['argument'], False))
            else:
                return None 

    @property
    def conjugue(self):
        if self.isCartesien:
            return (Complexe(self.__dict__['reel'], -self.__dict__['imag'], True))
        else:
            return self.polaireACartesien.conjugue

# =======================================================================================
#       TESTS
# =======================================================================================

def test():
    print ("---TESTS---\n")

    #---DEFINITION DES COMPLEXES---
    c1 = Complexe(10, 20, True)
    c2 = Complexe(20, 10, True)
    c_neutre_add = Complexe(0,0, True)
    c_neutre_mul = Complexe(1,0,True)

    p1 = Complexe(30, 40, False)
    p2 = Complexe(40, 30, False)

    #------------------------------
    print("---AFFICHAGE DES COMPLEXES ET VERIFICATIONS---\n")
    print ("c1=",c1)
    print ("c1 isCartesien ?",c1.isCartesien)
    print ("c1 isPolaire ?",c1.isPolaire)
    print(" ")
    print ("p1=",p1)
    print ("p1 isCartesien ?",p1.isCartesien)
    print ("p1 isPolaire ?",p1.isPolaire)
    print(" ")

    print("cartesien(c1)=",c1.cartesien)
    print("cartesien(c2)=",c2.cartesien)
    print(" ")
    print("cartesien(c_neutre_add)=",c_neutre_add.cartesien)
    print("cartesien(c_neutre_mul)=",c_neutre_mul.cartesien)
    print(" ")
    print("polaire(c1)=",c1.polaire)
    print("polaire(c2)=",c2.polaire)
    print("polaire(cartesienAPolaire(c1))=",c1.cartesienAPolaire.polaire)
    print("polaire(cartesienAPolaire(c2))=",c2.cartesienAPolaire.polaire)
    print(" ")
    print("cartesien(p1)=",p1.cartesien)
    print("cartesien(p2)=",p2.cartesien)
    print("cartesien(polaireACartesien(p1))=",p1.polaireACartesien.cartesien)
    print("cartesien(polaireACartesien(p2))=",p2.polaireACartesien.cartesien)
    print("polaire(p1)=",p1.polaire)
    print("polaire(p2)=",p2.polaire)
    print("\n")

    #------------------------------
    print("---OPPOSE---\n")
    print("oppose(c1).cartesien=",c1.oppose.cartesien)
    print("oppose(p1).polaire=",p1.oppose.polaire)
    print("oppose(p1).cartesien=",p1.oppose.cartesien)
    print("oppose(polaireACartesien(p1)).cartesien=",p1.polaireACartesien.oppose.cartesien) 
    print("cartesienAPolaire(oppose(p1)).polaire=",p1.oppose.cartesienAPolaire.polaire)
    print("cartesienAPolaire(oppose(polaireACartesien(p1))).polaire=",p1.polaireACartesien.oppose.cartesienAPolaire.polaire) 
    print("\n")

    #------------------------------
    print("---INVERSE---\n")
    print("inverse(c1)=",c1.inverse.cartesien)
    print("polaireACartesien(inverse(cartesienAPolaire(c1)))=",c1.cartesienAPolaire.inverse.polaireACartesien.cartesien)
    print("inverse(p1)=",p1.inverse.polaire)
    print("cartesienAPolaire(inverse(polaireACartesien(p1)))=",p1.polaireACartesien.inverse.cartesienAPolaire.polaire) # pb sur l'imaginaire
    print("\n")

    #------------------------------
    print("---CONJUGUE---\n")
    print("conjugue(c1)=",c1.conjugue.cartesien)
    print("conjugue(p1)=",p1.conjugue.polaire)
    print("conjugue(p1)=",p1.conjugue.cartesien)
    print("conjugue(polaireACartesien(p1)).cartesien=",p1.polaireACartesien.conjugue.cartesien) 
    print("cartesienAPolaire(conjugue(p1)).polaire=",p1.conjugue.cartesienAPolaire.polaire)
    print("cartesienAPolaire(conjugue(polaireACartesien(p1))).polaire=",p1.polaireACartesien.conjugue.cartesienAPolaire.polaire) 
    print("\n")

    #------------------------------
    print("---ADDITION (ADD)---\n")
    print("add(c1+c2)=",(c1+c2).cartesien)
    print("add(p1+p2)=",(p1+p2).polaire)
    print(" ")
    print("add(c1+c_neutre_add)=",(c1+c_neutre_add).cartesien)
    print(" ")
    print("add(c1+p1)=",(c1+p1).cartesien)
    print("add(c1+polaireACartesien(p1))=",(c1+p1.polaireACartesien).cartesien)
    print(" ")
    print("add(p1+c1)=",(p1+c1).polaire)    
    print("add(p1+cartesienAPolaire(c1))=",(p1+c1.cartesienAPolaire).polaire)
    print("\n")

    #------------------------------
    print("---MULTIPLICATION (MUL)---\n")
    print("mul(c1*c2)=",(c1*c2).cartesien)
    print("mul(p1*p2)=",(p1*p2).polaire)
    print(" ")
    print("mul(c1*c_neutre_mul)=",(c1*c_neutre_mul).cartesien) 
    print(" ")
    print("mul(c1+p1)=",(c1*p1).cartesien)
    print("mul(c1+polaireACartesien(p1))=",(c1*p1.polaireACartesien).cartesien)
    print(" ")
    print("mul(p1+c1)=",(p1*c1).polaire)    
    print("mul(p1+cartesienAPolaire(c1))=",(p1*c1.cartesienAPolaire).polaire)
    print("\n")

    #------------------------------
    print("---SOUSTRACTION (SUB)---\n")
    print("sub(c1-c2)=",(c1-c2).cartesien)
    print("sub(p1-p2)=",(p1-p2).polaire)
    print("sub(p1-p2).cartesien=",(p1-p2).cartesien)
    print(" ")
    print("sub(c1*c_neutre_add)=",(c1-c_neutre_add).cartesien) 
    print(" ")
    print("sub(c1-p1)=",(c1-p1).cartesien)
    print("sub(c1-polaireACartesien(p1))=",(c1-p1.polaireACartesien).cartesien)
    print(" ")
    print("sub(p1-c1)=",(p1-c1).polaire)    
    print("sub(p1-cartesienAPolaire(c1))=",(p1-c1.cartesienAPolaire).polaire)
    print("sub(p1-c1).cartesien=",(p1-c1).cartesien)    
    print("sub(p1-cartesienAPolaire(c1)).cartesien=",(p1-c1.cartesienAPolaire).cartesien)
    print("\n")
    
    #------------------------------
    print("---DIVISION (TRUEDIV)---\n")
    print("div(c1/c2)=",(c1 / c2).cartesien)
    print("div(p1/p2)=",(p1 / p2).polaire)
    print("div(p1/p2).cartesien=",(p1/p2).cartesien)
    print(" ")
    print("div(c1/p1)=",(c1/p1).cartesien)
    print("div(c1/polaireACartesien(p1))=",(c1/p1.polaireACartesien).cartesien)
    print(" ")
    print("div(p1/c1)=",(p1/c1).polaire)    
    print("div(p1/cartesienAPolaire(c1))=",(p1/c1.cartesienAPolaire).polaire)
    print("div(p1/c1).cartesien=",(p1/c1).cartesien)    
    print("div(p1/cartesienAPolaire(c1)).cartesien=",(p1/c1.cartesienAPolaire).cartesien)
    print("\n")

    #------------------------------
    print("---PUISSANCE COMPLEXE (POW)---\n")
    print("pow(c1,c2)=",(c1**c2).cartesien)
    print("pow(p1,p2)=",(p1**p2).cartesien)
    print("pow(c1,p1)=",(c1**p1).cartesien)
    print("pow(p1,c1)=",(p1**c1).cartesien)
    print("\n")
    
    #------------------------------
    print("---INFERIEUR (LT)---\n")
    print("lt(c1<c2)=",c1<c2)
    print("lt(c1<c_neutre_mul)=",c1<c_neutre_mul)
    print("lt(c_neutre_mul<c2)=",c_neutre_mul<c2)    
    print("lt(c_neutre_add<c_neutre_mul)=",c_neutre_add<c_neutre_mul)    
    print(" ")
    print("lt(p1<p2)=",p1<p2)
    print("lt(c1<p1)=",c1<p1)
    print("lt(p1<c1)=",p1<c1)
    print("\n")
    
    #------------------------------
    print("---EGAL (EQU)---\n")
    print("equ(c1==c1)=",c1==c1)
    print("equ(c1==c2)=",c1==c2)
    print("equ(p1==p1)=",p1==p1)    
    print("equ(p1==p2)=",p1==p2)
    print("equ(c1==p1)=",c1==p1)  
    print("\n")
          
    #------------------------------
    print("---LISTE---\n")
    liste = [c1, c2, c_neutre_add, c_neutre_mul]
    print("liste :")
    for i in liste:
        print(i.cartesien)
    print(" ")
    liste_classee = sorted(liste)
    print("liste classee :")
    for i in liste_classee:
        print(i.cartesien)
    print(" ")
    
    print("c2=",c2.cartesien)
    print("c2 dans liste ?",c2 in liste)
    c3 = Complexe(3,3,True)
    print("c3=",c3.cartesien)
    print("c3 dans liste ?",c3 in liste)
    print(" ")

    #------------------------------
    print("---FIN DE TESTS---")

# =======================================================================================
        
if __name__=="__main__":
    test()
    
