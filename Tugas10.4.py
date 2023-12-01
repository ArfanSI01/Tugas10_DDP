def filter_konsonan(kalimat):
    konsonan = ""
    for char in kalimat:
        if char.isalpha() and char.lower() not in ['a', 'e', 'i', 'o', 'u']:
            konsonan += char
    return konsonan

kalimat_asli = "Nurul Fikri"
hasil_konsonan = filter_konsonan(kalimat_asli)
print(hasil_konsonan)