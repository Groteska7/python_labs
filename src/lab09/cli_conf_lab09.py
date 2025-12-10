import argparse
import sys
from group import Group
from lab08.models import Student


def main():
    parser = argparse.ArgumentParser(description="Невероятные манипуляции студентами")

    parser.add_argument('--data-file', '-d', default='data/lab09/students.csv',help='Путь к файлу с данными (по умолчанию: data/lab09/students.csv)')

    subparsers = parser.add_subparsers(dest="command",required=True,title="доступные команды")

    parser_add = subparsers.add_parser('add', help='Добавить студента')
    parser_add.add_argument('fio',help='ФИО студента')
    parser_add.add_argument('-g','--group',required=True, help='Группа')
    parser_add.add_argument('--gpa',required=True,type=float, help='Средний балл')
    parser_add.add_argument('--birthdate',required=True,help='Дата рождения (ДД.ММ.ГГГГ)')

    parser_remove = subparsers.add_parser('remove',help='удаление студента')
    parser_remove.add_argument('fio',help='ФИО студента')

    parser_update = subparsers.add_parser('update',help='обновление информации о студенте')
    parser_update.add_argument('fio',help='ФИО студента')
    parser_update.add_argument('--group',help='Группа, на которую необходимо заменить')
    parser_update.add_argument('--birthdate',help='Дата рождения (ДД.ММ.ГГГГ)')
    parser_update.add_argument('--gpa',help='GPA, на который необходимо заменить')

    parser_find = subparsers.add_parser('find',help='Поиск студента по части информации (имени или типо того)')
    parser_find.add_argument('fio',help='Поиск студента по части информации (имени или типо того)')


    args = parser.parse_args()

    group = Group(args.data_file)

    if args.command == "add":
        student = Student(
                fio=args.fio,
                group=args.group,
                gpa=args.gpa,
                birthdate=args.birthdate
        )
        result = group.add(student)
        print(result)
    
    elif args.command == 'update':
        string={}
        if args.group:
            string["group"]=args.group
        if args.gpa is not None:
            string["gpa"]=args.gpa
        if args.birthdate is not None:
            string["birthdate"]=args.birthdate
        # print(string)
        print(group.update(args.fio,**string))
    elif args.command == 'remove':
        print(group.remove(args.fio))
    elif args.command == 'find':
        print(group.find(args.fio))

if __name__ == "__main__":
    main()