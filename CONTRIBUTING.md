# 🤝 Contribuindo para o Sistema de Consulta de Endereços

Obrigado por seu interesse em contribuir com este projeto! Este guia irá ajudá-lo a entender como contribuir de forma efetiva.

## 📋 Índice

- [Como Contribuir](#como-contribuir)
- [Configuração do Ambiente](#configuração-do-ambiente)
- [Padrões de Código](#padrões-de-código)
- [Processo de Pull Request](#processo-de-pull-request)
- [Reportando Bugs](#reportando-bugs)
- [Sugerindo Melhorias](#sugerindo-melhorias)
- [Estrutura do Projeto](#estrutura-do-projeto)

## 🚀 Como Contribuir

### 1. Fork do Repositório
```bash
# Clone seu fork
git clone https://github.com/SEU_USUARIO/ENDERECO_API.git
cd ENDERECO_API
```

### 2. Configuração do Ambiente
```bash
# Instale as dependências
pip install -r requirements.txt

# Execute o servidor de desenvolvimento
python manage.py runserver
```

### 3. Crie uma Branch
```bash
# Crie uma branch para sua feature/correção
git checkout -b feature/nome-da-sua-feature
# ou
git checkout -b fix/nome-do-bug
```

## ⚙️ Configuração do Ambiente

### Pré-requisitos
- Python 3.8+
- pip
- Git

### Instalação
1. Clone o repositório
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute o servidor: `python manage.py runserver`
4. Acesse: http://127.0.0.1:8000/

## 📝 Padrões de Código

### Python/Django
- Siga a PEP 8
- Use nomes descritivos para variáveis e funções
- Adicione docstrings para funções complexas
- Mantenha funções pequenas e focadas

### HTML/CSS
- Use indentação de 2 espaços
- Mantenha classes CSS organizadas
- Use nomes semânticos para classes

### JavaScript
- Use camelCase para variáveis
- Adicione comentários para lógica complexa
- Mantenha funções pequenas

### Exemplo de Código Python:
```python
def consultar_cep(cep):
    """
    Consulta informações de um CEP na API ViaCEP.
    
    Args:
        cep (str): CEP a ser consultado (apenas números)
    
    Returns:
        dict: Dados do endereço ou None se não encontrado
    """
    # Implementação aqui
    pass
```

## 🔄 Processo de Pull Request

### 1. Antes de Submeter
- [ ] Teste sua alteração localmente
- [ ] Verifique se não quebrou funcionalidades existentes
- [ ] Adicione prints de debug se necessário
- [ ] Atualize documentação se aplicável

### 2. Criando o PR
1. Faça push da sua branch
2. Abra um Pull Request no GitHub
3. Use um título descritivo
4. Descreva as alterações realizadas
5. Adicione screenshots se houver mudanças visuais

### 3. Template de PR
```markdown
## 📋 Descrição
Breve descrição das alterações realizadas.

## 🔧 Tipo de Mudança
- [ ] Bug fix
- [ ] Nova feature
- [ ] Melhoria de performance
- [ ] Refatoração
- [ ] Documentação

## ✅ Checklist
- [ ] Código testado localmente
- [ ] Documentação atualizada
- [ ] Prints de debug adicionados (se necessário)

## 📸 Screenshots (se aplicável)
Adicione screenshots das mudanças visuais.
```

## 🐛 Reportando Bugs

### Antes de Reportar
1. Verifique se o bug já foi reportado
2. Teste com a versão mais recente
3. Colete informações do erro

### Template de Bug Report
```markdown
## 🐛 Descrição do Bug
Descrição clara do que está acontecendo.

## 🔄 Passos para Reproduzir
1. Vá para '...'
2. Clique em '...'
3. Veja o erro

## ✅ Comportamento Esperado
O que deveria acontecer.

## 📱 Ambiente
- OS: [Windows/Mac/Linux]
- Browser: [Chrome, Firefox, etc.]
- Python: [versão]
- Django: [versão]

## 📋 Logs
Adicione logs do console se disponíveis.
```

## 💡 Sugerindo Melhorias

### Template de Feature Request
```markdown
## 🚀 Descrição da Feature
Descrição clara da funcionalidade sugerida.

## 🎯 Problema que Resolve
Que problema esta feature resolve?

## 💭 Solução Proposta
Como você imagina que deveria funcionar?

## 🔄 Alternativas Consideradas
Outras formas de resolver o problema.
```

## 📁 Estrutura do Projeto

```
ENDERECO_API/
├── cep_project/          # Configurações do Django
│   ├── settings.py       # Configurações principais
│   ├── urls.py          # URLs principais
│   └── ...
├── core/                # App principal
│   ├── views.py         # Lógica de negócio
│   ├── urls.py          # URLs do app
│   ├── templates/       # Templates HTML
│   └── ...
├── manage.py            # Script de gerenciamento Django
├── requirements.txt     # Dependências Python
└── README.md           # Documentação principal
```

## 🎯 Áreas que Precisam de Contribuição

### 🔧 Funcionalidades
- [ ] Histórico de consultas
- [ ] Cache de resultados
- [ ] API própria
- [ ] Testes automatizados
- [ ] Validação avançada de CEP

### 🎨 Interface
- [ ] Modo escuro
- [ ] Responsividade mobile
- [ ] Animações
- [ ] Acessibilidade

### 📚 Documentação
- [ ] Exemplos de uso
- [ ] Guias de instalação
- [ ] Documentação da API
- [ ] Tutoriais

## 🏷️ Convenções de Commit

Use mensagens de commit descritivas:

```bash
# Exemplos bons
git commit -m "Adiciona validação de CEP com regex"
git commit -m "Corrige erro de timeout na API ViaCEP"
git commit -m "Melhora responsividade do formulário"

# Evite
git commit -m "fix"
git commit -m "update"
git commit -m "changes"
```

## 📞 Contato

- **Issues**: Use as issues do GitHub para dúvidas técnicas
- **Discussões**: Use as discussões do GitHub para ideias gerais

## 📄 Licença

Ao contribuir, você concorda que suas contribuições serão licenciadas sob a mesma licença do projeto.

---

**Obrigado por contribuir! 🎉**

Sua contribuição ajuda a tornar este projeto melhor para toda a comunidade.