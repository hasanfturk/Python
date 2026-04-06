#set (küme) veri yapısı

#dersler_set = {"Tarih","Matematik","Fizik",} #unordered (sırasız) tutulur,aynı elemandan bir tane tutar.

"""
list=["Tarih","Kimya","Kimya"]
print(list)
"""

"""
#sets --> mutable
dersler_set.add("Kimya")
dersler_set.remove("Tarih")
print("Kimya" in dersler_set)
print(dersler_set)
"""

muh_dersler_set ={"Tarih","Matematik","Fizik","Kimya"}
sanat_dersleri_set={"Tarih","Piyano","Sanat"}

#kesişim - intersection 
ortak_dersler_set=muh_dersler_set.intersection(sanat_dersleri_set)
print(ortak_dersler_set)

#fark-difference
muh_fark_set=muh_dersler_set.difference(sanat_dersleri_set)
print(muh_fark_set)

#birleşim-union
birlesim_set=muh_dersler_set.union(sanat_dersleri_set)
print(birlesim_set)