Visto a dificulade na busca de desaparecidos no desastre natural no RS, este script provém uma forma prática de mapear a possível localização geografica dos desaparecidos,
por meio do sinal de celular, utilizando a técnica de triangulação.

O input consiste de um arquivo CSV que contém dos dados de latitude e longitude de 3 antenas e a distantancia de cada uma até o celular.
Feito isso, é gerado um mapa.html com a localização extraída de cada linha do CSV que pode facilitar nas buscas e salvamento.


Com o Python instalado, para executar:
1: pip3 install -r requirements.txt
2: Certifique-se de ter um arquivo CSV chamado input.csv com as seguintes colunas: latitude_p1, longitude_p1, latitude_p2, longitude_p2, latitude_p3, longitude_p3, dist_p1, dist_p2, dist_p3.

As colunas latitude_p1, longitude_p1, latitude_p2, longitude_p2, latitude_p3, longitude_p3 devem conter as coordenadas de três pontos representados por P1, P2 e P3.

As colunas dist_p1, dist_p2, dist_p3 devem conter as distâncias dos pontos P1, P2 e P3 ao ponto de interseção que deseja calcular.

Imagens:

Método:
<img width="564" alt="geogebra_modelo" src="https://github.com/FonteneleLucas/calculador_triangulacao/assets/18284262/15705188-6386-45d8-a974-577a3e5d1d23">

Input:
<img width="613" alt="csv_input" src="https://github.com/FonteneleLucas/calculador_triangulacao/assets/18284262/f4207875-6fd8-4acf-a42b-a2254f523d72">
