from csirke import Csirke
from kacsacsoru_emlos import KacsacsoruEmlos
from kutya import Kutya

tyuk = Csirke("Bözsi", 3, 2, 5, "szabadtartás",30,60)
print(f"{tyuk.nev}, {tyuk.suly}, {tyuk.kor}, {tyuk.tollassag}, {tyuk.el},{tyuk.sebesseg},{tyuk.idotartam} ")
tyuk.kotkodacsol()
tyuk.csip()
tyuk.eszik(2)
tyuk.repules()
print(f"{tyuk.nev}, {tyuk.suly}, {tyuk.kor}, {tyuk.tollassag}, {tyuk.el}")
tyuk.meghal()
print(f"{tyuk.nev}, {tyuk.suly}, {tyuk.kor}, {tyuk.tollassag}, {tyuk.el}")

