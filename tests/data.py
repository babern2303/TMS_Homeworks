class TestData:
    task1 = [
        (1, 1, 0),
        (4, 1, 0.6),
    ]
    task2 = [
        (1, (1, 1)),
        (4, (64, 16)),
        (1.5, (3.375, 2.25)),
    ]
    task3 = [
        (3, 4, 5),
    ]
    task4_11 = [
        ("task4", "sdkfmskldfmesldf", "d"),
        ("task4", "TeachMeSkills", "l"),
        ("task4", "214354464435436", "3"),
        ("task5", "sdkfmskldfmesldf", "sdkfm"),
        ("task5", "TeachMeSkills", "Teach"),
        ("task5", "214354464435436", "21435"),
        ("task6", "sdkfmskldfmesldf", "sdkfmskldfmesl"),
        ("task6", "TeachMeSkills", "TeachMeSkil"),
        ("task6", "214354464435436", "2143544644354"),
        ("task7", "sdkfmskldfmesldf", "skmkdmsd"),
        ("task7", "TeachMeSkills", "Tahekls"),
        ("task7", "214354464435436", "24544346"),
        ("task8", "sdkfmskldfmesldf", "k"),
        ("task8", "TeachMeSkills", "a"),
        ("task8", "214354464435436", "4"),
        ("task9", "sdkfmsldf", "d"),
        ("task9", "TeachMeSkills", "TeachMeSkills!!!"),
        ("task9", "214354464", "1"),
        ("task10", "sdkfmsldf", ('m', None)),
        ("task10", "TeachMeSkills", ('e', None)),
        ("task10", "214324464", ('2', '1432446')),
        ("task11", "TeachMeSkills", False),
        ("task11", "12345654321", True),
        ("task11", "kinnikinnik", True),
    ]
    task12 = [
        ("TeachMeSkills", "e", 2),
        ("kinnikinnik", "k", 3),
        ("kinnikinnik", "n", 4),
    ]
    task13 = [
        (1234, False),
        (1000, True),
        (1000000000, True),
        (100000001, False),
    ]
    task14 = [
        (30, "кафе"),
        (52, "ресторан"),
        (10, "дом"),
        (50, "кафе"),
        (20, "кафе"),
    ]
    micro_calc = [
        (1, 2, "+", 3),
        (1, 2, "-", -1),
        (1, 2, ":", 0.5),
        (1, 2, "*", 2),
        (2, 2, "^", 4),
    ]
    micro_calc_errors = [
        (1, 0, ":"),
        (1, 3, "$")
    ]
    perfect_square = [
        ('.', True),
        ('..\n..', True),
        ('...\n...\n...', True),
        ('....\n....\n....\n....', True),
        ('+', False),
        (' .\n. ', False),
        ('...\n.:.\n...', False),
        ('---\n---\n---', False),
        ('123\n456\n789', False),
        ('.\n.\n.', False),
        ('...\n....\n...', False),
        ('...\n..\n...', False),
        ('.\n.......\n.', False),
        ('........', False),
        ('\n.', False),
        ('\n..', False),
        ('....\n....\n....', False),
        ('...\n.;..\n...', False),
        ('..\n\n..', False),
        ('...\n\n...', False),
        ('abc\ndefg\nhijkl', False),
    ]
    big_letters = [
        ('heLLo WorLD',
         'H   H EEEEE L     L      OOO        W   W  OOO  RRRR  L     DDDD\n'
         'H   H E     L     L     O   O       W   W O   O R   R L     D   D\n'
         'H   H E     L     L     O   O       W   W O   O R   R L     D   D\n'
         'HHHHH EEEEE L     L     O   O       W W W O   O RRRR  L     D   D\n'
         'H   H E     L     L     O   O       W W W O   O R R   L     D   D\n'
         'H   H E     L     L     O   O       W W W O   O R  R  L     D   D\n'
         'H   H EEEEE LLLLL LLLLL  OOO         W W   OOO  R   R LLLLL DDDD'),
        ('ABCDEFGHIJKLM',
         ' AAA  BBBB   CCC  DDDD  EEEEE FFFFF  GGG  H   H IIIII JJJJJ K   K L     M   M\n'
         'A   A B   B C   C D   D E     F     G   G H   H   I       J K  K  L     MM MM\n'
         'A   A B   B C     D   D E     F     G     H   H   I       J K K   L     M M M\n'
         'AAAAA BBBB  C     D   D EEEEE FFFFF G GGG HHHHH   I       J KK    L     M   M\n'
         'A   A B   B C     D   D E     F     G   G H   H   I       J K K   L     M   M\n'
         'A   A B   B C   C D   D E     F     G   G H   H   I       J K  K  L     M   M\n'
         'A   A BBBB   CCC  DDDD  EEEEE F      GGG  H   H IIIII JJJJ  K   K LLLLL M   M'),
        ('NOPQRSTUVWXYZ',
         'N   N  OOO  PPPP   QQQ  RRRR   SSS  TTTTT U   U V   V W   W X   X Y   Y ZZZZZ\n'
         'NN  N O   O P   P Q   Q R   R S   S   T   U   U V   V W   W X   X Y   Y     Z\n'
         'N   N O   O P   P Q   Q R   R S       T   U   U V   V W   W  X X   Y Y     Z\n'
         'N N N O   O PPPP  Q   Q RRRR   SSS    T   U   U V   V W W W   X     Y     Z\n'
         'N   N O   O P     Q Q Q R R       S   T   U   U V   V W W W  X X    Y    Z\n'
         'N  NN O   O P     Q  QQ R  R  S   S   T   U   U  V V  W W W X   X   Y   Z\n'
         'N   N  OOO  P      QQQQ R   R  SSS    T    UUU    V    W W  X   X   Y   ZZZZZ'),
        ('   same',
         ' SSS   AAA  M   M EEEEE\n'
         'S   S A   A MM MM E\n'
         'S     A   A M M M E\n'
         ' SSS  AAAAA M   M EEEEE\n'
         '    S A   A M   M E\n'
         'S   S A   A M   M E\n'
         ' SSS  A   A M   M EEEEE'),
        ('same   ',
         ' SSS   AAA  M   M EEEEE\n'
         'S   S A   A MM MM E\n'
         'S     A   A M M M E\n'
         ' SSS  AAAAA M   M EEEEE\n'
         '    S A   A M   M E\n'
         'S   S A   A M   M E\n'
         ' SSS  A   A M   M EEEEE'),
        ('   but   different   ',
         'BBBB  U   U TTTTT                   DDDD  IIIII FFFFF FFFFF EEEEE RRRR  EEEEE N   N TTTTT\n'
         'B   B U   U   T                     D   D   I   F     F     E     R   R E     NN  N   T\n'
         'B   B U   U   T                     D   D   I   F     F     E     R   R E     N   N   T\n'
         'BBBB  U   U   T                     D   D   I   FFFFF FFFFF EEEEE RRRR  EEEEE N N N   T\n'
         'B   B U   U   T                     D   D   I   F     F     E     R R   E     N   N   T\n'
         'B   B U   U   T                     D   D   I   F     F     E     R  R  E     N  NN   T\n'
         'BBBB   UUU    T                     DDDD  IIIII F     F     EEEEE R   R EEEEE N   N   T'),
        ('  ', '')
    ]
