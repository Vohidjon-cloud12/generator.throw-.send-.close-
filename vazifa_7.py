# # 1-Fibonachi sonlarini Infinitive ( Cheksiz) iterator  orqali chiqarish:
# class InfiniteFibonacciIterator:
#     def __init__(self):
#         self.a = 0
#         self.b = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         current = self.a
#         self.a, self.b = self.b, self.a + self.b
#         return current
#
# # Фибоначчи итераторидан фойдаланиш
# fibonacci_iterator = InfiniteFibonacciIterator()
#
# # Бир неча Фибоначчи сонларини чиқариш
# while True:
#     print(next(fibonacci_iterator))



#2- Fibonacci sonlarini Infinitiveni ( Cheksiz) chiqarish generator orqali:
# def infinite_fibonacci_generator():
#     """Fibonachi sonlarini qayatruvchi funksiya"""
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# # Фибоначчи генераторидан фойдаланиш
# fibonacci_generator = infinite_fibonacci_generator()
# # Бир неча Фибоначчи сонларини чиқариш
# while True:
#     print(next(fibonacci_generator))

# def programming_language_generator(languages):
#     try:
#         index = 0
#         while index < len(languages):
#             received = (yield languages[index])
#             if received is not None:
#                 index = received
#             else:
#                 index += 1
#     except GeneratorExit:
#         print("Generator closed")
#     except Exception as e:
#         print(f"Exception: {e}")
#
# programming_languages = [
#     "Python", "JavaScript", "Java", "C++", "C#", "Ruby", "Go", "Swift", "Kotlin", "Rust"
# ]
#
# # Генераторни яратиш
# gen = programming_language_generator(programming_languages)
#
# # .send() методини ишлатиш
# print(next(gen))  # Python
# print(gen.send(3))  # C++
# print(next(gen))  # C#
# print(gen.send(None))  # Ruby
#
# # .throw() методини ишлатиш
# try:
#     gen.throw(ValueError, "Some error")
# except ValueError as e:
#     print(f"Caught an exception: {e}")
#
# # .close() методини ишлатиш
# gen.close()

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
class Fibonacci:
    def __init__(self):


































