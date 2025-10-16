import unittest

from work_place import *


class ScoreListTest(unittest.TestCase):

    def test_a_scenario(self):
        w = WorkPlace("quera")
        w.expertise = "mine"

        def f(self):
            self.capacity += 1

        WorkPlace.calc_capacity = f

        w.upgrade()

        class Person:
            pass

        p = Person()
        p.work_place = None
        w.hire(p)

        self.assertEqual(w.employees[0], p, '\nدر تابع سازنده کلاس WorkPlace، لیست کارکنان را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(w.level, 2, '\nدر تابع سازنده کلاس WorkPlace، سطح محل کار را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(w.capacity, 2, '\nدر تابع سازنده کلاس WorkPlace، ظرفیت محل کار را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(w.name, "quera", '\nدر تابع سازنده کلاس WorkPlace، نام محل کار را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(w.get_expertise(), "mine", '\nدر تابع get_expertise، تخصص مورد نظر را به درستی برنمی‌گردانید.')
        self.assertEqual(w.get_price(), Consts.BASE_PRICE["mine"], '\nدر تابع get_price، قیمت ساخت محل کار مورد نظر را به درستی برنمی‌گردانید.')

        WorkPlace.instances = []

        def f(a):
            def g():
                return a

            return g

        WorkPlace("new workplace").calc_costs = f(-10)
        WorkPlace("new workplace").calc_costs = f(-20)
        WorkPlace("new workplace").calc_costs = f(-30)

        self.assertEqual(60, WorkPlace.calc_all(), '\nدر تابع calc_all، مجموع وضعیت مالی را به درستی محاسبه نمی‌کنید.')