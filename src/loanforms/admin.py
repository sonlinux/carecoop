# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# from .models import (PersonalInformation, LoanApplication, LoanPaymentShareContribution, OutStandingLoans, 
# 					Security, Declaration, ReviewedByCoOperativeManager,
# 					LoanAnalysisAndApprovalByLoans, NameSignatureDate)

# class PersonalInformationAdmin(admin.ModelAdmin):
# 	list_display = ['name','organisation','member_number','employee_number','email_address','telephone','physical_address',
# 	'postal_address','length_of_membership','nrc_number']

# 	class Meta:
# 		model = PersonalInformation

# admin.site.register(PersonalInformation, PersonalInformationAdmin)

# class LoanApplicationAdmin(admin.ModelAdmin):
# 	list_display = ['amount_applied_for','amount_in_words','period_repayment','purposes_for_the_loan']

# 	class Meta:
# 		model = LoanApplication

# admin.site.register(LoanApplication, LoanApplicationAdmin)

# class LoanPaymentShareContributionAdmin(admin.ModelAdmin):
# 	list_display = ['period_of_repayment','monthly_principal_deduction','monthly_interest_deduction',
# 	'monthly_share_contribution','total_care_coop_deduction']

# 	class Meta:
# 		model = LoanPaymentShareContribution

# admin.site.register(LoanPaymentShareContribution, LoanPaymentShareContributionAdmin)


#
# from .models import (PersonalInformation, LoanApplication, LoanPaymentShareContribution, OutStandingLoans,
# 					Security, Declaration, ReviewedByCoOperativeManager,
# 					LoanAnalysisAndApprovalByLoans, NameSignatureDate)
#
# class PersonalInformationAdmin(admin.ModelAdmin):
# 	list_display = ['name','organisation','member_number','employee_number','email_address','telephone','physical_address',
# 	'postal_address','length_of_membership','nrc_number']
#
# 	class Meta:
# 		model = PersonalInformation
#
# admin.site.register(PersonalInformation, PersonalInformationAdmin)
#
# class LoanApplicationAdmin(admin.ModelAdmin):
# 	list_display = ['amount_applied_for','amount_in_words','period_repayment','purposes_for_the_loan']
#
# 	class Meta:
# 		model = LoanApplication
#
# admin.site.register(LoanApplication, LoanApplicationAdmin)
#
# class LoanPaymentShareContributionAdmin(admin.ModelAdmin):
# 	list_display = ['period_of_repayment','monthly_principal_deduction','monthly_interest_deduction',
# 	'monthly_share_contribution','total_care_coop_deduction']
#
# 	class Meta:
# 		model = LoanPaymentShareContribution
#
# admin.site.register(LoanPaymentShareContribution, LoanPaymentShareContributionAdmin)
#
# class OutStandingLoansAdmin(admin.ModelAdmin):
# 	list_display = ['premium_loan_amount','premium_balance','premium_monthly_repayment',
# 				 'ordinary_loan_amount','ordinary_balance','ordinary_monthly_repayment',
# 				 'rental_plus_loan_amount','rental_plus_balance','rental_plus_monthly_repayment',
# 				 'education_loan_amount','education_balance','education_monthly_repayment',
# 				 'emergency_loan_amount','emergency_balance','emergency_monthly_repayment',
# 				 'family_holiday_loan_amount','family_holiday_balance','family_holiday_monthly_repayment',
# 				 'commodity_loan_amount','commodity_balance','commodity_monthly_repayment',
# 				 'building_loan_amount','building_balance','building_monthly_repayment',
# 				 'land_purchase_loan_amount','land_purchase_balance','land_purchase_monthly_repayment',
# 				 'care_coop_land_loan_amount','care_coop_land_balance','care_coop_land_monthly_repayment',
# 				 'vehicle_loan_amount','vehicle_balance','vehicle_monthly_repayment',
# 				 'vehicle_insurance_loan_amount','vehicle_insurance_balance','vehicle_insurance_monthly_repayment',
# 				 'share_financing_loan_amount','share_financing_balance','share_financing_monthly_repayment',
# 				 'home_improvement_loan_amount','home_improvement_balance','home_improvement_monthly_repayment']


# 	class Meta:
# 		model = OutStandingLoans

# admin.site.register(OutStandingLoans, OutStandingLoansAdmin)

# class SecurityAdmin(admin.ModelAdmin):
# 	list_display = ['total_shares','terminal_benefits_accured','total','signaturea','signatureb','datea','dateb']

# 	class Meta:

# 		model = Security

# admin.site.register(Security, SecurityAdmin)


# class DeclarationAdmin(admin.ModelAdmin):
# 	list_display = ['applicant_name','datea','signature','dateb','bank_name','account_no',
# 					'branch','cheque','bank_transfer']

# 	class Meta:
# 		model = Declaration

# admin.site.register(Declaration, DeclarationAdmin)

# class ReviewedByCoOperativeManagerAdmin(admin.ModelAdmin):
# 	list_display = ['name','date','signature']

# 	class Meta:
# 		model = ReviewedByCoOperativeManager

# admin.site.register(ReviewedByCoOperativeManager, ReviewedByCoOperativeManagerAdmin)

#
# 	class Meta:
# 		model = OutStandingLoans
#
# admin.site.register(OutStandingLoans, OutStandingLoansAdmin)
#
# class SecurityAdmin(admin.ModelAdmin):
# 	list_display = ['total_shares','terminal_benefits_accured','total','signaturea','signatureb','datea','dateb']
#
# 	class Meta:
#
# 		model = Security
#
# admin.site.register(Security, SecurityAdmin)
#
#
# class DeclarationAdmin(admin.ModelAdmin):
# 	list_display = ['applicant_name','datea','signature','dateb','bank_name','account_no',
# 					'branch','cheque','bank_transfer']
#
# 	class Meta:
# 		model = Declaration
#
# admin.site.register(Declaration, DeclarationAdmin)
#
# class ReviewedByCoOperativeManagerAdmin(admin.ModelAdmin):
# 	list_display = ['name','date','signature']
#
# 	class Meta:
# 		model = ReviewedByCoOperativeManager
#
# admin.site.register(ReviewedByCoOperativeManager, ReviewedByCoOperativeManagerAdmin)
#
# class LoanAnalysisAndApprovalByLoansAdmin(admin.ModelAdmin):
# 	list_display = ['comments','chair_person_name','chair_person_signature','chair_person_date',
# 					'Treasurer_name','Treasurer_signature','Treasurer_date',
# 					'committee_member_name','committee_member_signature','committee_member_date']
# 	class Meta:
# 		model = LoanAnalysisAndApprovalByLoans

# admin.site.register(LoanAnalysisAndApprovalByLoans, LoanAnalysisAndApprovalByLoansAdmin)
			
# class NameSignatureDateAdmin(admin.ModelAdmin):
# 	list_display = ['name','signature','date']

# 	class Meta:
# 		model = NameSignatureDate

#
# admin.site.register(LoanAnalysisAndApprovalByLoans, LoanAnalysisAndApprovalByLoansAdmin)
#
# class NameSignatureDateAdmin(admin.ModelAdmin):
# 	list_display = ['name','signature','date']
#
# 	class Meta:
# 		model = NameSignatureDate
#
# admin.site.register(NameSignatureDate, NameSignatureDateAdmin)

# # class SuccessStoriesAdmin(admin.ModelAdmin):
# # 	list_display = ['message','name','carecoopnumber','','','','']

# # Register your models here.


# Register your models here.
