import requests
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """
    View principal que lida com requisições GET e POST para consulta de CEP.
    """
    context = {}
    
    if request.method == 'POST':
        cep = request.POST.get('cep', '').strip()
        
        if not cep:
            context['erro'] = 'Por favor, informe um CEP válido.'
        else:
            # Remove caracteres não numéricos do CEP
            cep_limpo = ''.join(filter(str.isdigit, cep))
            
            if len(cep_limpo) != 8:
                context['erro'] = 'CEP deve conter exatamente 8 dígitos.'
            else:
                try:
                    # Chama a API ViaCEP
                    url = f'https://viacep.com.br/ws/{cep_limpo}/json/'
                    response = requests.get(url, timeout=10)
                    
                    if response.status_code == 200:
                        data = response.json()
                        
                        # Verifica se o CEP foi encontrado
                        if 'erro' in data:
                            context['erro'] = 'CEP não encontrado. Verifique o número informado.'
                        else:
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
                    else:
                        context['erro'] = 'Erro ao consultar o CEP. Tente novamente mais tarde.'
                        
                except requests.exceptions.Timeout:
                    context['erro'] = 'Tempo limite excedido. Tente novamente.'
                except requests.exceptions.ConnectionError:
                    context['erro'] = 'Erro de conexão. Verifique sua internet.'
                except requests.exceptions.RequestException:
                    context['erro'] = 'Erro ao consultar o CEP. Tente novamente mais tarde.'
                except Exception as e:
                    context['erro'] = 'Erro interno. Tente novamente mais tarde.'
    
    return render(request, 'core/index.html', context)