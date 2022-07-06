
veiculo=int(input("Quantas rodas o veículo tem ?"))
peso=float(input("Qual o peso do veículo em KG ?"))
pessoas=int(input("Quantas pessoas cabem no veículo ?"))

if(veiculo==2) or (veiculo==3):
    {
        print("A categoria ideal é A")
    }
elif((veiculo==4)and(peso<=3500)and(pessoas<=8)):
    {
         print("A categoria ideal é B")
    }

elif((veiculo>=4)and(peso>=3500)and(peso<=6000)):
    {
         print("A categoria ideal é C")
    }

elif((veiculo>=4)and(pessoas>=8)):
    {
         print("A categoria ideal é D")
    }

elif((veiculo>=4)and(peso>=6000)):
    {
         print("A categoria ideal é E")
    }

else:
    {
         print("Dados incorretos para definição da categoria de habilitação")
    }