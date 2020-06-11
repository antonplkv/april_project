from models import Text


def init_texts():
    Text.objects.create(
        title=Text.TITLES['greetings'],
        body='Рады приветсвовать Вас в нашем интернет магазине'
    )
    Text.objects.create(
        title=Text.TITLES['cart'],
        body='Вы перешли в корзину'
    )


if __name__ == '__main__':
    init_texts()
