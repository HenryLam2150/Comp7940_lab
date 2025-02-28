import configparser
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Define the echo function
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_message = update.message.text.upper()
    logging.info("Update: " + str(update))
    logging.info("Context: " + str(context))
    await context.bot.send_message(chat_id=update.effective_chat.id, text=reply_message)

# Main function
def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    # Read the configuration
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Initialize the application
    application = ApplicationBuilder().token(config['TELEGRAM']['ACCESS_TOKEN']).build()

    # Create the echo handler
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    
    # Add the handler to the application
    application.add_handler(echo_handler)

    # Start polling
    application.run_polling()

# Entry point
if __name__ == '__main__':
    main()