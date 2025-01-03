import tkinter as tk
import random
import math

# Função para desenhar o coração
def desenha_coracao(canvas):
    largura = 600  # Aumentando a largura da tela para maior visualização
    altura = 600   # Aumentando a altura da tela
    raio = 5       # Pequeno raio para a linha (feixe de luz)
    step = 0.05    # O "passo" vai determinar a resolução do desenho
    escala = 15    # Fator de escala para aumentar o tamanho do coração
    pontos = []

    # Gerar os pontos do coração usando a fórmula paramétrica
    for t in range(0, 628, int(step * 100)):  # 0 até 2π (em centésimos)
        t = t / 100  # Convertendo para a forma de radianos
        x = 16 * math.sin(t) ** 3
        y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        
        # Escalar as coordenadas
        x *= escala
        y *= escala
        
        pontos.append((x, y))

    # Função para desenhar o feixe de luz
    def desenhar_luz():
        # Aleatoriza a ordem dos pontos
        indices = list(range(len(pontos)))
        random.shuffle(indices)  # Aleatoriza os índices dos pontos

        def desenhar():
            if indices:
                # Pega o próximo ponto aleatório
                idx = indices.pop()
                x, y = pontos[idx]

                # Desenha a linha (feixe de luz) do centro até o ponto calculado
                canvas.create_line(largura//2, altura//2, largura//2 + x, altura//2 - y, fill="red", width=2)
                
                # Agenda a próxima iteração para desenhar o próximo feixe
                root.after(10, desenhar)  # Delay de 10ms para animar os pontos

        desenhar()

    # Inicia o desenho progressivo do feixe de luz
    desenhar_luz()

# Função para limpar o canvas e reiniciar o desenho
def reiniciar_desafio(canvas):
    canvas.delete("all")  # Apaga todo o conteúdo do canvas
    desenha_coracao(canvas)  # Recomeça o desenho do coração
    root.after(3000, reiniciar_desafio, canvas)  # Após 5 segundos, reinicia o processo

# Configuração da interface gráfica
root = tk.Tk()
root.title("Coração com Feixe de Luz em Loop")

# Configuração do tamanho da janela e fundo preto
largura = 600
altura = 600
canvas = tk.Canvas(root, width=largura, height=altura, bg="black")
canvas.pack()

# Inicia o desenho do coração com o feixe de luz
reiniciar_desafio(canvas)

# Inicia o loop da interface gráfica
root.mainloop()
