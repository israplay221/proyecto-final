import discord
from discord.ext import commands
import os
import pyttsx3

engine = pyttsx3.init()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'✅ Bot conectado como {bot.user}')


@bot.command()
async def hello(ctx):
    await ctx.send(f'¡Hola! Soy {bot.user}!')


@bot.command()
async def calentamiento_global(ctx):
    await ctx.send(f"Hola, soy un bot {bot.user}! 🤖")
    await ctx.send("¿Quieres saber qué es el calentamiento global? (responde con 'si' o 'no')")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ['si', 'no']

    response = await bot.wait_for('message', check=check)

    if response.content.lower() == 'no':
        await ctx.send("Está bien 😊. Si quieres saber del tema más tarde, usa el mismo comando.")
        return

    await ctx.send("El calentamiento global es el incremento de la temperatura de la atmósfera terrestre asociado, en parte, a la emisión de gases de efecto invernadero.")
    await ctx.send("¿Quieres saber más sobre el cambio climático? (si/no)")

    response = await bot.wait_for('message', check=check)

    if response.content.lower() == 'no':
        await ctx.send("Está bien 😊. Si quieres saber más, usa este mismo comando luego.")
        return

    await ctx.send("El cambio climático se refiere a cambios a largo plazo de las temperaturas y los patrones climáticos.")
    await ctx.send("Actualmente, estos cambios están muy influenciados por la acción humana.")
    await ctx.send("Puedes preguntar lo siguiente: \n- grave\n- desencadena\n- frenar\n- fuentes\n- ejemplo")

    while True:
        def check_any(m):
            return m.author == ctx.author and m.channel == ctx.channel

        msg = await bot.wait_for('message', check=check_any)
        content = msg.content.lower()

        if "grave" in content:
            await ctx.send("Sí, es un problema muy grave y nos concierne directamente.")
            await ctx.send("Impactos: derretimiento de glaciares, aumento del nivel del mar, incendios, sequías, tormentas más intensas.")
        elif "desencadena" in content:
            await ctx.send("Causas naturales: volcanes, radiación solar, cambios orbitales.")
            await ctx.send("Causas humanas: quema de combustibles fósiles, deforestación, procesos industriales.")
        elif "frenar" in content:
            await ctx.send("Podemos frenarlo reduciendo emisiones y adaptándonos al cambio 🌍")
            await ctx.send("- Energías renovables")
            await ctx.send("- Reforestación")
            await ctx.send("- Transporte limpio")
            await ctx.send("- Educación ambiental")
        elif content in ['fuentes', 'bibliografia']:
            await ctx.send("🌍 **Fuentes:**")
            await ctx.send("- https://www.un.org/es/un75/climate-crisis-race-we-can-win")
            await ctx.send("- https://www.un.org/es/climatechange/science/causes-effects-climate-change")
            await ctx.send("- https://www.manosunidas.org/observatorio/cambio-climatico/calentamiento-global")
        elif content in ['ejemplo', 'foto']:
            image_path = 'CC.jpg'
            if os.path.exists(image_path):
                with open(image_path, 'rb') as f:
                    picture = discord.File(f)
                    await ctx.send("Aquí tienes un ejemplo de Calentamiento Global:", file=picture)
            else:
                await ctx.send("⚠️ No pude encontrar la imagen. Verifica la ruta.")
        elif content in ['salir', 'adios']:
            await ctx.send("¡Gracias por aprender sobre el cambio climático conmigo! 🌱")
            break


@bot.command()
async def test(ctx):
    await ctx.send(f"Hola, soy un bot {bot.user} 🤖")
    engine.say("Hola, soy un bot de prueba del calentamiento global")
    engine.runAndWait()

    await ctx.send("¿Quieres que te haga unas preguntas del calentamiento global? (si/no)")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ['si', 'no']

    response = await bot.wait_for('message', check=check)

    if response.content.lower() == 'no':
        await ctx.send("Está bien 🌍 cuando quieras podemos hacer el test.")
        return

    await ctx.send("¿El cambio climático es un problema grave para la humanidad? (si/no)")
    respuesta1 = await bot.wait_for('message', check=check)

    if respuesta1.content.lower() == 'si':
        await ctx.send("✅ Correcto.")
    else:
        await ctx.send("❌ Incorrecto, sí lo es.")

    await ctx.send("¿El cambio climático afecta solo a los países pobres? (si/no)")
    respuesta2 = await bot.wait_for('message', check=check)

    if respuesta2.content.lower() == 'no':
        await ctx.send("✅ Correcto.")
    else:
        await ctx.send("❌ Incorrecto, afecta a todo el mundo.")

    await ctx.send("¿Quieres seguir con preguntas de Verdadero/Falso? (si/no)")
    seguir = await bot.wait_for('message', check=check)

    if seguir.content.lower() == 'si':
        def check_vf(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ['verdadero', 'falso']

        await ctx.send("La quema de combustibles fósiles es una de las principales causas del cambio climático. (verdadero/falso)")
        respuesta3 = await bot.wait_for('message', check=check_vf)

        if respuesta3.content.lower() == 'verdadero':
            await ctx.send("✅ Correcto.")
        else:
            await ctx.send("❌ Incorrecto, sí lo es.")

bot.run("Token")
