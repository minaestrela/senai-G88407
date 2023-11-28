def calcular_custo_viagem(tipo_Veiculo):
    if tipo_Veiculo == 1:
        custo_por_km = 0.50
    elif tipo_Veiculo == 2:
        custo_por_km = 0.20
    elif tipo_Veiculo == 3:
        custo_por_km = 0.10
    
    else: 
        print("Tipo de veículo inválido.")
        
    return custo_por_km


tipo_Veiculo = int(input("Insira o tipo de veículo.\n"
                     "Digite 1 --> Carro\n"
                     "Digite 2 --> Moto\n"
                     "Digite 3 --> Bicicleta\n"))

distancia = float(input("Insira a distância percorrida: "))

custo_por_km = calcular_custo_viagem(tipo_Veiculo)

custo_total = distancia * custo_por_km
print(custo_total)