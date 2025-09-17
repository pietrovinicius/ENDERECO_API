import requests
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """
    View principal que lida com requisições GET e POST para consulta de CEP.
    """
    print(f"\n{'='*50}")
    print(f"🔄 NOVA REQUISIÇÃO: {request.method}")
    print(f"{'='*50}")
    
    context = {}
    
    if request.method == 'GET':
        print("📄 Requisição GET - Exibindo página inicial")
        
    elif request.method == 'POST':
        print("📝 Requisição POST - Processando consulta de CEP")
        cep = request.POST.get('cep', '').strip()
        print(f"📍 CEP recebido: '{cep}'")
        
        if not cep:
            print("❌ Erro: CEP vazio")
            context['erro'] = 'Por favor, informe um CEP válido.'
        else:
            # Remove caracteres não numéricos do CEP
            cep_limpo = ''.join(filter(str.isdigit, cep))
            print(f"🧹 CEP limpo (apenas números): '{cep_limpo}'")
            
            if len(cep_limpo) != 8:
                print(f"❌ Erro: CEP deve ter 8 dígitos, mas tem {len(cep_limpo)}")
                context['erro'] = 'CEP deve conter exatamente 8 dígitos.'
            else:
                print("✅ CEP válido - Iniciando consulta à API")
                try:
                    # Chama a API ViaCEP
                    url = f'https://viacep.com.br/ws/{cep_limpo}/json/'
                    print(f"🌐 Fazendo requisição para: {url}")
                    
                    response = requests.get(url, timeout=10)
                    print(f"📡 Status da resposta: {response.status_code}")
                    
                    if response.status_code == 200:
                        data = response.json()
                        print(f"📦 Dados recebidos da API: {data}")
                        
                        # Verifica se o CEP foi encontrado
                        if 'erro' in data:
                            print("❌ CEP não encontrado na base de dados")
                            context['erro'] = 'CEP não encontrado. Verifique o número informado.'
                        else:
                            print("✅ CEP encontrado! Processando dados...")
                            # CEP encontrado, passa os dados para o template
                            context['endereco'] = {
                                'cep': data.get('cep', ''),
                                'logradouro': data.get('logradouro', ''),
                                'bairro': data.get('bairro', ''),
                                'localidade': data.get('localidade', ''),
                                'uf': data.get('uf', ''),
                                'complemento': data.get('complemento', ''),
                                'ddd': data.get('ddd', ''),
                                'ibge': data.get('ibge', ''),
                                'gia': data.get('gia', ''),
                                'siafi': data.get('siafi', '')
                            }
                            print(f"📋 Endereço processado: {context['endereco']['logradouro']}, {context['endereco']['bairro']}, {context['endereco']['localidade']}-{context['endereco']['uf']}")
                    else:
                        print(f"❌ Erro HTTP: Status {response.status_code}")
                        context['erro'] = 'Erro ao consultar o CEP. Tente novamente mais tarde.'
                        
                except requests.exceptions.Timeout:
                    print("⏰ Erro: Timeout na requisição")
                    context['erro'] = 'Tempo limite excedido. Tente novamente.'
                except requests.exceptions.ConnectionError:
                    print("🌐 Erro: Problema de conexão")
                    context['erro'] = 'Erro de conexão. Verifique sua internet.'
                except requests.exceptions.RequestException as e:
                    print(f"📡 Erro na requisição: {e}")
                    context['erro'] = 'Erro ao consultar o CEP. Tente novamente mais tarde.'
                except Exception as e:
                    print(f"💥 Erro interno: {e}")
                    context['erro'] = 'Erro interno. Tente novamente mais tarde.'
    
    print(f"🎯 Renderizando template com contexto: {list(context.keys())}")
    if 'endereco' in context:
        print("✅ Sucesso: Dados do endereço serão exibidos")
    elif 'erro' in context:
        print(f"❌ Erro será exibido: {context['erro']}")
    else:
        print("📄 Página inicial será exibida")
    
    return render(request, 'core/index.html', context)