import discord
from discord.ext import commands
from utils.parser import parse_tags
from versioning.manager import update_version
from firebase.firebase_config import db

def setup_listener(bot: commands.Bot):
    @bot.event
    async def on_message(message: discord.Message):
        print(f"📨 Mensagem recebida: {message.content}")

        if message.author.bot:
            return

        tags = parse_tags(message)
        if not tags:
            # Se não houver tags, processa comandos normalmente
            await bot.process_commands(message)
            return

        tag = tags[0]  # Só usamos uma tag por mensagem

        # Lista de tags reconhecidas
        tag_list = {"MAJOR", "MINOR", "PATCH", "VERSION", "TASKS", "LOG"}

        # Dados básicos
        user = message.author.name
        date = message.created_at
        channel_id = str(message.channel.id)
        channel_name = message.channel.name

        # Referência ao projeto
        projeto_ref = db.collection("projetos").document(channel_id)

        # VERSION: apenas informa a versão atual
        if tag == "VERSION":
            entregas = projeto_ref.collection("entregas") \
                .order_by("data", direction="DESCENDING") \
                .limit(1).stream()
            ultima = next(entregas, None)
            versao = ultima.to_dict().get("versao", "v0.0.0") if ultima else "v0.0.0"
            await message.channel.send(f"🔎 Versão atual do projeto `{channel_name}`: `{versao}`")
            return

        # TASKS: lista todas as entregas
        if tag == "TASKS":
            entregas = projeto_ref.collection("entregas").order_by("data").stream()
            entregas_listadas = []
            for entrega in entregas:
                data = entrega.to_dict().get("data", "N/A")
                autor = entrega.to_dict().get("autor", "N/A")
                versao = entrega.to_dict().get("versao", "N/A")
                entregas_listadas.append(f"📦 `{versao}` por **{autor}** em `{data}`")

            if not entregas_listadas:
                await message.channel.send(f"🔍 Nenhuma entrega registrada para `{channel_name}`.")
            else:
                await message.channel.send(f"📋 Entregas registradas no projeto `{channel_name}`:\n" + "\n".join(entregas_listadas))
            return

        # LOG: gera changelog formatado
        if tag == "LOG":
            entregas = projeto_ref.collection("entregas").order_by("data").stream()
            changelog = []
            for entrega in entregas:
                versao = entrega.to_dict().get("versao", "N/A")
                mensagem = entrega.to_dict().get("mensagem", "").splitlines()[1:]  # ignora a linha da tag
                descricao = "\n".join(mensagem).strip() or "Sem descrição."
                changelog.append(f"### {versao}\n{descricao}")

            if not changelog:
                await message.channel.send(f"📭 Nenhum changelog disponível para `{channel_name}`.")
            else:
                await message.channel.send(f"📝 Changelog do projeto `{channel_name}`:\n\n" + "\n\n".join(changelog))
            return

        # Recupera última versão
        entregas = projeto_ref.collection("entregas") \
            .order_by("data", direction="DESCENDING") \
            .limit(1).stream()
        ultima = next(entregas, None)
        versao_atual = ultima.to_dict().get("versao", "v0.0.0") if ultima else "v0.0.0"

        # Atualiza versão com base na tag
        new_version = update_version([tag], current_version=versao_atual)

        # Atualiza metadados do projeto
        projeto_ref.set({
            "canal_id": channel_id,
            "canal_nome": channel_name,
            "criado_em": date.isoformat()
        }, merge=True)

        # Registra entrega na subcoleção 'entregas'
        projeto_ref.collection("entregas").add({
            "autor": user,
            "data": date.isoformat(),
            "mensagem": message.content,
            "versao": new_version,
            "tag": tag
        })

        await message.channel.send(
            f"📦 Entrega registrada com tag `{tag}` no projeto `{channel_name}`! Nova versão: `{new_version}`"
        )

        # Só processa comandos se a tag não for uma das reconhecidas
        if tag not in tag_list:
            await bot.process_commands(message)