from itertools import permutations

OPERATORS = {
    '+': (1, lambda x, y: x + y),
    '-': (1, lambda x, y: x - y),
    '*': (2, lambda x, y: x * y),
    '^': (3, lambda x, y: x ** y)
}

COUNT = 0

def parse(formula_string):
    word = ''
    for s in formula_string:
        if s.isalpha() or s.isdigit() or s == '?':
            word += s
        elif word:
            yield word
            word = ''
        if s in OPERATORS or s in "()=":
            yield s
    if word:
        yield word


def shunting_yard(parsed_formula):
    stack = []
    for token in parsed_formula:
        if token in OPERATORS:
            while stack and stack[-1] != "(" and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
                yield stack.pop()
            stack.append(token)
        elif token == ")":
            while stack:
                x = stack.pop()
                if x == "(":
                    break
                yield x
        elif token == "(":
            stack.append(token)
        else:
            yield token
    while stack:
        yield stack.pop()


def calc(polish, operators=None):
    global COUNT
    COUNT += 1
    if operators is None:
        operators = OPERATORS
    stack = []
    for token in polish:
        if token in operators:
            y, x = stack.pop(), stack.pop()
            stack.append(operators[token][1](x, y))
        else:
            stack.append(token)
    return stack[0]


def solve_part(rebus_part: [str], count: int, known_letters: str, known_digits_variables):
    digits_variables = set()

    if count:

        operators = {
            '+': (1, lambda x, y: (x + y) % 10 ** count),
            '-': (1, lambda x, y: (x - y) % 10 ** count),
            '*': (2, lambda x, y: (x * y) % 10 ** count),
            '^': (3, lambda x, y: (x % 10 ** count) ** y)
        }

        rebus_part = [word if word in operators else word[-count:] for word in rebus_part]

    else:

        operators = {
            '+': (1, lambda x, y: x + y),
            '-': (1, lambda x, y: x - y),
            '*': (2, lambda x, y: x * y),
            '^': (3, lambda x, y: x ** y)
        }

    unknown_letters = ''.join(list(
        filter(lambda x: x.isalpha() and x not in known_letters,
               set(list(''.join(rebus_part))))))

    total_letters = known_letters+unknown_letters

    for known_digits_variable in known_digits_variables:

        avalible_digits = [digit for digit in '0123456789' if digit not in known_digits_variable]

        if len(unknown_letters) > len(avalible_digits):
            continue

        known_table = ''.maketrans(known_letters, known_digits_variable)

        rebus_part_variable = [
            word if word in operators else
            word.translate(known_table)
            for word in rebus_part]

        for digits in permutations(avalible_digits, len(unknown_letters)):
            digits = ''.join(digits)
            table = ''.maketrans(unknown_letters, digits)

            rebus_permutate = [
                word if word in operators else
                int(word.translate(table))
                for word in rebus_part_variable]

            if calc(rebus_permutate, operators) == 0:
                digits_variables.add(known_digits_variable+digits)
    return total_letters, digits_variables


def delta(a, b):
    return f"(({a})-({b}))"


def solve_rebus_text(rebus_text):
    """ Получает строку в человеко-читаемом виде, состветствующую задаче. Выводит список строк, соотв. ответу. """

    answer_texts = []

    parts = ''.join(rebus_text.split()).split('=')

    parts_count = len(parts)

    if parts_count == 1:
        rebus = parts[0]
    elif parts_count == 2:
        rebus = f"(({parts[0]})-({parts[1]}))"
    else:
        delta_parts = []
        for i in range(parts_count - 1):
            delta_parts.append(f"(({parts[i]})-({parts[i + 1]}))^2")
        rebus = '+'.join(delta_parts)

    rebus = list(shunting_yard(parse(rebus)))

    word_max_len = 0
    for word in rebus:
        if len(word) > word_max_len:
            word_max_len = len(word)

    answers = ('', [''])

    for i in range(1, word_max_len):
        answers = solve_part(rebus, i, *answers)
    answers = solve_part(rebus, 0, *answers)

    for letters in answers[1]:
        table = ''.maketrans(answers[0], letters)
        answer_texts.append(rebus_text.translate(table))

    return answer_texts


if __name__ == '__main__':
    rebus_text = 'a+b=c'
    print(rebus_text)

    answer_texts = solve_rebus_text(rebus_text)

    for answer in answer_texts:
        print(answer)
    print(len(answer_texts))

    print(COUNT)