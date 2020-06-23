from models import Category, Product


def seed_categories():
    category_titles = ['tech', 'tech for home', 'items']
    category_description = ['here gonna be tech', '...', ',,,']

    for title, description in zip(category_titles, category_description):
        Category.objects.create(title=title, description=description)


if __name__ == '__main__':
    seed_categories()