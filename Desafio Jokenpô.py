# %%
print("\033[35m===================================" + "\n\033[35m        PYTHON FOR GIRLS        " + "\n\033[35m SEJA BEM VINDO AO JOGO DE JOKENPO " + "\n\033[35m===================================")
print("\n\033[97mMenu de opções: \npedra \npapel \ntesoura")
jogador1 = input("\n\033[36mJogador(a) 1, digite o seu nome: ")
jogador2 = input("\n\033[36mJogador(a) 2, digite o seu nome: ")


def partida(num_partida):
    jogada1 = input(f"\n\033[32m{jogador1}, digite a sua {num_partida}ª jogada: ")
    jogada2 = input(f"\n\033[32m{jogador2}, digite a sua {num_partida}ª jogada: ")
    
    if jogada1 != "pedra" and jogada1 != "tesoura" and jogada1 != "papel":
        print("\n\033[31mEntrada inválida")
   
    if jogada1 == jogada2:
        return "\033[31mNão houve vencedor"
    elif (jogada1 == "pedra" and jogada2 == "tesoura") or (jogada1 == "tesoura" and jogada2 == "papel") or (jogada1 == "papel" and jogada2 == "pedra"):
        return'jogador1'
    elif (jogada2 == "pedra" and jogada1 == "tesoura") or (jogada2 == "tesoura" and jogada1 == "papel") or (jogada2 == "papel" and jogada1 == "pedra"):
        return 'jogador2'
    else:
        return 'jogador2'


resultado1= partida(1)
resultado2= partida(2)
resultado3= partida(3)


vitoriap1 = 0
vitoriap2 = 0

if resultado1 == 'jogador1':
    vitoriap1 += 1
elif resultado1 == 'jogador2':
    vitoriap2 += 1
else:
    pass

if resultado2 == 'jogador1':
    vitoriap1 += 1
elif resultado2 == 'jogador2':
    vitoriap2 += 1
else:
    pass

if resultado3 == 'jogador1':
    vitoriap1 += 1
elif resultado3 == 'jogador2':
    vitoriap2 += 1
else:
    pass

if vitoriap1 == vitoriap2:
    print("\033[31mEmpate")
elif vitoriap1 > vitoriap2:
    print(f"\n\033[33mJogador(a) {jogador1} venceu!")
else:
    print(f"\n\033[33mJogador(a) {jogador2} venceu!")


print(f"\n\n\033[35mNa primeira rodada o(a) {resultado1} venceu. \nNa segunda rodada o(a) {resultado2} venceu. \nNa terceira rodada o {resultado3} venceu. \nParabens pelo jogo!")





# %%

# %%
