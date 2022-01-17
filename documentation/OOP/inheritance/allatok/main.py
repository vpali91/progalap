from csirke import Csirke
from kutya import Kutya

tyuk = Csirke("Bözsi", 3, 2, 5, "szabadtartás")
print(f"{tyuk.nev}, {tyuk.suly}, {tyuk.kor}, {tyuk.tollassag}, {tyuk.el}")
tyuk.kotkodacsol()
tyuk.csip()
tyuk.eszik(2)
print(f"{tyuk.nev}, {tyuk.suly}, {tyuk.kor}, {tyuk.tollassag}, {tyuk.el}")
tyuk.meghal()
print(f"{tyuk.nev}, {tyuk.suly}, {tyuk.kor}, {tyuk.tollassag}, {tyuk.el}")

bundas = Kutya("Bundás", 10, 2, 3, "puli")
print(f"{bundas.nev},{bundas.suly},{bundas.kor},{bundas.szor_hossz},{bundas.fajta},{bundas.el}")
bundas.ugat()
bundas.harap()
bundas.eszik(3)
print(f"{bundas.nev},{bundas.suly},{bundas.kor},{bundas.szor_hossz},{bundas.fajta},{bundas.el}")
bundas.meghal()
print(f"{bundas.nev},{bundas.suly},{bundas.kor},{bundas.szor_hossz},{bundas.fajta},{bundas.el}")
