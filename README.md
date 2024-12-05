# Helpful AI Assistant for Math and Science

## Visão Geral
Este programa é um assistente de IA projetado para resolver e criar perguntas relacionadas à matemática e ciências. Ele interpreta entradas fornecidas pelo usuário e responde com soluções ou cria questões relevantes, dependendo do tipo de solicitação. A IA utiliza ferramentas específicas para processar cálculos complexos e fornecer respostas precisas ou criativas.

## Features
- **Frameworks**: Python 3.x e bibliotecas específicas para cálculos e processamento de linguagem natural.
- **Custom Tools**: Integrações com APIs avançadas para resolver questões matemáticas e científicas.
- **Language Model**: Google Gemini para compreender e responder perguntas matemáticas e científicas.

## Tools
O programa utiliza as seguintes ferramentas:

1. **WolframAlpha**
   - Uma ferramenta para resolver problemas matemáticos complexos, realizar cálculos e fornecer informações científicas detalhadas.

2. **Python Repl**
   - Um ambiente de execução que permite a interpretação e execução de código Python para cálculos dinâmicos e geração de soluções programáticas.

## Como Funciona
Quando o usuário fornece uma entrada, o programa analisa o tipo de solicitação: 
1. Se a entrada é uma pergunta para resolver, o programa usa as ferramentas disponíveis para calcular ou responder a questão e retorna uma solução detalhada.
2. Se a entrada solicita a criação de perguntas, o programa gera questões relevantes, baseadas no tema especificado.

O fluxo lógico é o seguinte:
- Identificar o tipo de entrada (resolver ou criar perguntas).
- Selecionar a ferramenta apropriada.
- Processar a entrada.
- Retornar a resposta ou perguntas geradas.

## Exemplo de execução
**Input:**
``
What is -x^2 - 4x + 5 = 0?
``

**Output:**
The solutions to the quadratic equation -x² - 4x + 5 = 0 are x = 1 and x = -5.
```python
import cmath

def solve_quadratic(a, b, c):
  delta = (b**2) - 4*(a*c)
  if delta >= 0:
    x1 = (-b - delta**0.5) / (2*a)
    x2 = (-b + delta**0.5) / (2*a)
  else:
    x1 = (-b - cmath.sqrt(delta)) / (2 * a)
    x2 = (-b + cmath.sqrt(delta)) / (2 * a)
  return x1, x2

a = -1
b = -4
c = 5
x1, x2 = solve_quadratic(a, b, c)
print(f"The solutions are x1 = {x1} and x2 = {x2}")
```

## How to Run

1. **Instale as dependências:**
```python
pip install -r requirements.txt
```

2. **Crie um arquivo `.env` e configure as chaves de API (Gemini e WolframAlpha):**
```python
GOOGLE_API_KEY = 
WOLFRAM_ALPHA_APPID = 
```

3. **Pegue as variáveis:**
```python
from dotenv import load_dotenv
load_dotenv()
```

4. **Rode o programa:**
```python
streamlit run app.py
```

## Conclusão
Este programa fornece uma solução prática e eficaz para lidar com questões matemáticas e científicas, utilizando ferramentas avançadas e uma IA treinada. Ele é ideal tanto para estudantes quanto para profissionais que precisam de respostas rápidas e confiáveis para problemas complexos ou desejam criar novas questões para estudo ou avaliação.
