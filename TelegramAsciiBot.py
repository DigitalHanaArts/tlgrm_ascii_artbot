import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import pyfiglet


# List of sample words for ASCII Art
topics = ["Hello", "Python", "Bot", "ASCII", "Art", "Fun", "Creative", "Code", "ASCII Art", "Digital", "Hana", "Arts", "DIGITAL__HANA__ARTS", "Digital--Hana--Arts", "digital..hana..arts", "NFTs", "NFT_ARTS"]
# Function to generate ASCII art
def generate_ascii_word():
    word = random.choice(topics)
    return word

def generate_ascii_art():
    try:
        # Get all available fonts and select a random one
        fonts = pyfiglet.FigletFont.getFonts()
        font = random.choice(fonts)
        fig = pyfiglet.Figlet(font=font)
    except Exception as e:
        # Fallback to default font if there's an error
        fig = pyfiglet.Figlet()
    
    # Generate ASCII art for a specific text
    ascii_art = fig.renderText(generate_ascii_word())
    return ascii_art

async def start_ascii(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    job_name = str(chat_id)
    
    # Remove existing jobs for this chat
    current_jobs = context.job_queue.get_jobs_by_name(job_name)
    for job in current_jobs:
        job.schedule_removal()
    
    # Add new job to the queue
    context.job_queue.run_repeating(
        send_ascii_art,
        interval=10,  # χ minutes in seconds
        first=0,       # Send immediately
        name=job_name,
        data={'chat_id': chat_id}
    )
    
    await update.message.reply_text("🚀 Started! You'll receive ASCII art every minute. Use /stop_ascii to cancel.")

async def stop_ascii(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    job_name = str(chat_id)
    
    # Remove existing jobs for this chat
    current_jobs = context.job_queue.get_jobs_by_name(job_name)
    for job in current_jobs:
        job.schedule_removal()
    
    await update.message.reply_text("❌ Stopped sending ASCII art. Use /start_ascii to begin again.")

async def send_ascii_art(context: ContextTypes.DEFAULT_TYPE):
    job = context.job
    ascii_art = generate_ascii_art()
    
    # Send message with HTML-formatted monospace text
    await context.bot.send_message(
        chat_id=job.data['chat_id'],
        text=f'<pre>{ascii_art}</pre>',
        parse_mode='HTML'
    )

def main():
    # Initialize the application with your bot token
    application = Application.builder().token("7922504568:AAEwRbotFyAdGaePnXCirhzlGfjnf4iprS4").build()
    
    # Add command handlers
    application.add_handler(CommandHandler("start_ascii", start_ascii))
    application.add_handler(CommandHandler("stop_ascii", stop_ascii))
    
    # Start polling for updates
    application.run_polling()

if __name__ == "__main__":
    main()