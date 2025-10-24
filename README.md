# Executando Testes Unitários em uma Aplicação Python Simples
Usamos o pytest (o framework de testes mais popular do Python) para verificar se nossa lógica de negócios (a função soma() na nossa calculadora) funciona corretamente.

Se algum teste falhar, o GitHub Actions bloqueia o workflow e nos avisa que o código novo "quebrou" algo.

- app/ --> Contém o código da aplicação (calculator.py).
- tests/ --> Contém os testes unitários (test_calculator.py).
- requirements.txt --> Lista as dependências do projeto (principalmente o pytest).
- .github/workflows/tests.yml -->	O nosso fluxo de CI que instala o Python e executa o pytest.
