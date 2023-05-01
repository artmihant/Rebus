# Решаем арифметические ребусы с помощью python и яндекс.функций

Если вы увлекались математикой в возрасте до 12 лет, то, наверное, встречались с числовыми ребусами. 

Числовым ребусом называется корректное арифметическое выражение (обычно - равенство), часть цифр в котором заменена на буквы и звездочки. Правила просты: одинаковые буквы заменяются на одинаковые цифры, разные - на разные.

Задача - восстановить исходные цифры, получив верное равенство.

Числовые ребусы хороши для тренировки у младшеклассников навыков логического мышления и счета в столбик. Однако и взрослым дядям математикам программистам может быть интересно поискать ответ на общий вопрос - а как, всё таки, алгоритмизировать процесс решения ребуса?

## Формулировка задачи 

На вход программы подается арифметический ребус. Он представляет из себя строку и состоит из букв, цифр, знаков арифметических действий +-*, знака = и круглых скобок. 

Если ребус корректно преобразуется в арифметическое сравнение, программа должна вернуть список его решений. Например, на `"КОЗА*2 = СТАДО"` программа вернет `["8653*2 = 17306", "7693*2 = 15386"]`, что решит нашу задачу.

## Часть первая. Наивный алгоритм.

Искусство программирования учит нас: что бы решить задачу, представьте, что она уже решена. В данном случае, определим функцию, решающую ребусы:

    def solve(rebus: str) -> list[str]:
        # Решаем ребус
        return solutions

    def test_rebus_solver():
        solutions = solve("КОЗА+КОЗА = СТАДО")
        assert solutions == ["8653+8653 = 17306", "7693+7693 = 15386"]


### Предобработка ребуса   

Прежде всего, стоит упростить задачу, преобразовав текущее выражение. А именно: 

1) Уберем знак =. Для этого обернем выражение справа и слева в скобки и вычтем одно из другого.

`КОЗА*2 = СТАДО` => `(КОЗА*2)-(СТАДО)`

2) Составим множество уникальных букв в выражении. Для упрощения восприятия, я буду записывать в своем псевдокоде список в виде последовательности строк, разделенных запятыми:

 `[К,О,З,A,С,Т,Д]`

3) Разобьем выражение на токены. Токен - строка, представляющая либо арифметическое действие, либо скобку, либо строку из букв и цифр. Для упрощения восприятия, я :

`(КОЗА*2)-(СТАДО)` => `[(,КОЗА,*,2,),-,(,СТАДО,)]`

4) Уберем из списка токенов скобки. Для этого преобразуем выражение внутри него в обратную польскую запись (Reverse Polish notation, RPN): 

`[(,КОЗА,*,2,),-,(,СТАДО,)]` => `[КОЗА,2,*,СТАДО,-]`

Для преписывания выражения в RPN используем, например, алгоритм Shunting Yard.

Операции 1-4 можно назвать предобработкой исходного ребуса. Обьединим их в функцию:


    def rebus_preprocessing(rebus: str) -> list[str], set[str]:
        # 1) Убираем знак =
        # 2) Составляем список букв под замену 
        # 3) Токенезируем выражение
        # 4) Переводим выражение в RPN

        return rpn_rebus, letters

    def test_rebus_preprocessing():
        rpn_rebus, letters = rebus_preprocessing("КОЗА*2 = СТАДО")
        assert rpn_rebus == ["КОЗА","2",'*',"СТАДО",'-']
        assert letters == {'К','О','З','A','С','Т','Д'}

### Поиск решений

Первая - простая - идея состоит в том, что бы перебрать все возможные замены букв на цифры и проверить полученное после каждой замены арифметическое выражение на равенство нулю.

Напишем функцию под это:

    def naive_rebus_solver(rpn_rebus: list[str], letters: set[str]) -> list[dict[int,str]]
        # Перебираем все возможные подстановки. Возвращаем список корректных подстановок
        return substitutions 

    def test_naive_rebus_solver():
        rpn_rebus, letters = rebus_preprocessing("КОЗА*2 = СТАДО")
        substitutions = naive_rebus_solver(rpn_rebus, letters)
        assert substitutions == [
            {'К':'8','О':'6','З':'5','A':'3','С':'1','Т':'7','Д':'0'}
            {'К':'7','О':'6','З':'9','A':'3','С':'1','Т':'5','Д':'8'}
        ]

Как же мы будем делать перебор? 

Арифметические выражения, записанные с помощью RPN, замечательно удобно вычислять. Например, представим себе, что мы хотим вычислить 8653*2 - 17306 . В обратной польской записи это выражение перепишется как:

    `8653*2 - 17306` => [8653,2,*,17306,-]

Затем наш вычислитель идет по списку токенов, и по очереди кладет их в стек, пока не обнаружит операцию. Обнаружив её, он извлекает из стека два последний числа, применяет к ним операцию и снова кладет в стек. Если изначальное арифметическое выражение корректно, когда мы дойдем до конца списка, в стеке будет лежать единственное число - результат вычислений.

Остается перебрать все подстановки. На этот случай python есть удобнейший itertools.permutations:

    from itertools import permutations

    substitution = {l:'' for l in letters}

    for permutation in permutations('0123456789', len(letters)):
        for i, s in enumerate(letters):
            substitution[s] = permutation[i]
        # ... 

Подставляем, вычисляем, сравниваем с нулем каждую подстановку. Готово!

## Часть вторая. Не такой наивный алгоритм.

Поигравшись с наивным алгоритмом, представленным выше, обнаруживаем в нем один недостаток. Он медленный.

Легко видеть, что в худшем случае нам придется перебрать 10! = 3628800 подстановок. Не так уж много - но на моей машине, будучи реализован на python, этот алгоритм исполняется в худшем случае около 8 секунд.

Пути решения проблемы:

* Переписать на более быстрый язык программирования
* Распараллелить
* Попробовать оптимизировать цикл подстановки-и-подсчета

Всё это - хорошие пути решения, но можно поступить проще.

Задумаемся над тем, как эту задачу бы решал ребенок. Врят ли он стал бы механически перебирать миллионы вариантов подстановки. Покумекав слегка, умный математический школьник изобретет примерно следующее:

- Рассмотрим последнюю букву в каждом из слогаемых. 
- Переберем несколько вариантов этой буквы, затем добавим в рассмотрение предпосленюю. 
- Будем делать так, пока не решим весь ребус.

Когда матшкольнику случится подрасти и поступить в универ, он может встретить концепцию *кольца* - множества элементов, замкнутого относительно сложения, вычитания и умножения. Самые простые для понимания кольца - кольца остатков от деления. Действительно, для любого a,b,p верно:

    (a%p + b%p)%p == (a+b)%p

    (a%p - b%p)%p == (a-b)%p

    (a%p * b%p)%p == (a*b)%p

К сожалению, вообще говоря, это неверно для деления. Система чисел, замкнутая относительно операции деления, помимо первых трех, зовется у математиков *полем* - и если мы рассматривали простое p, то могли бы утверждать, что у множества остатков от деления на p есть свойства поля. В данном случае, однако, мы будем последовательно рассматривать в роли p числа 10, 100, 1000... то есть, по сути, брать несколько последних цифр от каждого значения в нашем выражении. 

Мы получаем цепочку ребусов такого вида:

    А+А = О (mod 10)

    ЗА+ЗА = ДО (mod 100)

    ОЗА+ОЗА = АДО (mod 1000)

    КОЗА+КОЗА = ТАДО (mod 10000)

    КОЗА+КОЗА = СТАДО (mod 100000)

Мы должны последовательно решить каждый из них с учетом решений предыдущих. А именно, первый ребус дает варианты:

    2+2 = 4, 3+3 = 6, 4+4 = 8, 5+5 = 0, 6+6 = 2, 7+7 = 4, 8+8 = 6, 9+9 = 8

Для каждого из этих вариатов мы пытаемся решить второй ребус, подставив в него предварительно буквы 'А' и 'О' в соответствии с вариантом. Допустим, `{А:2, О:4}`. В таком случае, второй ребус имеет следующие варианты решения:

    32+32 = 64, 52+52 = 04, 82+82 = 64, 92+92 = 84

Для кажого из эти вариантов мы решаем третий ребус...

В конце концов, мы получим все варианты, каждый из которых решает пятый ребус. Это множество вариантов гарантированно содержит все ответы на наш ребус, и может содержать некоторое количество ложных ответов. К примеру, ребус `А+А=В` решенный таким образом имел бы в качестве кандидатов на решения сложения двух равных цифр, перечисленные выше, но верными были бы только `2+2 = 4, 3+3 = 6, 4+4 = 8`. Нам не составит никакого труда отфильтровать итоговый список вариантов, проверив каждый из них на оригинальном ребусе уже без всяких алгебраических колец.

## Часть третья. Выкладка.

Теперь наше решение работает быстро! Однако нет никакой радости от обладания консольной программой, которой никто не пользуется. Время создать из решения веб-страницу и выложить в интернет.

Сегодня нам хочется попробовать организовать это простым, бесплатным способом, не требующим чего-то вроде VPS/VDS в нашем распоряжении. В наше время нет никакой проблемы бесплатно захостить любое статическое приложение на github pages. Однако, наш решающий код написан на python, который надо где-то запустить! Что делать?

Пути решения проблемы:

* Переписать код с python на javascript
* С помощью WebAssembley компилировать код на python в javascript
* Найти способ бесплатно исполнять где-то код python-функции.

Мне давно хотелось опробовать на чем-то serverless function - концепцию, придуманную впервые Amazon AWS как AWS Lambda, а позже взятую на вооружение и другими облачными хостерами. Перебрав варианты, и приняв во внимание некоторые затруднения, вызванные текущей геополитической обстановкой я остановился на яндекс.функциях. 

(Дальше описываем трудности в выкладке этого всего на яндекс функции)

Для 