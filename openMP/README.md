Компилировать: g++ -fopenmp -std=gnu++11 changed_Source.cpp
Запускать: python3 scheduler.py > result.txt
Обработка результатов: (в среде ipython, например) 
  1. Убрать лишние комментарии к выводу: from prepared_data import *
  затем усреднить повторные вычисления (производился запуск 4 одинаковых вычислений 
      для защиты от случайных выбросов): from prepared_data2 import *
  затем визуализация: from the_best_plot import *
