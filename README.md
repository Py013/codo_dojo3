# Coding Dojo Py013 - 18/10/2025
Terceiro (na verdae 4o) coding dojo da py013 - Tema Webscraping

# Regras do Coding Dojo
* Obrigatoriamente deverá ser codificado o teste (utilizando pytest preferencialmente, exemplo (https://github.com/Py013/codo_dojo3/tree/main/exemplo_pytest) antes do desenvolvimetno da funcionaldiade
* Sempre teremos um piloto e um navegador. Somente o piloto tem acesso ao teclado e mouse, e no período de 5 minutos irá realizar a codificação da solução, o navegador é a única pessoa que pode falar com o piloto durante esse tempo. Terminado os 5 minutos, o piloto vai para a platéia, o navegador assume o papel de piloto, e uma pessoa da platéia assume o papel do navegador. Esse ciclo se repete a cada 5 minutos.

# Desafio
* A partir de um arquivo .csv contendo uma lista de cidades, o programa deve pesquisar a temperatura atual de cada uma.
* Use a API de clima do `wttr.in` para buscar a temperatura atual de cada cidade. Por exemplo: https://wttr.in/Santos?format=j1 retorna um JSON com dados de Santos.
* Atualize o .csv para criar uma coluna `temperatura_c`, com a temperatura atual em Celsius (propriedade `temp_C` do JSON), e coloque em cada linha a temperatura da cidade respectiva.
* A tela também exibirá as temperaturas registradas para as cidades, informando quais cidades possuem a maior e menor temperatura entre elas.

# Desafios opcionais
* Também adicione a condição de céu (dentro de `current_condition` no JSON) de cada cidade no arquivo .csv
