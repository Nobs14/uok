import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.network.urlrequest import UrlRequest
from kivy.graphics import Color, RoundedRectangle
import json
import threading
import time
import socket

kivy.require('1.11.1')

class MessageBubble(Label):
    pass

class UOKChatApp(App):
    def build(self):
        self.title = 'UOK FAQ Bot'
        # Set window size to simulate mobile device
        Window.size = (400, 700)
        from kivy.lang import Builder
        Builder.load_file('uok_chat.kv')
        return ChatInterface()

    def on_start(self):
        # Send welcome message after app starts
        Clock.schedule_once(self.send_welcome_message, 0.5)

    def send_welcome_message(self, dt):
        welcome_text = "Hello! Welcome to University of Kabianga (UOK) Assistant. How can I help you today? Ask about admissions, fees, or student portal."
        self.root.add_bot_message(welcome_text)

class ChatInterface(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setup_ui()
        
    def setup_ui(self):
        # Main layout
        self.main_layout = BoxLayout(orientation='vertical')
        
        # Header
        self.header = BoxLayout(size_hint_y=None, height=60)
        # Placeholder for UOK logo
        with self.header.canvas.before:
            Color(0, 0.39, 0, 1)  # Deep green background
            RoundedRectangle(pos=self.header.pos, size=self.header.size, radius=[0, 0, 20, 20])
        
        logo_placeholder = Widget(size_hint_x=None, width=50)
        with logo_placeholder.canvas.before:
            Color(1, 0.84, 0, 1)  # Gold color
            Ellipse(pos=logo_placeholder.pos, size=(30, 30))
        
        header_label = Label(
            text='UOK Assistant',
            color=(1, 1, 1, 1),
            font_size=20,
            bold=True
        )
        
        self.header.add_widget(logo_placeholder)
        self.header.add_widget(header_label)
        
        # Chat history container
        self.chat_history_container = ScrollView()
        self.chat_history = GridLayout(cols=1, spacing=10, size_hint_y=None, padding=10)
        self.chat_history.bind(minimum_height=self.chat_history.setter('height'))
        self.chat_history_container.add_widget(self.chat_history)
        
        # Input area
        self.input_area = BoxLayout(size_hint_y=None, height=60, padding=5)
        self.message_input = TextInput(
            multiline=False,
            hint_text='Ask about UOK...',
            size_hint_x=0.8,
            padding=[10, 10],
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1)
        )
        self.send_button = Button(
            text='Send',
            size_hint_x=0.2,
            background_color=(0, 0.39, 0, 1),  # Deep green
            color=(1, 0.84, 0, 1)  # Gold text
        )
        
        # Bind events
        self.message_input.bind(on_text_validate=self.send_message)
        self.send_button.bind(on_press=self.send_message)
        
        # Add widgets to layouts
        self.input_area.add_widget(self.message_input)
        self.input_area.add_widget(self.send_button)
        self.main_layout.add_widget(self.header)
        self.main_layout.add_widget(self.chat_history_container)
        self.main_layout.add_widget(self.input_area)
        
        self.add_widget(self.main_layout)
        
        # Store references for external access
        self.ids = {'chat_history': self.chat_history}
    
    def add_user_message(self, text):
        bubble = MessageBubble(
            text=text,
            size_hint_y=None,
            halign='right',
            valign='middle',
            text_size=(Window.width * 0.7, None)
        )
        self.chat_history.add_widget(bubble)
        self.scroll_to_bottom()
    
    def add_bot_message(self, text):
        bubble = MessageBubble(
            text=text,
            size_hint_y=None,
            halign='left',
            valign='middle',
            text_size=(Window.width * 0.7, None)
        )
        self.chat_history.add_widget(bubble)
        self.scroll_to_bottom()
    
    def scroll_to_bottom(self):
        # Scroll to bottom after a small delay to ensure widget is rendered
        Clock.schedule_once(lambda dt: self.chat_history_container.scroll_to(self.chat_history.children[0] if self.chat_history.children else (0,0)), 0.1)
    
    def send_message(self, instance):
        text = self.message_input.text.strip()
        if text:
            # Add user message
            self.add_user_message(text)
            
            # Clear input
            self.message_input.text = ''
            
            # Process the message and get bot response
            self.process_user_message(text)
    
    def process_user_message(self, user_message):
        # Check internet connectivity
        if self.is_connected():
            # Show thinking indicator
            thinking_indicator = MessageBubble(
                text='Thinking...',
                size_hint_y=None,
                halign='left',
                valign='middle',
                opacity=0.7
            )
            self.chat_history.add_widget(thinking_indicator)
            self.scroll_to_bottom()
            
            # Make API request to Google Gemini
            self.request_gemini_response(user_message, thinking_indicator)
        else:
            # Fallback to local FAQ
            response = self.get_local_faq_response(user_message.lower())
            self.add_bot_message(response)
    
    def is_connected(self):
        try:
            # Connect to a reliable host to check internet connection
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            return True
        except OSError:
            return False
    
    def request_gemini_response(self, user_message, thinking_indicator):
        # Prepare the API request to Google Gemini
        api_key = "AIzaSyDAdjKNImo5y989ECivXu75R-6xhL-phng"  # Your Gemini API key
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
        
        headers = {
            'Content-Type': 'application/json'
        }
        
        data = {
            "contents": [{
                "parts": [{
                    "text": f"You are a helpful assistant for University of Kabianga (UOK) students. Answer the following question about UOK: {user_message}. Keep your response concise and informative."
                }]
            }]
        }
        
        # Make the API request asynchronously
        req = UrlRequest(
            url,
            on_success=lambda req, result: self.on_gemini_success(result, thinking_indicator),
            on_failure=lambda req, result: self.on_gemini_failure(req, result, thinking_indicator),
            on_error=lambda req, error: self.on_gemini_error(req, error, thinking_indicator),
            req_body=json.dumps(data),
            req_headers=headers,
            timeout=30
        )
    
    def on_gemini_success(self, result, thinking_indicator):
        # Remove thinking indicator
        Clock.schedule_once(lambda dt: self.chat_history.remove_widget(thinking_indicator), 0)
        
        try:
            # Extract the response from Gemini API
            text_response = result['candidates'][0]['content']['parts'][0]['text']
            Clock.schedule_once(lambda dt: self.add_bot_message(text_response), 0.1)
        except (KeyError, IndexError):
            # Fallback if API response format is unexpected
            fallback_response = "I received a response from the AI, but couldn't process it properly. Is there anything else I can help you with?"
            Clock.schedule_once(lambda dt: self.add_bot_message(fallback_response), 0.1)
    
    def on_gemini_failure(self, req, result, thinking_indicator):
        # Remove thinking indicator
        Clock.schedule_once(lambda dt: self.chat_history.remove_widget(thinking_indicator), 0)
        
        # Fallback to local FAQ
        Clock.schedule_once(lambda dt: self.add_bot_message("API request failed. Using local FAQ..."), 0.1)
        # Schedule the local FAQ response after the failure message
        Clock.schedule_once(lambda dt: self.add_bot_message(self.get_local_faq_response("")), 1.0)
    
    def on_gemini_error(self, req, error, thinking_indicator):
        # Remove thinking indicator
        Clock.schedule_once(lambda dt: self.chat_history.remove_widget(thinking_indicator), 0)
        
        # Fallback to local FAQ
        Clock.schedule_once(lambda dt: self.add_bot_message("Connection error. Using local FAQ..."), 0.1)
        # Schedule the local FAQ response after the error message
        Clock.schedule_once(lambda dt: self.add_bot_message(self.get_local_faq_response("")), 1.0)
    
    def get_local_faq_response(self, user_message):
        """Handle common UOK FAQs as fallback when API is unavailable"""
        user_message = user_message.lower()
        
        # Admission related queries
        if any(word in user_message for word in ['admission', 'admissions', 'apply', 'application', 'register']):
            if any(word in user_message for word in ['date', 'deadline', 'when']):
                return "Admission deadlines vary by program. For undergraduate programs, applications typically close in October for the following academic year. Visit the admissions office website for exact dates."
            elif any(word in user_message for word in ['process', 'how', 'steps']):
                return "To apply for admission: 1) Visit the UOK admissions portal, 2) Fill out the online application form, 3) Upload required documents, 4) Pay application fee, 5) Wait for admission letter."
            else:
                return "For admission inquiries: Application deadlines, required documents, and procedures vary by program. Would you like specific information about undergraduate or postgraduate admissions?"
        
        # Fee related queries
        elif any(word in user_message for word in ['fee', 'fees', 'tuition', 'cost', 'money', 'pay']):
            if any(word in user_message for word in ['amount', 'how much', 'cost']):
                return "Tuition fees vary by program. Undergraduate programs typically cost between KES 40,000-80,000 per semester depending on the faculty. Postgraduate fees are higher. Check the finance office for current rates."
            elif any(word in user_message for word in ['payment', 'pay', 'method']):
                return "Fees can be paid through bank deposit to UOK accounts, online banking, or mobile money (M-Pesa). Payment receipts should be submitted to the finance office."
            else:
                return "Fee structures differ by program. Undergraduate fees are approximately KES 40,000-80,000 per semester. For specific fee information, visit the finance office or check your program requirements."
        
        # Student portal related queries
        elif any(word in user_message for word in ['portal', 'student', 'login', 'account', 'profile']):
            return "The UOK student portal is available at https://student.uok.ac.ke. Here you can access course materials, check grades, register for courses, and manage your student profile. Access credentials are given during registration."
        
        # General university info
        elif any(word in user_message for word in ['university', 'uok', 'campus', 'about']):
            return "University of Kabianga (UOK) is a public university established in 2016. Located in Kabianga town, Kericho County, it offers various undergraduate and postgraduate programs across multiple faculties."
        
        # Default response
        else:
            return "I'm here to help with University of Kabianga (UOK) FAQs. You can ask about: \n• Admissions and applications\n• Fee structures and payment\n• Student portal and accounts\n• General university information\n\nTry asking about specific topics like 'admission dates' or 'fee payment methods'"

if __name__ == '__main__':
    UOKChatApp().run()