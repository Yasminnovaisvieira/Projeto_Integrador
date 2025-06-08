import http.server
import socketserver
import ssl

# Configurações do servidor
PORT = 8080  # Porta em que o servidor vai rodar
DIRECTORY = "."


# Está bem completo, ficou muito bom o site e o server
# Acho q a unica coisa que eu faria de diferente é usar container para a aplicação em sí
# E criar mais arquivos CSS para não ficar no código
# Usar modularização do CSS seria uma boa

# Acho que se estive usando uma estrutura mais robusta como React, Next, Vue ou Angular
# você teria muito mais liberdade e seria um projeto muito mais profissional, pq o design
# e codigo estão bem profissionais

# Tutorial para limpar suas credenciais do GitHub
# Gerenciador de Credenciais > Credenciais do Windows > git:https://github.com > Remover

# Não esqueça de usar guia anônima :)

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'html/index.html'  # Página padrão para servir
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


# Inicia o servidor usando ThreadingTCPServer
with socketserver.ThreadingTCPServer(("", PORT), MyHttpRequestHandler) as httpd:
    # Configuração do SSL
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")

    # Envolvendo o socket do servidor com SSL usando SSLContext
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

    print(f"Servidor HTTPS iniciado na porta {PORT}. Acesse https://localhost:{PORT}")
    httpd.serve_forever()