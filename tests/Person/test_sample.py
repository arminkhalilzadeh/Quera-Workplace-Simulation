import unittest, math
from person import Person

class ScoreListTest(unittest.TestCase):

    def test_a_scenario(self):
        p = Person("mammad", 10)
        p.job = "mohandes"
        p.level = 9
        p.upgrade()

        class WorkPlace:
            pass

        p.work_place = WorkPlace()
        p.work_place.level = 5

        def f(a):
            def g():
                return a
            return g

        self.assertEqual(p.name, "mammad", '\nدر تابع سازنده کلاس Person، نام فرد را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(p.age, 10, '\nدر تابع سازنده کلاس Person، سن فرد را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(p.job, "mohandes", '\nدر تابع سازنده کلاس Person، نوع کار فرد را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(p.level, 10, '\nدر تابع سازنده کلاس Person، سطح فرد را به درستی مقداردهی نمی‌کنید.') # 1 + 9

        p.calc_income = f(100)
        p.calc_life_cost = f(20)
        self.assertAlmostEqual(p.calc(), p.do_level(p.calc_income()) - p.calc_life_cost(), delta=1e-5)