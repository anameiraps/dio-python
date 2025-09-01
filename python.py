def gerenciar_reservas(quartos_disponiveis, reservas_solicitadas):
    confirmadas = []
    recusadas = []

    for quarto in reservas_solicitadas:
        if quarto in quartos_disponiveis:
            confirmadas.append(quarto)
        else:
            recusadas.append(quarto)

    print("Reservas confirmadas: " + " ".join(map(str, confirmadas)))
    print("Reservas recusadas: " + " ".join(map(str, recusadas)))


# Entrada
quartos_disponiveis = list(map(int, input().split()))
reservas_solicitadas = list(map(int, input().split()))

# Saída
gerenciar_reservas(quartos_disponiveis, reservas_solicitadas)