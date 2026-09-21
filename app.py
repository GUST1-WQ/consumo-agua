# Entrada
# Solicitação do tipo de imóvel e do consumo mensal de água
tipo_de_imovel = input("Tipo de imóvel (1 - Casa, 2 - Apartamento, 3 - Comercial): ")
consumo_mensal = float(input("Consumo mensal de água em m³: "))

# Processamento e saída
# Classificação do consumo com base no tipo de imóvel
match tipo_de_imovel:
    case "1" | "Casa" | "um" | "Um" | "casa":
        if consumo_mensal <= 25:
            print("Consumo moderado - dentro do padrão residencial.")
        else:
            print("Consumo excessivo - adote medidas de economia e verifique vazamentos.")
    case "2" | "Apartamento" | "dois" | "Dois" | "apartamento":
        if consumo_mensal < 10:
            print("Consumo econômico - excelente controle de água!")
        elif consumo_mensal <= 25:
            print("Consumo moderado - dentro do padrão residencial.")
        else:
            print("Consumo excessivo - adote medidas de economia e verifique vazamentos.")
    case "3" | "Comercial" | "três" | "Três" | "tres" | "três" | "comercial":
        print("Tarifa comercial aplicada - consulte o plano corporativo.")
    case _:
        print("Tipo de imóvel inválido.")