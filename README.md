# İYTE WhatsApp Bot 🤖

A WhatsApp bot developed for students of İzmir Institute of Technology (İYTE). This bot allows students to access daily menu information and query bus schedules.

## 🌟 Features

### 📱 WhatsApp Integration
- Messaging via Meta WhatsApp Business API
- Interactive buttons and list messages
- User-friendly interface

### 🍽️ Menu Services
- Daily menu query (today/tomorrow)
- Menu like/dislike system
- Calorie information
- Holiday check

### 🚌 Bus Schedules
- Buses departing from İYTE to various locations
- Buses arriving at İYTE from different locations
- Weekday/Saturday/Sunday schedules
- Supported routes:
    - İYTE ↔ İzmir
    - İYTE ↔ Urla
    - İYTE ↔ Gülbahçe
    - Urla ↔ Çeşme

## 🛠️ Technologies

- **Backend:** Django 5.1.6
- **Database:** SQLite3
- **API:** Django REST Framework
- **WhatsApp:** Meta WhatsApp Business API
- **Web Scraping:** Selenium + BeautifulSoup4
- **Database ORM:** Django ORM

## 📦 Installation

### Requirements
```bash
pip install django
pip install djangorestframework
pip install selenium
pip install beautifulsoup4
pip install requests
```

### Project Setup

1. **Clone the repository:**
```bash
git clone https://github.com/subhanakbenli/iyte-wp-bot.git
cd iyte-wp-bot
```

2. **Create a virtual environment (recommended):**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt  # requirements.txt will be created
```

4. **Set environment variables:**
Copy the example environment file and configure it:
```bash
cp .env.example .env
```
Then edit `.env` file with your actual values:
```env
WHATSAPP_TOKEN=your_actual_whatsapp_token
PHONE_NUMBER_ID=your_actual_phone_number_id
SECRET_KEY=your_new_secret_key_here
DEBUG=True
```

⚠️ **GÜVENLİK UYARISI:** 
- `.env` dosyasını asla GitHub'a yüklemeyin!
- Production'da yeni bir SECRET_KEY oluşturun
- DEBUG=False yapın production ortamında

5. **Prepare the database:**
```bash
cd iyte_wp_bot
python manage.py migrate
python manage.py createsuperuser  # For admin user
```

6. **Start the server:**
```bash
python manage.py runserver
```

## 🔧 Configuration

### WhatsApp Business API Setup
1. Create a [Meta for Developers](https://developers.facebook.com/) account
2. Activate WhatsApp Business API
3. Redirect the Webhook URL to your project
4. Obtain Access Token and Phone Number ID

### Webhook Endpoint
The bot receives WhatsApp messages via the following endpoint:
```
POST /webhook/
```

## 📱 Bot Commands

### Main Menu
- **11** - What's on the menu today?
- **12** - What's on the menu tomorrow?
- **2** - Bus schedules from İYTE
- **3** - Bus schedules to İYTE
- **99** - More information

### Bus Routes
**From İYTE:**
- **21** - İYTE → Everywhere
- **22** - İYTE → İzmir
- **23** - İYTE → Urla
- **24** - İYTE → Gülbahçe
- **25** - Urla → Çeşme

**To İYTE:**
- **31** - Everywhere → İYTE
- **32** - İzmir → İYTE
- **33** - Urla → İYTE
- **34** - Gülbahçe → İYTE
- **35** - Çeşme → Urla

## 📊 Database Models

### Core App
- **Messages:** Bot commands and message texts

### Menu App
- **Menu:** Daily menu information
- **MenuItems:** Menu items (main dish, soup, salad, etc.)

### Bus App
- **Bus:** Bus numbers
- **Trip:** Trip information (departure/arrival points, times)

## 🔄 Web Scraping

The bot uses Selenium to automatically fetch menu information:
- The `get_menu.py` file fetches menu data from the web
- Daily menu updates
- Automated data processing

## 🚀 Deployment

### Heroku Deployment
1. Create a Heroku account
2. Install Heroku CLI
3. Set config vars:
     - `WHATSAPP_TOKEN`
     - `PHONE_NUMBER_ID`

### Docker (Optional)
```dockerfile
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push your branch (`git push origin feature/amazing-feature`)
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT license. See the `LICENSE` file for details.

## 👥 Team

- **Developer:** [@subhanakbenli](https://github.com/subhanakbenli)

## 📞 Contact

For questions about the project:
- Contact via GitHub Issues
- Submit a pull request

## 🔮 Upcoming Features

- [ ] Currency exchange integration
- [ ] Weather information
- [ ] Event tracking
- [ ] User preferences
- [ ] Multi-language support
- [ ] Voice message support

## ⚠️ Güvenlik Notları

### 🔒 Hassas Bilgilerin Korunması
- **Asla** `.env` dosyasını GitHub'a yüklemeyin
- **SECRET_KEY**'i güvenli tutun ve production'da değiştirin
- **WhatsApp API** tokenlarınızı paylaşmayın
- Production ortamında `DEBUG = False` yapın

### 🛡️ Production Güvenliği
```bash
# Yeni SECRET_KEY oluşturmak için:
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 📋 Güvenlik Kontrol Listesi
- [ ] `.env` dosyası `.gitignore`'da
- [ ] Production'da yeni SECRET_KEY
- [ ] DEBUG=False production'da
- [ ] ALLOWED_HOSTS doğru ayarlanmış
- [ ] WhatsApp webhook HTTPS kullanıyor
- Be aware of WhatsApp Business API limits
- Chrome WebDriver is required for Selenium

---

**📚 For more information, visit [Django Documentation](https://docs.djangoproject.com/) and [WhatsApp Business API Documentation](https://developers.facebook.com/docs/whatsapp).**
