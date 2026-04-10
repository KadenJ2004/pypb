import tokenize
import io
import sys

dicionario = {
# Controle de Fluxo
    'como': 'as',
    'afirmar': 'assert',
    'interromper': 'break',
    'classe': 'class',
    'continuar': 'continue',
    'definir': 'def',
    'def': 'def',
    'excluir': 'del',
    'apagar': 'del',
    'senaose': 'elif',
    'senãose': 'elif',
    'senao': 'else',
    'senão': 'else',
    'excecao': 'except',
    'exceção': 'except',
    # 'capturar': 'except',
    'finalmente': 'finally',
    'para': 'for',
    'de': 'from',
    'se': 'if',
    'importar': 'import',
    'em': 'in',
    'eh': 'is',
    'é': 'is',
    'naolocal': 'nonlocal',
    'nãolocal': 'nonlocal',
    'passar': 'pass',
    'lancar': 'raise',
    'lançar': 'raise',
    'retornar': 'return',
    'tentar': 'try',
    'enquanto': 'while',
    'com': 'with',
    'gerar': 'yield',
    # 'produzir': 'yield',
# Lógico e Booleanos
    'e': 'and',
    'Falso': 'False',
    'Nenhum': 'None',
    'nao': 'not',
    'não': 'not',
    'ou': 'or',
    'Verdadeiro': 'True',
# Tipos de Dados e Conversão de Tipos
    'bool': 'bool',
    'bytes': 'bytes',
    'dicionario': 'dict',
    'dicionário': 'dict',
    'decimal': 'float',
    'float': 'float',
    'inteiro': 'int',
    'int': 'int',
    'lista': 'list',
    'conjunto': 'set',
    'texto': 'str',
    # 'str': 'str',
    'tupla': 'tuple',
# Funções Embutidas
    'absoluto': 'abs',
    'abs': 'abs',
    'diretorio': 'dir',
    'dir': 'dir',
    'enumerar': 'enumerate',
    'avaliar': 'eval',
    'filtrar': 'filter',
    'formatar': 'format',
    'ajuda': 'help',
    'entrada': 'input',
    'ler': 'input',
    'tamanho': 'len',
    'mapear': 'map',
    'maximo': 'max',
    'máximo': 'max',
    'max': 'max',
    'minimo': 'min',
    'mínimo': 'min',
    'min': 'min',
    'abrir': 'open',
    'imprimir': 'print',
    'escrever': 'print',
    'intervalo': 'range',
    'arredondar': 'round',
    'ordenar': 'sorted',
    'ordenado': 'sorted',
    'somar': 'sum',
    'tipo': 'type',
    'juntar': 'zip',
# Métodos de Lista
    'adicionar': 'append',
    'limpar': 'clear',
    'copiar': 'copy',
    'contar': 'count',
    'estender': 'extend',
    'indice': 'index',
    'índice': 'index',
    'inserir': 'insert',
    'sacar': 'pop',
    'remover': 'remove',
    'inverter': 'reverse',
    'organizar': 'sort',
# Métodos de Dicionário
    'pegar': 'get',
    'itens': 'items',
    'chaves': 'keys',
    'atualizar': 'update',
    'valores': 'values',
# Métodos de Texto
    'capitalizar': 'capitalize',
    'terminacom': 'endswith',
    'encontrar': 'find',
    'unir': 'join',
    'minusculo': 'lower',
    'minúsculo': 'lower',
    'substituir': 'replace',
    'dividir': 'split',
    'comecacom': 'startswith',
    'começacom': 'startswith',
    'remover_espacos': 'strip',
    'remover_espaços': 'strip',
    'titulo': 'title',
    'título': 'title',
    'maiusculo': 'upper',
    'maiúsculo': 'upper',
# Métodos de Arquivo (File Methods)
    'fechar': 'close',
    'ler_arquivo': 'read',
    'gravar': 'write',
}

def traduzir_codigo(codigo_pt):
    tokens_traduzidos = []
    stream = io.BytesIO(codigo_pt.encode('utf-8'))

    for tok in tokenize.tokenize(stream.readline):
        tipo_token = tok.type
        valor_token = tok.string

        if tipo_token == tokenize.NAME and valor_token in dicionario:
            tokens_traduzidos.append((tipo_token, dicionario[valor_token]))
        else:
            tokens_traduzidos.append((tipo_token, valor_token))

    return tokenize.untokenize(tokens_traduzidos).decode("utf-8")

def main():
    if len(sys.argv) < 2:
        print("Uso: python pypb/tradutor.py <arquivo.pypb>")
        return
    
    caminho = sys.argv[1]
    with open(caminho, 'r', encoding = 'utf-8') as f:
        codigo_pt = f.read()
        codigo_en = traduzir_codigo(codigo_pt)

    try:
        exec(codigo_en)
    except Exception as e:
        print(f"Erro na execução: {e}")

if __name__== "__main__":
    main()