
tall_liste = [3, 7, 2, 8, 5, 10, 12, 1, 6, 9]

def kvadrater_av_partall(liste):

    return [x**2 for x in liste if x % 2 == 0]

def sum_og_gjennomsnitt(liste):

    total = sum(liste)
    gjennomsnitt = total / len(liste)
    return total, gjennomsnitt

def finn_maks_og_min(liste):

    return max(liste), min(liste)


kvadrater = kvadrater_av_partall(tall_liste)
total, gjennomsnitt = sum_og_gjennomsnitt(tall_liste)
maks, minst = finn_maks_og_min(tall_liste)

print("Opprinnelig liste:", tall_liste)
print("Kvadrater av partallene:", kvadrater)
print("Summen av tallene:", total)
print("Gjennomsnittet av tallene:", gjennomsnitt)
print("Største tall:", maks)
print("Minste tall:", minst)
