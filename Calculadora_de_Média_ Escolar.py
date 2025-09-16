print ("Bem vindo a calculadora de media escolar 😁")

nota1= float (input("digite a nota do 1ª Bimestre:"))
nota2 = float (input("digite a nota do 2ª Bimestre:"))
nota3 = float (input("digite a nota do 3ª Bimestre:"))
nota4 = float (input("digite a nota do 4ª Bimestre:"))

print ("nota do 1ª Bimestre: ", nota1 )
print ("nota do 2ª Bimestre: ", nota2 )
print ("nota do 3ª Bimestre: ", nota3 )
print ("nota do 4ª Bimestre: ", nota4 )
media_escolar_final = (nota1 + nota2 + nota3 + nota4) / 4


print ("mostrar media_escolar_final:",media_escolar_final)

if media_escolar_final>= 7:
    print ("Parabens! você foi aprovado 😁✅")


elif media_escolar_final >=5.0 < 7.0:
    print ("Você ficou de recuperaçâo, CUIDADO ⚠️ ")

elif media_escolar_final< 5.0: 
    print("REPROVADO ❌")

else:
    quit()