# 📊 Formas de Monitorar o "TI Internship Finder"

**Pergunta: Como saber se o programa está rodando?**

Resposta: Existem **3 formas** de acompanhar e você pode usar todas!

---

## 1. 🖥️ Monitor Terminal com Cores (Recomendado para Terminal)

**Arquivo**: `monitor.bat`

```
Double-click em: monitor.bat
```

### O que você vê:

✅ **Estatísticas em Tempo Real:**
- Total de vagas no banco
- Tamanho do arquivo CSV
- Hora atual

✅ **Últimos 15 Logs:**
- ✓ (verde) = Sucesso
- ✗ (vermelho) = Erro
- ⚠ (amarelo) = Aviso

✅ **Menu Interativo:**
- `R` - Rodar busca manual agora
- `S` - Iniciar agendador
- `A` - Abrir API
- `L` - Limpar logs
- `C` - Editar configurações
- `Q` - Sair

✅ **Auto-atualiza automaticamente!**

**Exemplo de Output:**
```
============================================================
   TI Internship Finder - Monitor de Status
============================================================

📊 ESTATÍSTICAS ATUAIS:
  • Total de vagas no banco: 42
  • Tamanho do CSV: 5240 bytes
  • Banco de dados: jobs.db
  • Arquivo CSV: jobs.csv

📋 ÚLTIMOS LOGS (últimas 15 linhas):
──────────────────────────────────────────────────────────
✓ 2026-03-13 14:23:02 - INFO - Iniciando busca de vagas
✓ 2026-03-13 14:23:05 - INFO - Encontradas 15 vagas reais
✓ 2026-03-13 14:23:06 - INFO - Jobs após filtragem: 8
✗ 2026-03-13 14:23:07 - ERROR - Erro ao enviar Telegram
──────────────────────────────────────────────────────────
```

---

## 2. 🌐 Dashboard Web (Recomendado para Navegador)

**Arquivo**: `api_start.bat`

```
Double-click em: api_start.bat
Acesse: http://127.0.0.1:8000
```

### O que você vê:

✅ **Interface Moderna:**
- Cores atraentes (roxo/azul)
- Layout responsivo
- 100% funcional

✅ **Informações Ao Vivo:**
- Total de vagas encontradas
- Última atualização
- Hora exata da sincronia

✅ **Lista de Vagas:**
- Título completo
- Empresa 🏢
- Localização 📍
- Tipo (remoto/híbrido) 💼
- Data 📅
- Link direto para aplicar

✅ **Auto-atualiza a cada 5 segundos**

**Passos:**
1. Double-click em `api_start.bat`
2. Aguarde "Uvicorn running on http://127.0.0.1:8000"
3. Abra no navegador: http://127.0.0.1:8000
4. Veja as vagas em tempo real!

---

## 3. 📝 Arquivo de Logs (Detalhado)

**Arquivo**: `logs/system.log`

```
Abra diretamente: logs/system.log
Ou com: Notepad++, VSCode, etc
```

### O que você vê:

✅ **Histórico Completo:**
```
2026-03-13 14:23:02,599 - INFO - Iniciando busca de vagas
2026-03-13 14:23:05,291 - INFO - Encontradas 15 vagas reais
2026-03-13 14:23:06,001 - INFO - Jobs após filtragem: 8
2026-03-13 14:23:06,002 - INFO - Jobs após deduplicação: 8
2026-03-13 14:23:06,235 - INFO - Novas jobs salvas: 2
2026-03-13 14:23:07,500 - ERROR - Erro ao enviar Telegram
2026-03-13 14:23:08,120 - INFO - Busca concluída com sucesso
```

✅ **Três Níveis de Detalhes:**
- `INFO` - Informações normais
- `ERROR` - Erros encontrados
- `WARNING` - Avisos

---

## 🚀 Resumo: Como Usar

### Para Saber Se Está Rodando:

**Opção 1: Terminal com Cores** (em tempo real)
```bash
monitor.bat
```

**Opção 2: Dashboard Web** (visual bonito)
```bash
api_start.bat
# Depois acesso http://127.0.0.1:8000
```

**Opção 3: Logs Detalhados** (histórico)
```
Abra: logs/system.log
```

### Para Rodar o Programa:

**Uma única vez:**
```bash
executar.bat
```

**Todos os dias às 9h:**
```bash
agendador.bat
```

---

## 📱 Você Também Receberá:

| Canal | O Que Você Recebe |
|-------|-------------------|
| **Telegram** 📲 | Notificação de cada vaga nova |
| **Email** 📧 | Resumo diário às 9:00 em bruno.gfv@gmail.com |
| **CSV** 📊 | Arquivo jobs.csv com todas as vagas |
| **Banco** 🗄️ | jobs.db com histórico completo |

---

## ⚡ Quick Start

1. **Abrir Monitor:**
   ```
   Double-click em: monitor.bat
   ```

2. **Em outro terminal, rodar busca:**
   ```
   Double-click em: executar.bat
   ```

3. **Ver no navegador:**
   ```
   Double-click em: api_start.bat
   # Acesse http://127.0.0.1:8000
   ```

4. **Ver notificações:**
   - Verifique seu Telegram
   - Verifique seu email

---

## 🎯 Fluxo Recomendado

```
┌─────────────────────────────────────┐
│ PRIMEIRO: Monitor Terminal          │
│ (monitor.bat - vê tudo em cores)    │
└─────────────┬───────────────────────┘
              │
┌─────────────▼───────────────────────┐
│ SEGUNDO: Rodar Busca                │
│ (executar.bat - uma vez)            │
└─────────────┬───────────────────────┘
              │
┌─────────────▼───────────────────────┐
│ TERCEIRO: Ver no Dashboard Web      │
│ (api_start.bat - http://127.0...)   │
└─────────────────────────────────────┘
```

---

## ✅ Checklist de Monitoramento

- [ ] Abri o `monitor.bat` para ver em cores?
- [ ] Rodei `executar.bat` para buscar vagas?
- [ ] Abri `api_start.bat` para ver interface web?
- [ ] Verifiquei se Telegram recebeu notificação?
- [ ] Verifiquei o email bruno.gfv@gmail.com?
- [ ] Consultei `logs/system.log` para detalhes?
- [ ] Agendei o programa com `agendador.bat` para rodar diariamente?

---

**Dúvidas? Confira `logs/system.log` para erros detalhados!** 🚀
