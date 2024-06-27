#!/usr/bin/python3
from models.petition import Petition
from models.complainant import Complainant
from models.suspect import Suspect
from models import storage

#Create Petition
petition = Petition(casefile_no='sdfsdgdssd')
petition2 = Petition(casefile_no='dafdgeedges')
petition.save()
petition2.save()

#Create Complainant
complainant = Complainant(name="Adeshina")
complainant2 = Complainant(name="Ibrahim")
complainant3 = Complainant(name="Olaiya")
complainant.save()
complainant2.save()
complainant3.save()

#Create Suspect
suspect = Suspect(name="Omo")
suspect2 = Suspect(name="Yibo")
suspect3 = Suspect(name="Aba")
suspect.save()
suspect2.save()
suspect3.save()


# Link them together
petition.complainants.extend([complainant, complainant3])
petition2.complainants.append(complainant2)
# this must fail
petition2.complainants.append(suspect)

for c in petition2.complainants:
    print(c.name)

suspect.petitions.extend([petition, petition2])
suspect2.petitions.append(petition)
suspect3.petitions.append(petition2)

complainant.suspects.extend([suspect, suspect2])
complainant2.suspects.append(suspect3)
complainant3.suspects.append(suspect)

storage.save()

print("OK")
