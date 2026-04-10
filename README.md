# 🇧🇷 PyPB (Python Para Brasileiros)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

**PyPB** é uma linguagem educacional construída sobre o Python, projetada para ensinar a lógica de programação usando o vocabulário natural do Português. 

Por baixo dos panos, o PyPB traduz o seu código em português para Python nativo em tempo real e o executa instantaneamente. Isso dá aos iniciantes o poder de uma linguagem profissional com o conforto de aprender no seu idioma materno.

## 🌟 Por que o PyPB?
Aprender a programar já é difícil o suficiente sem ter que traduzir comandos do inglês na sua cabeça. O PyPB permite que os estudantes se concentrem na **lógica** de estruturas de controle, loops e manipulação de dados usando o vocabulário que já conhecem.

---

## 🚀 Instalação

Você pode instalar o PyPB diretamente pelo terminal usando o gerenciador de pacotes do Python (`pip`). Abra o seu terminal e digite:

```bash
pip install pypb-br
```

---

## 💻 Como Usar

### Pelo Terminal
Após instalar, você pode criar qualquer arquivo de texto com a extensão `.pypb` (ou apenas `.py`) e rodá-lo pelo terminal usando o comando `pypb`:

```bash
pypb meu_programa.pypb
```

### Configurando o VS Code
Se você usa o Visual Studio Code, pode configurar um atalho para rodar seu código em português instantaneamente:

1. Crie uma pasta chamada `.vscode` na raiz do seu projeto.
2. Dentro dela, crie um arquivo chamado `tasks.json`.
3. Cole a seguinte configuração:

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Executar Código PYPB",
            "type": "shell",
            "command": "pypb",
            "args": [
                "${file}"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "presentation": {
                "reveal": "always",
                "panel": "shared",
                "clear": true
            }
        }
    ]
}
```
*Dica: Agora você pode executar seu código simplesmente pressionando `Ctrl+Shift+B` (ou `Cmd+Shift+B` no Mac).*

---

## 📝 Exemplo de Código

Aqui está como um programa em PyPB se parece na prática:

```python
# Um simples sistema de notas
notas = []

enquanto Verdadeiro:
    entrada_usuario = ler("Digite uma nota (ou 'sair'): ")
    
    se entrada_usuario.minusculo() == "sair":
        interromper
        
    notas.adicionar(inteiro(entrada_usuario))

imprimir("A maior nota foi: " + texto(maximo(notas)))
imprimir("A média foi: " + texto(somar(notas) / tamanho(notas)))
```

---

### 💡 Dica de Ouro: Acentos são Opcionais!
O PyPB foi projetado para ser amigável para iniciantes. Se você esquecer um acento na pressa de digitar, não se preocupe! A linguagem entende tanto as palavras com acento quanto sem acento.

**Ambos funcionam perfeitamente:**
* `senão` ou `senao`
* `título()` ou `titulo()`
* `começacom()` ou `comecacom()`
* `maiúsculo()` ou `maiusculo()`

---

## 📚 Dicionário de Referência

O PyPB suporta a tradução direta de todas as estruturas principais do Python. Abaixo está a lista completa de comandos disponíveis.

### Controle de Fluxo
| PyPB (Português) | O que faz? | Python Nativo |
| :--- | :--- | :--- |
| `se`, `senaose`, `senao` | Condições lógicas (If/Elif/Else). | `if`, `elif`, `else` |
| `para`, `em` | Laço de repetição (Loop). | `for`, `in` |
| `enquanto` | Laço de repetição baseado em condição. | `while` |
| `interromper`, `continuar` | Controla o fluxo dentro de um laço. | `break`, `continue` |
| `definir` / `def` | Cria uma função personalizada. | `def` |
| `retornar` | Devolve o resultado de uma função. | `return` |
| `tentar`, `excecao`, `finalmente` | Tratamento de erros. | `try`, `except`, `finally` |
| `lancar` | Gera um erro propositalmente. | `raise` |
| `importar`, `de`, `como` | Traz bibliotecas externas para o código. | `import`, `from`, `as` |
| `classe`, `passar`, `eh` | Estruturas avançadas e de identidade. | `class`, `pass`, `is` |

### Lógica e Tipos de Dados
| PyPB (Português) | O que faz? | Python Nativo |
| :--- | :--- | :--- |
| `Verdadeiro`, `Falso`, `Nenhum` | Valores booleanos e nulos. | `True`, `False`, `None` |
| `e`, `ou`, `nao` | Operadores lógicos (And/Or/Not). | `and`, `or`, `not` |
| `texto` | Sequência de caracteres (String). | `str` |
| `inteiro`, `decimal` | Números sem e com vírgula. | `int`, `float` |
| `lista`, `dicionario`, `tupla` | Coleções de dados. | `list`, `dict`, `tuple` |

### Funções Embutidas (Built-ins)
| PyPB (Português) | O que faz? | Python Nativo |
| :--- | :--- | :--- |
| `imprimir()` / `escrever()` | Mostra dados na tela. | `print()` |
| `ler()` / `entrada()` | Pede para o usuário digitar algo. | `input()` |
| `tamanho()` | Conta os itens de uma coleção ou texto. | `len()` |
| `somar()`, `maximo()`, `minimo()`| Operações matemáticas em listas. | `sum()`, `max()`, `min()` |
| `arredondar()`, `absoluto()` | Funções matemáticas para números. | `round()`, `abs()` |
| `ordenar()`, `juntar()` | Organiza e combina listas. | `sorted()`, `zip()` |
| `intervalo()`, `enumerar()` | Gera sequências numéricas para loops. | `range()`, `enumerate()` |
| `tipo()`, `ajuda()`, `diretorio()`| Ferramentas de inspeção do código. | `type()`, `help()`, `dir()` |

### Métodos de Lista
Usados diretamente após uma lista (ex: `minha_lista.adicionar(item)`).

| PyPB (Português) | Python Nativo |
| :--- | :--- |
| `.adicionar()` | `.append()` |
| `.remover()`, `.sacar()`, `.limpar()` | `.remove()`, `.pop()`, `.clear()` |
| `.organizar()`, `.inverter()` | `.sort()`, `.reverse()` |
| `.indice()`, `.contar()` | `.index()`, `.count()` |
| `.inserir()`, `.estender()` | `.insert()`, `.extend()` |

### Métodos de Dicionário
Usados diretamente após um dicionário.

| PyPB (Português) | Python Nativo |
| :--- | :--- |
| `.pegar()`, `.atualizar()` | `.get()`, `.update()` |
| `.chaves()`, `.valores()`, `.itens()` | `.keys()`, `.values()`, `.items()` |

### Métodos de Texto
Usados diretamente após uma string (texto).

| PyPB (Português) | Python Nativo |
| :--- | :--- |
| `.maiusculo()`, `.minusculo()` | `.upper()`, `.lower()` |
| `.capitalizar()`, `.titulo()` | `.capitalize()`, `.title()` |
| `.substituir()`, `.dividir()`, `.unir()` | `.replace()`, `.split()`, `.join()` |
| `.remover_espacos()` | `.strip()` |
| `.comecacom()`, `.terminacom()` | `.startswith()`, `.endswith()` |
| `.encontrar()` | `.find()` |

### Métodos de Arquivo
Usados quando você abre um arquivo com `abrir()`.

| PyPB (Português) | Python Nativo |
| :--- | :--- |
| `.ler_arquivo()` | `.read()` |
| `.gravar()` | `.write()` |
| `.fechar()` | `.close()` |

---

## 🤝 Contribuições e Sugestões

O PyPB é um projeto de código aberto e em constante evolução! Se você tem ideias para novos comandos, encontrou um bug, ou quer melhorar a documentação, sua ajuda é muito bem-vinda. 

Existem várias formas de participar:
* **Sugestões e Bugs:** Sinta-se à vontade para abrir uma *Issue* na página do GitHub do projeto.
* **Melhorias no Código:** Faça um *Fork* do repositório, adicione suas melhorias e envie um *Pull Request*.

### 📬 Contato
Se você quiser conversar sobre o projeto, dar um feedback de como está usando o PyPB, ou se precisar de ajuda, pode entrar em contato diretamente comigo:

* **Email:** kadeneichelberger@gmail.com
* **GitHub:** [KadenJ2004](https://github.com/KadenJ2004)