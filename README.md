# TI Internship Finder

Sistema automatizado para buscar vagas de estágio em Tecnologia da Informação.

## Funcionalidades

- Scraping de vagas em LinkedIn, Indeed, Glassdoor, Vagas.com, Gupy
- Filtragem por estágio, TI, remoto/híbrido
- Deduplicação de vagas
- Armazenamento em SQLite
- Notificações via Telegram e email
- Scheduler diário
- API REST opcional com FastAPI

## Instalação

1. Instalar dependências: `pip install -r requirements.txt`
2. Instalar Playwright: `python -m playwright install`
3. Configurar tokens para Telegram e email no código (notifications/telegram_notifier.py e notifications/email_notifier.py)

## Uso

- Executar `python main.py` para busca manual
- Executar `python scheduler.py` para agendamento diário
- Para API: `uvicorn api:app --reload`

## Próximos Passos

1. **Configurar notificações**:
   - Edite `config.py` com seus tokens de Telegram e credenciais de email
   - Descomente as linhas de notificação em `main.py`

2. **Melhorar scrapers**:
   - Ajuste os seletores CSS/HTML nos scrapers conforme mudanças nos sites
   - Implemente `vagas_scraper.py` e `gupy_scraper.py` para Vagas.com e Gupy
   - Use Playwright para páginas dinâmicas se necessário

3. **Testar API**:
   - Execute `uvicorn api:app --reload` para testar a API REST

4. **Agendamento local**:
   - Execute `python scheduler.py` para rodar diariamente às 9:00

## ☁️ Hospedando no GitHub (sem usar seu PC)

Agora o projeto inclui um workflow GitHub Actions que executa o scraper automaticamente:
- Roda uma vez por dia às 9:00 (BRT)
- Atualiza `jobs.csv`, `jobs.db` e `logs/system.log`
- Dá push no próprio repositório com os resultados

### Passos para ativar no GitHub
1. No seu repositório GitHub, vá em **Settings → Secrets and variables → Actions**.
2. Crie os segredos:
   - `TELEGRAM_TOKEN`
   - `TELEGRAM_CHAT_ID`
   - `EMAIL_FROM`
   - `EMAIL_TO`
   - `EMAIL_PASSWORD`
3. O workflow já existe em `.github/workflows/scheduled_run.yml`.
4. Na aba **Actions**, clique em **Run workflow** para testar.

## Status Atual

- ✅ Sistema básico funcionando
- ✅ Scraping de LinkedIn, Indeed, Glassdoor (básico)
- ✅ Filtragem e deduplicação
- ✅ Armazenamento SQLite e CSV
- ✅ Logs
- ✅ Scheduler
- ✅ API REST
- ⚠️ Notificações desabilitadas (configurar tokens)
- ⚠️ Scrapers podem precisar ajustes para capturar mais dados"# find-job" 
