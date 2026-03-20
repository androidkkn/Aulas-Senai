# Importa as classes necessárias do módulo padrão do Python para criar o servidor web
from http.server import HTTPServer,BaseHTTPRequestHandler

# Define uma classe personalizada que herda de BaseHTTPRequestHandler. Esta classe vai definir como o servidor processa e responde aos diferentes métodos HTTP (GET, POST, etc.)
class Servidor(BaseHTTPRequestHandler):
    
    # O método 'do_GET' é acionado automaticamente quando o servidor recebe uma requisição GET
    def do_GET(self):   
        # Envia o código de status HTTP 200 (OK), indicando que a requisição foi bem-sucedida
        self.send_response(200)
        # Sinaliza o fim do envio da resposta HTTP
        self.end_headers()
        # Escreve o corpo da resposta que o cliente (navegador) vai receber.
        self.wfile.write(b"Server ON")

    # O método 'do_POST' é acionado automaticamente quando o servidor recebe uma requisição POST
    def do_POST(self):
        # O método 'do_POST' é acionado automaticamente quando o servidor recebe uma requisição POST
        tamanho = int(self.headers['Content-Length'])
        # Lê o corpo da requisição exatamente até o tamanho informado no cabeçalho
        dados = self.rfile.read(tamanho)
        # O '.decode()' converte os dados recebidos de bytes de volta para texto (string).
        # Em seguida, imprime o texto recebido no console/terminal onde o servidor está rodando.
        print("Dados recebidos!", dados.decode())
        
        # Envia um código de status HTTP 200 (OK) de volta para o cliente que fez o POST
        self.send_response(200)
        # Finaliza o envio dos cabeçalhos desta resposta
        self.end_headers()
        # Envia uma mensagem de confirmação para o cliente, informando que o POST deu certo
        self.wfile.write(b"Post recebido")
        # Esta última linha configura, inicializa e mantém o servidor rodando.
        # - serve_forever(): Inicia um loop infinito, mantendo o servidor ligado e esperando requisições até você pará-lo manualmente (ex: apertando Ctrl+C no terminal).
HTTPServer(("0.0.0.0", 8000), Servidor).serve_forever()