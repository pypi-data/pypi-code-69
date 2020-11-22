from openfisca_core.model_api import *
from openfisca_uk.entities import *
import numpy as np

# Input variables


class employee_earnings(Variable):
    value_type = float
    entity = Person
    label = u"Gross employee_earnings per week"
    definition_period = ETERNITY


class deductions(Variable):
    value_type = float
    entity = Person
    label = u"Deductions from earnings per week"
    definition_period = ETERNITY


class self_employed_earnings(Variable):
    value_type = float
    entity = Person
    label = u"Earnings from self-employment per week"
    definition_period = ETERNITY


class maintenance_income(Variable):
    value_type = float
    entity = Person
    label = u"Income from maintenance payments per week"
    definition_period = ETERNITY


class interest(Variable):
    value_type = float
    entity = Person
    label = u"Income from interest per week"
    definition_period = ETERNITY


class assets(Variable):
    value_type = float
    entity = Person
    label = u"Total value of reported assets"
    definition_period = ETERNITY


class maintenance_expense(Variable):
    value_type = float
    entity = Person
    label = u"Expense fro maintenance payments per week"
    definition_period = ETERNITY


class misc_income(Variable):
    value_type = float
    entity = Person
    label = u"Miscellaneous income per week"
    definition_period = ETERNITY


class pension_income(Variable):
    value_type = float
    entity = Person
    label = u"Reported gross amount of occupational or private pension income per week"
    definition_period = ETERNITY


class total_benefits(Variable):
    value_type = float
    entity = Person
    label = u"Total amount of benefits received per week"
    definition_period = ETERNITY


class student_loan_repayments(Variable):
    value_type = float
    entity = Person
    label = u"Reported amount of weeklyised student loan payments"
    definition_period = ETERNITY


class net_income_adjustment(Variable):
    value_type = float
    entity = Person
    label = u"Adjustment for FRS net income disparities"
    definition_period = ETERNITY


class SSP(Variable):
    value_type = float
    entity = Person
    label = u"Amount of Statutory Sick Pay per week"
    definition_period = ETERNITY


class eligible_childcare_cost(Variable):
    value_type = float
    entity = Person
    label = u"Costs of registered childcare for this person per week"
    definition_period = ETERNITY


# Derived variables


class external_child_payment(Variable):
    value_type = float
    entity = Person
    label = u"Amount of the benefit units external child maintenance paid by this person"
    definition_period = ETERNITY

    def formula(person, period, parameters):
        return person("is_head", period) * person.benunit(
            "external_child_maintenance", period
        )


class earnings(Variable):
    value_type = float
    entity = Person
    label = u"Total earnings per week"
    definition_period = ETERNITY

    def formula(person, period, parameters):
        return person("employee_earnings", period) + person(
            "self_employed_earnings", period
        )


class state_pension(Variable):
    value_type = float
    entity = Person
    label = u"Amount of State Pension income per week"
    definition_period = ETERNITY

    def formula(person, period, parameters):
        return person("state_pension_reported", period)


class benefits(Variable):
    value_type = float
    entity = Person
    label = u"Non-State Pension benefit total"
    definition_period = ETERNITY

    def formula(person, period, parameters):
        return person("total_benefits", period) - person(
            "state_pension_reported", period
        )


class income_tax_applicable_amount(Variable):
    value_type = float
    entity = Person
    label = u"Total taxable income per week"
    definition_period = ETERNITY

    def formula(person, period, parameters):
        TAXABLE_BENEFITS = [
            "BSP",
            "carers_allowance",
            "ESA_contrib",
            "incapacity_benefit",
            "JSA_contrib",
            "IIDB",
        ]
        taxed_benefit_sum = sum(
            map(
                lambda benefit: person(benefit + "_reported", period),
                TAXABLE_BENEFITS,
            )
        )
        return max_(
            person("employee_earnings", period)
            + person("self_employed_earnings", period)
            + person("state_pension", period)
            + 0.75 * person("pension_income", period)
            + taxed_benefit_sum
            + person("taxed_means_tested_bonus", period),
            0,
        )


class capital_gains_tax(Variable):
    value_type = float
    entity = Person
    label = u"Capital Gains Tax on investment income"
    definition_period = ETERNITY

    def formula(person, period, parameters):
        estimated_yearly_gains = person("interest", period) * 52
        basic_amount = min_(
            estimated_yearly_gains,
            parameters(period).taxes.capital_gains_tax.higher_threshold,
        )
        higher_amount = max_(
            0,
            estimated_yearly_gains
            - parameters(period).taxes.capital_gains_tax.higher_threshold,
        )
        yearly_tax = (
            basic_amount
            * parameters(period).taxes.capital_gains_tax.basic_rate
            + higher_amount
            * parameters(period).taxes.capital_gains_tax.higher_rate
        )
        return yearly_tax / 52


class NI(Variable):
    value_type = float
    entity = Person
    label = u"National Insurance paid per week"
    definition_period = ETERNITY
    reference = ["https://www.gov.uk/national-insurance"]

    def formula(person, period, parameters):
        employee_NI = parameters(
            period
        ).taxes.national_insurance.employee_rates.calc(
            person("employee_earnings", period)
            + person("taxed_means_tested_bonus", period)
        )
        estimated_yearly_self_emp = (
            person("self_employed_earnings", period) * 52
        )
        self_employed_NI_basic = parameters(
            period
        ).taxes.national_insurance.self_employed_basic * (
            estimated_yearly_self_emp
            > parameters(
                period
            ).taxes.national_insurance.self_employed_basic_threshold
        )
        self_employed_NI_higher = (
            parameters(
                period
            ).taxes.national_insurance.self_employed_higher.calc(
                estimated_yearly_self_emp
            )
            / 52
        )
        return (1 - person("is_state_pension_age", period)) * (
            employee_NI + self_employed_NI_basic + self_employed_NI_higher
        )


class personal_allowance(Variable):
    value_type = float
    entity = Person
    label = u"Amount of personal allowance per year"
    definition_period = ETERNITY

    def formula(person, period, parameters):
        estimated_yearly_income = (
            person("income_tax_applicable_amount", period)
        ) * 52
        pa_deduction = parameters(
            period
        ).taxes.income_tax.personal_allowance_deduction.calc(
            estimated_yearly_income
        )
        return max_(
            0,
            parameters(period).taxes.income_tax.personal_allowance
            - pa_deduction,
        )


class income_tax(Variable):
    value_type = float
    entity = Person
    label = u"Income tax paid per week"
    definition_period = ETERNITY

    def formula(person, period, parameters):
        estimated_yearly_income = (
            person("income_tax_applicable_amount", period)
        ) * 52
        weekly_tax = (
            parameters(period).taxes.income_tax.income_tax.calc(
                max_(
                    estimated_yearly_income
                    - person("personal_allowance", period),
                    0,
                )
            )
        ) / 52
        return weekly_tax + person("child_benefit_reduction", period)


class income_tax_and_NI(Variable):
    value_type = float
    entity = Person
    label = u"Total NI and Income tax paid per week"
    definition_period = ETERNITY

    def formula(person, period, parameters):
        return person("NI", period) + person("income_tax", period)


class taxed_means_tested_bonus(Variable):
    value_type = float
    entity = Person
    label = u"Variable for a future taxed and means-tested benefit"
    definition_period = ETERNITY


class untaxed_means_tested_bonus(Variable):
    value_type = float
    entity = Person
    label = u"Variable for a future untaxed, but means-tested benefit"
    definition_period = ETERNITY


class non_means_tested_bonus(Variable):
    value_type = float
    entity = Person
    label = u"Variable for a future untaxed, non-means-tested benefit"
    definition_period = ETERNITY


class child_benefit_reduction(Variable):
    value_type = float
    entity = Person
    label = u"High income tax charge on the Child Benefit"
    definition_period = ETERNITY

    def formula(person, period, parameters):
        return (
            person("is_head", period)
            * person.benunit("child_benefit", period)
            * 1e-4
            * max_(0, person("income_tax_applicable_amount", period) - 961)
        )


class income(Variable):
    value_type = float
    entity = Person
    label = u"Income per week (not including benefits)"
    definition_period = ETERNITY

    def formula(person, period, parameters):
        COMPONENTS = [
            "employee_earnings",
            "self_employed_earnings",
            "pension_income",
            "state_pension",
            "interest",
            "taxed_means_tested_bonus",
            "untaxed_means_tested_bonus",
        ]
        return sum(
            map(lambda component: person(component, period), COMPONENTS)
        )


class actual_net_income(Variable):
    value_type = float
    entity = Person
    label = u"Actual net income from FRS"
    definition_period = ETERNITY


class post_tax_income(Variable):
    value_type = float
    entity = Person
    label = u"Post-tax income, before benefits, per week"
    definition_period = ETERNITY

    def formula(person, period, parameters):
        return (
            person("income", period)
            - person("income_tax", period)
            - person("NI", period)
            - person("capital_gains_tax", period)
        )


class benefit_modelling(Variable):
    value_type = float
    entity = Person
    label = u"Difference between reported person-level benefits and modelled benefits"
    definition_period = ETERNITY

    def formula(person, period, parameters):
        ADDED_BENEFITS = ["JSA_contrib"]
        REMOVED_BENEFITS = ["JSA_contrib_reported"]
        added_sum = sum(
            map(lambda benefit: person(benefit, period), ADDED_BENEFITS)
        )
        removed_sum = sum(
            map(lambda benefit: person(benefit, period), REMOVED_BENEFITS)
        )
        benunit_benefit_modelling = person("is_head", period) * person.benunit(
            "benunit_benefit_modelling", period
        )
        return added_sum - removed_sum + benunit_benefit_modelling


class gross_income(Variable):
    value_type = float
    entity = Person
    label = u"Gross income per week"
    definition_period = ETERNITY

    def formula(person, period, parameters):

        COMPONENTS = [
            "employee_earnings",
            "self_employed_earnings",
            "pension_income",
            "state_pension",
            "interest",
            "untaxed_means_tested_bonus",
            "taxed_means_tested_bonus",
            "benefits",
            "non_means_tested_bonus",
            "maintenance_income",
        ]
        return sum(
            map(lambda component: person(component, period), COMPONENTS)
        ) + person("benefit_modelling", period)


class net_income(Variable):
    value_type = float
    entity = Person
    label = u"Net income per week"
    definition_period = ETERNITY

    def formula(person, period, parameters):
        return (
            person("gross_income", period)
            - person("income_tax", period)
            - person("NI", period)
            - person("capital_gains_tax", period)
            - person("maintenance_expense", period)
            - person("deductions", period)
            - person("student_loan_repayments", period)
            - person("external_child_payment", period)
            - person("misc_income", period)
        )


class personal_housing_costs(Variable):
    value_type = float
    entity = Person
    label = u"Amount paid for houshold housing costs"
    definition_period = ETERNITY

    def formula(person, period, parameters):
        return person("is_householder", period) * person.household(
            "housing_costs", period
        )


class receives_means_tested_benefits(Variable):
    value_type = float
    entity = Person
    label = u"Whether the person receives means-tested benefits"
    definition_period = ETERNITY

    def formula(person, period, parameters):
        MEANS_TESTED_BENEFITS = [
            "working_tax_credit",
            "child_tax_credit",
            "pension_credit",
            "JSA_income",
            "income_support",
            "housing_benefit",
            "universal_credit",
        ]
        return (
            sum(
                map(
                    lambda benefit: person.benunit(benefit, period),
                    MEANS_TESTED_BENEFITS,
                )
            )
            > 0
        )


class person_household_net_income_ahc(Variable):
    value_type = float
    entity = Person
    label = u"The persons household net income AHC"
    definition_period = ETERNITY

    def formula(person, period, parameters):
        return person.household("household_net_income_ahc", period)


class person_benunit_net_income(Variable):
    value_type = float
    entity = Person
    label = u"The persons benefit unit net income"
    definition_period = ETERNITY

    def formula(person, period, parameters):
        return person.benunit("benunit_net_income", period)


class person_benunit_IS(Variable):
    value_type = float
    entity = Person
    label = u"Income Support received by the persons benefit unit"
    definition_period = ETERNITY

    def formula(person, period, parameters):
        return person.benunit("income_support", period)


class person_benunit_UC(Variable):
    value_type = float
    entity = Person
    label = u"Universal Credit received by the persons benefit unit"
    definition_period = ETERNITY

    def formula(person, period, parameters):
        return person.benunit("universal_credit", period)


class person_benunit_PC(Variable):
    value_type = float
    entity = Person
    label = u"Pension Credit received by the persons benefit unit"
    definition_period = ETERNITY

    def formula(person, period, parameters):
        return person.benunit("pension_credit", period)


class person_benunit_TC(Variable):
    value_type = float
    entity = Person
    label = u"Tax Credits received by the persons benefit unit"
    definition_period = ETERNITY

    def formula(person, period, parameters):
        return person.benunit("working_tax_credit", period) + person.benunit(
            "child_tax_credit", period
        )


class person_benunit_JSA(Variable):
    value_type = float
    entity = Person
    label = u"JSA received by the persons benefit unit"
    definition_period = ETERNITY

    def formula(person, period, parameters):
        return person.benunit("JSA_income", period) + person(
            "JSA_contrib", period
        )
