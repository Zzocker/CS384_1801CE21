class Student(object):
    def __init__(self):
        self.sem_total_credits = dict()
        self.sem_credit_obtained = dict()
        self.sem_spi_numerator = dict()
        self.current_sem = 0
    def get_sem_total_credits(self,sem):
        return self.sem_total_credits.setdefault(sem,0)
    def get_sem_credit_obtained(self,sem):
        return self.sem_credit_obtained.setdefault(sem,0)
    def get_sem_spi_numerator(self,sem):
        return self.sem_spi_numerator.setdefault(sem,0)
    def get_current_sem(self):
        return self.current_sem
    def add_grade(self,sem,credit,grade):
        self.sem_total_credits[sem] = self.sem_total_credits.setdefault(sem,0)+credit
        self.sem_credit_obtained[sem] = self.sem_credit_obtained.setdefault(sem,0)+grade
        self.sem_spi_numerator[sem] = self.sem_spi_numerator.setdefault(sem,0)+(grade*credit)
        if sem > self.current_sem:
            self.current_sem = sem
    def get_total_credit(self,sem):
        out = 0
        for i in range(1,sem+1):
            out=out+self.get_sem_total_credits(i)
        return out
    def get_total_credit_obtained(self,sem):
        out = 0
        for i in range(1,sem+1):
            out=out+self.get_sem_credit_obtained(i)
        return out
    def get_spi(self,sem):
        credit = self.get_sem_total_credits(sem)
        if credit == 0:
            return 0
        return self.get_sem_spi_numerator(sem)/credit
    def get_cpi(self,sem):
        credit = self.get_total_credit(sem)
        if credit == 0:
            return 0
        numerator = 0
        for i in range(1,sem+1):
            numerator=numerator+(self.get_spi(i)*self.get_sem_total_credits(i))
        return numerator/credit
    
