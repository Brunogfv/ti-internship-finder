# 🚀 TI Internship Finder - Guia de Uso

Sistema automatizado para buscar vagas de estágio em TI.

## 📋 Como Usar

### Opção 1: Busca Manual (Uma vez)
```bash
executar.bat
```
Ou:
```bash
python main.py
```
✅ Busca vagas uma única vez e salva no banco de dados, Telegram e email.

### Opção 2: Agendamento Automático (Diário)
```bash
agendador.bat
```
Ou:
```bash
python scheduler.py
```
✅ O sistema roda TODOS OS DIAS às 9:00 da manhã até você desligar.

### Opção 3: API REST (Consultar vagas)
```bash
api_start.bat
```
Ou:
```bash
python -m uvicorn api:app --reload
```
✅ Acesse em: http://127.0.0.1:8000/docs

## 📊 Onde Ver os Resultados

| Local | Tipo | Descrição |
|-------|------|-----------|
| `jobs.csv` | Arquivo | Todas as vagas em formato CSV |
| `jobs.db` | Banco | Banco SQLite com todas as vagas |
| `logs/system.log` | Log | Histórico de execuções |
| **Telegram** | Chat | Notificações automáticas de novas vagas |
| **Email** | Email | Resumo diário (bruno.gfv@gmail.com) |

## 🔧 Configurações

As configurações estão em `config.py`:
- ✅ Email: bruno.gfv@gmail.com
- ✅ Token Telegram: Configurado
- ✅ Chat ID: 969624447

Para alterar, edite `config.py` diretamente.

## 📱 Notificações Telegram

Você receberá automaticamente no Telegram:
- Novas vagas de estágio encontradas
- Link direto para acessar a vaga
- Informações: título, empresa, localização

## 📧 Notificações Email

Você receberá um email diário em: **bruno.gfv@gmail.com**
- Resumo das novas vagas do dia
- Horário: Junto com a busca agendada (9:00)

## 🛠️ Resolver Problemas

### Telegram não funciona?
1. Verifique se o bot está ativo em @BotFather
2. Envie uma mensagem ao bot
3. Confira o Chat ID em `config.py`

### Email não funciona?
1. Verifique a "Senha de App" em: myaccount.google.com > Segurança
2. Verifique se é Gmail (outra conta pode não funcionar)
3. Veja os logs em `logs/system.log`

### Vagas não aparecem?
1. Verifique `logs/system.log` para ver se o scraper encontrou vagas reais (procure por "Encontradas X vagas reais").
2. Acesse `jobs.db` ou `jobs.csv` para ver se novos registros foram gravados.
3. Muitos sites retornam vagas “presenciais”, e por padrão o sistema filtra apenas remoto/híbrido.
   - Para incluir vagas presenciais APENAS em sua cidade (ex: Garanhuns), rode:
     ```
     set ALLOW_PRESENCIAL=1
     set PRESENCIAL_CIDADES=garanhuns
     python main.py
     ```
   - Caso queira permitir presencial em qualquer cidade (não recomendado), use:
     ```
     set ALLOW_PRESENCIAL=1
     set PRESENCIAL_CIDADES=
     python main.py
     ```
4. Se quiser verificar o scraper SEM NENHUM FILTRO (todas as vagas capturadas):
   ```
   set DEBUG_KEEP_ALL=1
   python main.py
   ```
5. Os sites podem ter mudado estrutura HTML (o scraper precisa ser adaptado).
6. Aguarde alguns minutos e tente novamente.

## 📈 Próximas Melhorias

- Melhorar scrapers para capturar descrição completa
- Implementar Vagas.com e Gupy
- Dashboard web para visualizar vagas
- Filtros avançados por salário, tecnologia, etc

## 📞 Suporte

Verifique `logs/system.log` para detalhes de qualquer erro.
