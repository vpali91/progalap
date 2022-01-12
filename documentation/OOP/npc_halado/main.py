from npc import NPC

sanyi = NPC("Sanyi", 100, True)
print(f"{sanyi.name}, {sanyi.hp}, {sanyi.friendly}, {sanyi.ebony.name}, {sanyi.ebony.defense}, fegyó: {sanyi.primary.hp}")
sanyi.injuring(10)
print(f"{sanyi.name}, {sanyi.hp}, {sanyi.friendly}, {sanyi.ebony.name}, {sanyi.ebony.defense}, fegyó: {sanyi.primary.hp}")
sanyi.attack(1)
print(f"{sanyi.name}, {sanyi.hp}, {sanyi.friendly}, {sanyi.ebony.name}, {sanyi.ebony.defense}, fegyó: {sanyi.primary.hp}")

sanyi.injuring(10)
print(f"{sanyi.name}, {sanyi.hp}, {sanyi.friendly}, {sanyi.ebony.name}, {sanyi.ebony.defense}, fegyó: {sanyi.primary.hp}")
sanyi.injuring(10)
print(f"{sanyi.name}, {sanyi.hp}, {sanyi.friendly}, {sanyi.ebony.name}, {sanyi.ebony.defense}, fegyó: {sanyi.primary.hp}")
