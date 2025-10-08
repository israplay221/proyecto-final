import discord
import pyttsx3
import os
from discord.ext import commands
engine = pyttsx3.init() # object creation


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Inicializar el bot
intents = discord.Intents.default()
intents.message_content = True  # Para leer mensajes
bot = commands.Bot(command_prefix="!", intents=intents)

# RATE
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        # printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate
volume = engine.getProperty('volume')   # getting to know current volume level (min=0 and max=1)
print (volume)                          # printing current volume level
engine.setProperty('volume',1.0)        # setting up volume level  between 0 and 1
voices = engine.getProperty('voices')       # getting details of current voice
#engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   # changing index, changes voices. 1 for female

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')


@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)


import discord
from discord.ext import commands
import os

@bot.command()
async def calentamiento_global(ctx):

    await ctx.send(f"Hola, soy un bot {bot.user}! 🤖")
    await ctx.send("¿Quieres saber qué es el calentamiento global? (responde con 'si' o 'no')")

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() in ['si', 'no']

    response = await bot.wait_for('message', check=check)

    if response.content.lower() == 'si':
        await ctx.send("El calentamiento global es el incremento de la temperatura de la atmósfera terrestre asociado, en parte, a la emisión de gases de efecto invernadero.")
    else:
        await ctx.send("Está bien 😊. Si quieres saber del tema más tarde, usa el mismo comando.")
        return

    await ctx.send("¿Quieres saber más sobre el cambio climático? (si/no)")
    response1 = await bot.wait_for('message', check=check)

    if response1.content.lower() == 'si':
        await ctx.send("El cambio climático se refiere a cambios a largo plazo de las temperaturas y los patrones climáticos.")
        await ctx.send("Actualmente, estos cambios están muy influenciados por la acción humana.")
        await ctx.send("Puedes preguntar lo siguiente:")
        await ctx.send("- ¿Es grave este problema? ¿Nos concierne?")
        await ctx.send("- ¿Qué desencadena el cambio climático?")
        await ctx.send("- ¿Cómo podemos frenar el cambio climático?")
        await ctx.send("- fuentes")
        await ctx.send("- ejemplo")

        # ---- Pregunta 1
        def check2(message):
            return message.author == ctx.author and message.channel == ctx.channel and "grave" in message.content.lower()

        response2 = await bot.wait_for('message', check=check2)
        await ctx.send("Sí, es un problema muy grave y nos concierne directamente.")
        await ctx.send("Los impactos ya son visibles: derretimiento de glaciares, aumento del nivel del mar, incendios, sequías, tormentas más intensas.")
        await ctx.send("Si no se actúa con decisión, la temperatura podría aumentar más de 3 °C para fin de siglo.")

        # ---- Pregunta 2
        def check3(message):
            return message.author == ctx.author and message.channel == ctx.channel and "desencadena" in message.content.lower()

        response3 = await bot.wait_for('message', check=check3)
        await ctx.send("Las causas pueden ser naturales o humanas.")
        await ctx.send("Naturales: actividad volcánica, radiación solar y cambios orbitales de la Tierra.")
        await ctx.send("Humanas: quema de combustibles fósiles, deforestación y procesos industriales que liberan CO₂.")

        # ---- Pregunta 3
        def check4(message):
            return message.author == ctx.author and message.channel == ctx.channel and "frenar" in message.content.lower()

        response4 = await bot.wait_for('message', check=check4)
        await ctx.send("Podemos frenarlo reduciendo emisiones y adaptándonos al cambio.")
        await ctx.send("🔹 Energías renovables (solar, eólica, hidroeléctrica)")
        await ctx.send("🔹 Reforestación y conservación de bosques")
        await ctx.send("🔹 Uso eficiente de la energía y transporte limpio")
        await ctx.send("🔹 Educación y cooperación global")

        # ---- Fuentes
        def check5(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() in ['fuentes', 'bibliografia']

        response5 = await bot.wait_for('message', check=check5)
        await ctx.send("🌍 **Fuentes:**")
        await ctx.send("- https://www.un.org/es/un75/climate-crisis-race-we-can-win")
        await ctx.send("- https://www.un.org/es/climatechange/science/causes-effects-climate-change")
        await ctx.send("- https://www.manosunidas.org/observatorio/cambio-climatico/calentamiento-global")

        # ---- Ejemplo con imagen
        def check6(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() in ['ejemplo', 'foto']

        response6 = await bot.wait_for('message', check=check6)

        image_path = 'CC.jpg'
        if os.path.exists(image_path):
            with open(image_path, 'rb') as f:
                picture = discord.File(f)
                await ctx.send("Aquí tienes un ejemplo de Calentamiento Global:", file=picture)
        else:
            await ctx.send("No pude encontrar la imagen. Verifica que la ruta sea correcta.")

    else:
        await ctx.send("Está bien 😊. Si quieres saber más, usa este mismo comando luego.")


@bot.command()
async def test(ctx):
    await ctx.send(f"Hola, soy un bot {bot.user} 🤖")
    engine.say(f"Hola, soy un bot {bot.user} 🤖")

    await ctx.send("¿Quieres que te haga unas preguntas del calentamiento global? (responde con 'si' o 'no')")

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() in ['si', 'no']

    # Espera respuesta
    response = await bot.wait_for('message', check=check)

    if response.content.lower() == 'si':
        # Primera pregunta
        await ctx.send("¿El cambio climático es considerado un problema grave para la humanidad? (sí/no)")
        respuesta1 = await bot.wait_for('message', check=check)

        if respuesta1.content.lower() == 'si':
            await ctx.send("✅ Correcto, es un problema grave que afecta a todos los países.")
        else:
            await ctx.send("❌ Incorrecto, sí es un problema muy serio.")

        # Segunda pregunta
        await ctx.send("¿El cambio climático afecta únicamente a los países pobres y no al resto del mundo? (sí/no)")
        respuesta2 = await bot.wait_for('message', check=check)

        if respuesta2.content.lower() == 'no':
            await ctx.send("✅ Correcto, el cambio climático afecta a todo el planeta.")
        else:
            await ctx.send("❌ Incorrecto, no solo afecta a los países pobres.")

        # Puedes seguir con las de Verdadero/Falso si quieres
        await ctx.send("¿Quieres seguir con las preguntas de Verdadero o Falso? (sí/no)")
        seguir = await bot.wait_for('message', check=check)

        if seguir.content.lower() == 'si':
            await ctx.send("La quema de combustibles fósiles es una de las principales causas del cambio climático. (verdadero/falso)")

            def check_vf(message):
                return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() in ['verdadero', 'falso']

            respuesta3 = await bot.wait_for('message', check=check_vf)

            if respuesta3.content.lower() == 'verdadero':
                await ctx.send("✅ Correcto.")
            else:
                await ctx.send("❌ Incorrecto, sí lo es.")

    else:
        await ctx.send("Está bien, cuando quieras podemos hacer el test 🌍")




bot.run("Token")
