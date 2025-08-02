# 🤖 Asarado DBot

Mascote digital oficial do estúdio **ASAR Lab**.  
Gerencia versões, registra entregas, gera changelogs e interage com projetos diretamente via **Discord**.

---

## 🚀 Funcionalidades

O Asarado Bot reconhece comandos enviados em canais de projeto e realiza ações automáticas com base em tags:

### Comandos disponíveis

- `!MAJOR`  
  Incrementa versão principal (ex: `v1.0.0` → `v2.0.0`)

- `!MINOR`  
  Incrementa versão secundária (ex: `v1.2.0` → `v1.3.0`)

- `!PATCH`  
  Incrementa correção (ex: `v1.2.3` → `v1.2.4`)

- `!VERSION`  
  Exibe a versão atual do projeto

- `!TASKS`  
  Lista todas as entregas registradas

- `!LOG`  
  Gera changelog formatado com histórico de versões e descrições

> Basta iniciar a mensagem com uma dessas tags e o bot cuida do resto.  
> Exemplo:
>
> ```
> !MINOR  
> Adicionada tela de configurações com suporte a múltiplos perfis.
> ```

---

## 🧠 Tecnologias Utilizadas

- 🐍 Python  
- 💬 Discord API  
- 🔥 Firebase Firestore  
- 🧩 Modularização com `parser.py`, `listener.py`, `manager.py`

---

## 📅 Roadmap de Atualizações

### ✅ Funcionalidades já implementadas

- Registro automático de entregas com versão
- Consulta de versão atual (`!VERSION`)
- Listagem de entregas (`!TASKS`)
- Geração de changelog (`!LOG`)

### 🛠 Em desenvolvimento

- Suporte a embeds para changelog
- Exportação de changelog em Markdown ou PDF
- Integração com GitHub para commits e issues

### 💡 Sugestões futuras

- Reações automáticas para aprovar entregas
- Sistema de aprovação por emojis
- Dashboard web com estatísticas de entregas

---

## 👨‍💻 Autor

**Rafael Elyah** — [ASAR Lab]