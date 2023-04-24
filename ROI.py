class RentalProperty:
    def __init__(self, property_value, rental_income, laundry_income, storage_income, misc_income,
                 taxes, insurance, utilities, hoa, lawn_snow, vacancy, repairs, capex, property_management, mortgage):
        self.property_value = property_value
        self.rental_income = rental_income
        self.laundry_income = laundry_income
        self.storage_income = storage_income
        self.misc_income = misc_income
        self.taxes = taxes
        self.insurance = insurance
        self.utilities = utilities
        self.hoa = hoa
        self.lawn_snow = lawn_snow
        self.vacancy = vacancy
        self.repairs = repairs
        self.capex = capex
        self.property_management = property_management
        self.mortgage = mortgage

    def calculate_cashflow(self):
        total_income = self.rental_income + self.laundry_income + self.storage_income + self.misc_income
        total_expenses = self.taxes + self.insurance + self.utilities + self.hoa + self.lawn_snow + \
                         self.vacancy + self.repairs + self.capex + self.property_management + self.mortgage
        return total_income - total_expenses

    def calculate_cash_on_cash_roi(self, down_payment, closing_costs, rehab_budget, misc_other):
        total_investment = down_payment + closing_costs + rehab_budget + misc_other
        cashflow = self.calculate_cashflow()
        return cashflow * 12 / total_investment * 100


# example usage
property_value = 200000
rental_income = 2000
laundry_income = 0
storage_income = 0
misc_income = 0
taxes = 150
insurance = 100
utilities = 0
hoa = 0
lawn_snow = 0
vacancy = 100
repairs = 100
capex = 100
property_management = 200
mortgage = 860

rental_property = RentalProperty(property_value, rental_income, laundry_income, storage_income, misc_income,
                                 taxes, insurance, utilities, hoa, lawn_snow, vacancy, repairs, capex,
                                 property_management, mortgage)

cash_on_cash_roi = rental_property.calculate_cash_on_cash_roi(40000, 3000, 7000, 0)
print(f"Cash on Cash ROI: {cash_on_cash_roi:.2f}%")
