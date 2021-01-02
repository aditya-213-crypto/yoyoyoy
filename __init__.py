from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
import pickle
import logging
from telegram import (InlineKeyboardMarkup, InlineKeyboardButton)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler, CallbackQueryHandler)
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
from telegram import bot
import random
import smtplib