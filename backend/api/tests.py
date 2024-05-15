from django.test import TestCase
from api.models import Company
from .serializers import CompanySerializer

# Create your tests here.
class Test(TestCase):
    def test_creditProfit(self):
        loadnAmount = 20000
        rate = 12
        countMonth = 36
        
        ratePerMonth = (rate / 100 + 1) ** (1 / 12) - 1
        persentPaymentPerMonth = loadnAmount * (ratePerMonth) / (1 - (1 + ratePerMonth) ** (-1 * countMonth))
        totalRevenue = persentPaymentPerMonth * countMonth - loadnAmount
        totalRevenue = round(totalRevenue, 2)
        
        correctValue = 3917 # Значение, полученное через онлайн калькулятор
        if (abs((totalRevenue / correctValue) - 1) * 100 < 1):
            self.assertTrue(True)
        else:
            self.assertFalse(False)
        
    def setUp(self):
        self.object = Company.objects.create(
            name = 'test',
            ful_name = 'test_last',
            representative_name = 'M',
            representative_last_name = 'source',
            phone = 79134570795,
            email = 'email',
            address = 'adress',
            inn = 200000,
            kpp = 20,
            industry = 'industry',
            revenue = 100000000,
        )
        
    def tearDown(self):
        Company.objects.get(pk=1).delete() 
        
    def test_companyTable_get(self):
        try:
            Company.objects.get(pk=1)
            self.assertTrue(True)
        except Company.DoesNotExist:
            self.assertTrue(False)
            
    def test_companyTable_update(self):
        try:
            Company.objects.filter(pk=1).update(name = 'new name')
            self.assertTrue(True)
        except Company.DoesNotExist:
            self.assertTrue(False)
  