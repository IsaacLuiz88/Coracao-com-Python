Desenhando Feixes de Luz:

A principal diferença agora é que, em vez de desenharmos um ponto pequeno (como no código anterior), estamos desenhando uma linha (create_line) que vai do centro da tela até o ponto do coração. Isso cria a sensação de que a luz (feixe) está se estendendo para preencher o coração.
Cada linha é desenhada do centro (largura//2, altura//2) até o ponto calculado pela fórmula paramétrica do coração, o que gera a forma de preenchimento.
Uso de create_line:

A função create_line(x1, y1, x2, y2) é usada para desenhar uma linha entre os pontos (x1, y1) e (x2, y2). Aqui, os valores (x1, y1) são o centro da tela e (x2, y2) são as coordenadas do ponto do coração.
O feixe de luz é desenhado com a cor vermelha (fill="red") e uma espessura de linha de 2 pixels (width=2).
Ordem Aleatória:

A linha é desenhada de forma aleatória, ligando o centro aos pontos do coração. A lista indices é embaralhada para garantir que a ordem dos pontos seja aleatória a cada execução.
Animação:

O uso de root.after(10, desenhar) garante que a animação seja progressiva, com um atraso de 10 milissegundos entre cada linha desenhada, criando um efeito de preenchimento gradual.
Como Funciona:
Feixe de Luz: Cada linha vermelha é desenhada a partir do centro da tela até os pontos do coração, criando o efeito de "laser". A linha é desenhada progressivamente.
Ordem Aleatória: As linhas são desenhadas em ordem aleatória, criando um efeito dinâmico e imprevisível de preenchimento.
Progresso Gradual: O coração é preenchido gradualmente, conectando o centro aos pontos da curva do coração, até que ele esteja totalmente preenchido.
Personalizações:
Cor do Feixe:

Para mudar a cor do feixe de luz, altere o valor de fill="red" para qualquer cor de sua preferência, como "blue", "green", etc.
Velocidade da Animação:

O parâmetro de delay root.after(10, desenhar) pode ser ajustado para controlar a velocidade de desenho. Reduza o valor para uma animação mais rápida, ou aumente para uma animação mais lenta (ex: root.after(5, desenhar) ou root.after(20, desenhar)).
Espessura da Linha:

O valor width=2 pode ser ajustado para aumentar ou diminuir a espessura do feixe de luz. Por exemplo, width=5 criará linhas mais grossas.
Teste e Resultado Esperado:
Ao executar o código, você verá um feixe de luz vermelho que começa do centro da tela e vai preenchendo o coração gradualmente, conectando o centro a vários pontos do contorno do coração. A animação vai preenchendo todo o coração até que ele esteja completamente "iluminado", criando o efeito visual de uma luz dinâmica.

Função reiniciar_desafio:

A função reiniciar_desafio é responsável por apagar o conteúdo do canvas usando canvas.delete("all") e depois chamar novamente a função desenha_coracao para recomeçar o processo de desenho do coração.
A função root.after(5000, reiniciar_desafio, canvas) agendando a execução de reiniciar_desafio após 5 segundos (5000 milissegundos). O número 5000 pode ser ajustado para aumentar ou diminuir o tempo entre os ciclos de animação.
Animação Contínua:

O processo de desenho é iniciado uma vez e, após 5 segundos, o canvas é limpo e o coração começa a ser desenhado novamente.
Esse ciclo vai se repetir indefinidamente, criando um loop contínuo.
Função desenha_coracao:

A função desenha_coracao continua a mesma, mas agora ela será chamada repetidamente a partir de reiniciar_desafio.
O Que Esperar:
O coração será desenhado com o feixe de luz a partir do centro.
Depois que o coração for totalmente desenhado, ele será apagado e o processo de animação será reiniciado após 5 segundos (ou o intervalo que você definir).
Personalizações:
Alterar o Intervalo do Loop:

O intervalo de tempo entre o reinício do desenho pode ser ajustado no valor de root.after(5000, reiniciar_desafio, canvas). A quantidade de tempo (em milissegundos) entre os ciclos pode ser aumentada ou diminuída conforme necessário.
Controle de Velocidade:

A velocidade de desenho pode ser alterada modificando o valor de root.after(10, desenhar), onde 10 é o tempo (em milissegundos) entre o desenho de cada linha. Valores menores tornam a animação mais rápida, enquanto valores maiores tornam a animação mais lenta.
Alterar a Cor ou Tamanho do Feixe:

Para modificar a cor do feixe de luz, basta alterar o parâmetro fill="red" dentro da função create_line.
A espessura da linha pode ser ajustada em width=2, aumentando ou diminuindo o valor de 2.
Resultado Esperado:
O programa agora irá desenhar o coração com luzes (feixes vermelhos), preencherá a forma de maneira progressiva, e após o tempo definido (5 segundos neste caso), apagará o coração e reiniciará o processo, criando um loop contínuo.
