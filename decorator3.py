import time

def log_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        with open('log.txt', 'a') as f:
            f.write(f'{func.__name__} was called at {time.ctime()}, time elapsed: {end_time - start_time:.4f} seconds.\n')
        return result
    return wrapper

courses = ["Курс 1", "Курс 2", "Курс 3"]
mentors = [
    ["Виктор Сергеев", "Анна Сергеева", "Сергей Виролайнен", "Анна Виролайнен"],
    ["Сергей Виролайнен", "Анна Виролайнен", "Евгений Шмаргунов", "Олег Булыгин", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

mentors_names = []
for m in mentors:
    course_names = []
    for name in m:
        course_names.append(name.split()[0])
    mentors_names.append(course_names)

pairs = []

@log_decorator
def print_mentors(courses, mentors):
    for id1 in range(len(mentors_names)):
        for id2 in range(len(mentors_names)):
            if id1 == id2:
                continue
            intersection_set = set(mentors_names[0]) & set(mentors_names[1])
            if len(intersection_set) > 0:
                pair = {courses[0], courses[1]}
    print(f"На курсах '{courses[0]}' и '{courses[1]}' преподают: {', '.join(sorted(intersection_set))}")

print_mentors(courses, mentors_names)