from calculadora import somar, subtrair

"""
O pytest automaticamente encontra testes em arquivos que começam ou terminam com o 
prefixo test_. As funções de teste também devem começar com test_.
"""

def test_soma_positivos():
    """Testa a soma de dois números positivos."""
    # O 'assert' é a chave! Ele verifica se a condição é verdadeira.
    assert somar(2, 3) == 5

def test_soma_com_zero():
    """Testa a soma com um dos números sendo zero."""
    assert somar(5, 0) == 5

def test_subtracao_simples():
    """Testa uma subtração básica."""
    assert subtrair(10, 3) == 7

def test_subtracao_negativa():
    """Testa uma subtração que resulta em um número negativo."""
    assert subtrair(5, 8) == -3

"""
Para rodar o teste execute na linha de comando
$ pytest
"""