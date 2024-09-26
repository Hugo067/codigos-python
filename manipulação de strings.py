# função len
a = "hugo"
print(len(a))

# função capitalize
a = "hugo"
print(a.capitalize())

# função upper
a = "hugo"
print(a.upper())

# função casefold
a = "hugo"
print(a.casefold())

# função lower
a = "hugo"
print(a.lower())

# função islower
a = "hugo"
print(a.islower())

# função isupper
a = "hugo"
print(a.isupper())

#função isdigit
a = "hugo"
print(a.isdigit())

#função replace
a = "hugo henrique"
print(a.replace("henrique", "hugo"))

# função split
a = "hugo-henrique-de-sousa-freres"
print (a.split("-"))

#função find
a = "hugo henrique de sousa freres"
print(a.find("henrique"))

#função in
a = "hugo henrique de sousa freres"
print("henrique" in a)

#função count
a = "hugo henrique de sousa freres"
print(a.count("u"))

#função substrings
a = "hugo henrique de sousa freres"
print(a[0:22])
print(a[11])
print(a[0])

#se omitir vai começar desde o primeiro e vai até onde mandar parar
a = "hugo"
print(a[:30])

#
a = "hugo"
print(a[ : ])