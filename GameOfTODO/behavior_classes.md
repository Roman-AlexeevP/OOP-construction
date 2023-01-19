
class Task:

name - str - название задачи

description - str - описание задачи

started_at - datetime - дата и время создания задачи

ended_at - datetime - дата и время дедлайна по задаче

type - int - один из 4 типов задачи

worked_time_by_sec - int кол-во отработанного времени в секундах

is_active - bool - активна ли задача на текущий момент

close() - закрыть задачу(выполнить)

is_closed() - закрыта задача или нет на текущий момент

is_open() - доступна ли задача для роаботы на текущий момент

work_for() - добавляет к отработанному времени еще времени в секундах

activate() - сделать задачу активной на текущий момент

is_active() - активна ли задача на текущий момент

TaskMatrix

important_urgent_tasks - TasksList список задач: важные и срочные

not_important_urgent_tasks - TasksList список задач: неважные и срочные

important_not_urgent_tasks - TasksList список задач: важные и несрочные

not_important_not_urgent_tasks - TasksList список задач: неважные и несрочные


get_task_count() - общее кол-во задач

get_task_hours() - общий объем задач в часах


is_matrix_empty() - пуста ли матрица или нет

can_create_more_task() - можно ли добавить задачу

get_tasks_names() - имена задач для отображения

get_most_important_task() - возвращает наиболее приоритетную задачу на текущий момент


TasksList

task - list - список задач

get_last_created_task() - возвращает последнюю созданную задачу

get_first_created_task() - возвращает первую созданную задачу

get_largest_task() - возвращает наибольшую по объему задачу

get_tiniest_task() - возвращает наименьшую по объему задачу

