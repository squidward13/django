from django.shortcuts import render
from django.http import HttpResponse
import logging

# Create your views here.

logger = logging.getLogger(__name__)

def index(request):
	body = """
    <title>Главная страница</title>
    <body>
        <div>
            <h1>Главная страница</h1>
            <p>Содержимое главной страницы</p>
            <p>Перейдите на страницу: /about/</p>
        </div>
        <footer>
            <div>
                <p>Copyright &copy;
                    <script type="text/javascript"> document.write(new Date().getFullYear());</script>
                    Communications Inc. Все права защищены.
                </p>
            </div>
        </footer>
    </body>
    """
	logger.info('User visited main page!')
	return HttpResponse(body, charset='utf-8')

def about(request):
	body = """
        <title>О себе</title>  
        <body>     
            <div>
                <h1>Иванов Иван Иванович</h1>
                <p>Мужчина, 27 лет, родился 12 марта 1998 года.</p>
            </div>
            <footer>
                <div>
                    <p>Copyright &copy;
                        <script type="text/javascript"> document.write(new Date().getFullYear());</script>
                        Communications Inc. Все права защищены.
                    </p>
                </div>
            </footer>
        </body>
        """
	logger.info('User visited about page!')
	return HttpResponse(body, charset='utf-8')