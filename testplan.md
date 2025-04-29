# План тестирования сайта

## Элементы страницы

### Навигация
- Логотип: `LC` (левый верхний угол)
- Ссылка "Продукция": верхнее меню
- Ссылка "Корзина": верхнее меню

### Товары
1. Розетка
   - Изображение розетки
   - Название: "Розетка"
   - Цена: "1000 ₽"
   - Кнопка "В корзину"

2. Выключатель
   - Изображение выключателя
   - Название: "Выключатель"
   - Цена: "2000 ₽"
   - Кнопка "В корзину"

### Футер
- Текст копирайта: "© 2024 О нас"

## Селекторы для автоматизации

```javascript
// Селекторы навигации
const logo = document.querySelector('.logo'); // Логотип LC
const productsLink = document.querySelector('a:contains("Продукция")');
const cartLink = document.querySelector('a:contains("Корзина")');

// Селекторы товаров
// Розетка
const socketItem = {
  container: document.querySelector('.socket-container'),
  image: document.querySelector('.socket-image'),
  name: document.querySelector('.socket-name'),
  price: document.querySelector('.socket-price'),
  addToCartButton: document.querySelector('.socket-add-button')
};

// Выключатель
const switchItem = {
  container: document.querySelector('.switch-container'),
  image: document.querySelector('.switch-image'),
  name: document.querySelector('.switch-name'),
  price: document.querySelector('.switch-price'),
  addToCartButton: document.querySelector('.switch-add-button')
};

// Селектор футера
const footer = document.querySelector('footer');
```

## Тест-кейсы для проверки

1. Проверка навигации
   - Проверить видимость логотипа
   - Проверить наличие и работу ссылок "Продукция" и "Корзина"

2. Проверка отображения товаров
   - Проверить корректность отображения названий товаров
   - Проверить корректность отображения цен товаров
   - Проверить наличие и видимость кнопок "В корзину"

3. Проверка функциональности корзины
   - Проверить добавление товара в корзину при нажатии на кнопку "В корзину"
   - Проверить отображение товара в корзине после добавления

4. Проверка отображения футера
   - Проверить наличие и корректность текста в футере
