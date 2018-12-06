def embedsayadmin(self, ctx, *, text: str):
        """Says Something as the bot without any trace of the message author in a embed"""

        if ctx.message.server.me.bot:
            try:
                await self.bot.delete_message(ctx.message)
            except:
                await self.bot.send_message(ctx.message.author, 'Could not delete your message on ' + ctx.message.server.name)

        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)

        randnum = randint(1, 10)
        empty = u"\u2063"
        emptyrand = empty * randnum

        data = discord.Embed(description=str(
            text), colour=discord.Colour(value=colour))

        try:
            await self.bot.say(emptyrand, embed=data)
        except:
            await self.bot.say("I need the `Embed links` permission "
                               "to send this") 
