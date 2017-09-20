# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

"""
	This model represents the Revised Member Organisations Loan Form child
	 under Loan Forms
"""

# class PersonalInformation(models.Model):

# 	# B. PERSONAL INFORMATION (to be filled by loan applicant)
# 	name = models.CharField(_("1. Members Name"),max_length=255, null=True, blank=True)
# 	organisation = models.CharField(_("2. Member's Organisation"),max_length=255, null=True, blank=True)
# 	member_number = models.CharField(_("3. Member's Number"),max_length=255, null=True, blank=True)
# 	employee_number = models.CharField(_("4. Employee Number"),max_length=255, null=True, blank=True)
# 	email_address = models.CharField(_("5. Email Address"),max_length=255, null=True, blank=True)
# 	telephone = models.CharField(_("6. Contact telephone No."),max_length=255, null=True, blank=True)
# 	physical_address = models.CharField(_("7. Physical Address"),max_length=255, null=True, blank=True)
# 	postal_address = models.CharField(_("8. Postal Address"),max_length=255, null=True, blank=True)
# 	length_of_membership = models.CharField(_("9. Length of Membership"),max_length=255, null=True, blank=True)
# 	nrc_number = models.CharField(_("10. NRC No."),max_length=255, null=True, blank=True)
# 	created = models.DateTimeField(auto_now_add=True)

# 	class Meta:
# 		ordering = ['-created']
# 		verbose_name = 'PERSONAL INFORMATION'
# 		verbose_name_plural = 'PERSONAL INFORMATIONS'

# 	def __unicode__(self):
# 		return self.name

# class LoanApplication(models.Model):

# 	# C. LOAN APPLICATION (to be filled by loan applicant)
# 	amount_applied_for = models.CharField(_("1. Amount Applied for (K)"),max_length=255, null=True, blank=True)
# 	amount_in_words = models.CharField(_("2. Amount in Words (K)"),max_length=255, null=True, blank=True)
# 	period_repayment = models.CharField(_("3. Period of Repayment (months)"),max_length=255, null=True, blank=True)
# 	purposes_for_the_loan = models.CharField(_("4. Purpose for the Loan"),max_length=255, null=True, blank=True)
# 	created = models.DateTimeField(auto_now_add=True)

# 	class Meta:
# 		ordering = ['-created']
# 		verbose_name = 'LOAN APPLICATION'
# 		verbose_name_plural = 'LOAN APPLICATIONS'

# 	def __unicode__(self):
# 		return self.amount_applied_for

# class LoanPaymentShareContribution(models.Model):

# 	# D. LOAN REPAYMENT/SHARE CONTRIBUTION (to be filled in by Coop Loans Officer)
# 	period_of_repayment = models.CharField(_("1. Period of Repayment (months)"),max_length=255, null=True, blank=True)
# 	monthly_principal_deduction = models.CharField(_("2. Monthly Principal Deduction (K)"),max_length=255, null=True, blank=True)
# 	monthly_interest_deduction = models.CharField(_("3. Monthly Interest Deduction (K)"),max_length=255, null=True, blank=True)
# 	monthly_share_contribution = models.CharField(_("4. Monthly Share Contribution(K)"),max_length=255, null=True, blank=True)
# 	total_care_coop_deduction = models.CharField(_("5. Total Care Coop Deduction (K)"),max_length=255, null=True, blank=True)
# 	created = models.DateTimeField(auto_now_add=True)

# 	class Meta:
# 		ordering = ['-created']
# 		verbose_name = 'LOANPAYMENTSHARECONTRIBUTION'
# 		verbose_name_plural = 'LOANPAYMENTSHARECONTRIBUTIONS'

# 	def __unicode__(self):
# 		return self.period_repayment

# class OutStandingLoans(models.Model):

# 	# E. OUTSTANDING LOANS (to be filled by care coop loans officer)

# 	premium_loan_amount = models.CharField(_("Premium Loan Amount (K)"),max_length=255, null=True, blank=True)
# 	premium_balance = models.CharField(_("Premium Balance (K)"),max_length=255, null=True, blank=True)
# 	premium_monthly_repayment = models.CharField(_("Premium Monthly repayment (K)"),max_length=255, null=True, blank=True)

# 	ordinary_loan_amount = models.CharField(_("Ordinary Loan Amount (K)"),max_length=255, null=True, blank=True)
# 	ordinary_balance = models.CharField(_("Ordinary Balance (K)"),max_length=255, null=True, blank=True)
# 	ordinary_monthly_repayment = models.CharField(_("Ordinary Monthly repayment (K)"),max_length=255, null=True, blank=True)

# 	rental_plus_loan_amount = models.CharField(_("Rental Plus Loan Amount (K)"),max_length=255, null=True, blank=True)
# 	rental_plus_balance = models.CharField(_("Rental Plus Balance (K)"),max_length=255, null=True, blank=True)
# 	rental_plus_monthly_repayment = models.CharField(_("Rental Plus Monthly repayment (K)"),max_length=255, null=True, blank=True)

# 	education_loan_amount = models.CharField(_("Education Loan Amount (K)"),max_length=255, null=True, blank=True)
# 	education_balance = models.CharField(_("Education Balance (K)"),max_length=255, null=True, blank=True)
# 	education_monthly_repayment = models.CharField(_("Education Monthly repayment (K)"),max_length=255, null=True, blank=True)

# 	emergency_loan_amount = models.CharField(_("Emergeny Loan Amount (K)"),max_length=255, null=True, blank=True)
# 	emergency_balance = models.CharField(_("Emergeny Balance (K)"),max_length=255, null=True, blank=True)
# 	emergency_monthly_repayment = models.CharField(_("Emergeny Monthly repayment (K)"),max_length=255, null=True, blank=True) 

# 	family_holiday_loan_amount = models.CharField(_("Family Holiday Loan Amount (K)"),max_length=255, null=True, blank=True)
# 	family_holiday_balance = models.CharField(_("Family Holiday Balance (K)"),max_length=255, null=True, blank=True)
# 	family_holiday_monthly_repayment = models.CharField(_("Family Holiday Monthly repayment (K)"),max_length=255, null=True, blank=True)

# 	commodity_loan_amount = models.CharField(_("Commodity Loan Amount (K)"),max_length=255, null=True, blank=True)
# 	commodity_balance = models.CharField(_("Commodity Balance (K)"),max_length=255, null=True, blank=True)
# 	commodity_monthly_repayment = models.CharField(_("Commodity Monthly repayment (K)"),max_length=255, null=True, blank=True)

# 	building_loan_amount = models.CharField(_("Building Loan Amount (K)"),max_length=255, null=True, blank=True)
# 	building_balance = models.CharField(_("Building Balance (K)"),max_length=255, null=True, blank=True)
# 	building_monthly_repayment = models.CharField(_("Building Monthly repayment (K)"),max_length=255, null=True, blank=True)

# 	land_purchase_loan_amount = models.CharField(_("Land Purchase Loan Amount (K)"),max_length=255, null=True, blank=True)
# 	land_purchase_balance = models.CharField(_("Land Purchase Balance (K)"),max_length=255, null=True, blank=True)
# 	land_purchase_monthly_repayment = models.CharField(_("Land Purchase Monthly repayment (K)"),max_length=255, null=True, blank=True)

# 	care_coop_land_loan_amount = models.CharField(_("Care Coop Land Loan Amount (K)"),max_length=255, null=True, blank=True)
# 	care_coop_land_balance = models.CharField(_("Care Coop Land Balance (K)"),max_length=255, null=True, blank=True)
# 	care_coop_land_monthly_repayment = models.CharField(_("Care Coop Land Monthly repayment (K)"),max_length=255, null=True, blank=True)

# 	vehicle_loan_amount = models.CharField(_("Vehicle Loan Amount (K)"),max_length=255, null=True, blank=True)
# 	vehicle_balance = models.CharField(_("Vehicle Balance (K)"),max_length=255, null=True, blank=True)
# 	vehicle_monthly_repayment = models.CharField(_("Vehicle Monthly repayment (K)"),max_length=255, null=True, blank=True)

# 	vehicle_insurance_loan_amount = models.CharField(_("Vehicle Insurance Loan Amount (K)"),max_length=255, null=True, blank=True)
# 	vehicle_insurance_balance = models.CharField(_("Vehicle Insurance Balance (K)"),max_length=255, null=True, blank=True)
# 	vehicle_insurance_monthly_repayment = models.CharField(_("Vehicle Insurance Monthly repayment (K)"),max_length=255, null=True, blank=True)

# 	share_financing_loan_amount = models.CharField(_("Share Financing Loan Amount (K)"),max_length=255, null=True, blank=True)
# 	share_financing_balance = models.CharField(_("Share Financing Balance (K)"),max_length=255, null=True, blank=True)
# 	share_financing_monthly_repayment = models.CharField(_("Share Financing Monthly repayment (K)"),max_length=255, null=True, blank=True)

# 	home_improvement_loan_amount = models.CharField(_("Home Improvement Loan Amount (K)"),max_length=255, null=True, blank=True)
# 	home_improvement_balance = models.CharField(_("Home Improvement Balance (K)"),max_length=255, null=True, blank=True)
# 	home_improvement_monthly_repayment = models.CharField(_("Home Improvement Monthly repayment (K)"),max_length=255, null=True, blank=True)

# 	name_loans_officer = models.CharField(_("Name(loans officer)"),max_length=255, null=True, blank=True)
# 	signature = models.BooleanField(_("Signature"),default=False)
# 	text = models.TextField(_("Text"), null=True,blank=True)
# 	date = models.DateTimeField(auto_now_add=False)
# 	created = models.DateTimeField(auto_now_add=True)

# 	class Meta:
# 		ordering = ['-created']
# 		verbose_name = 'OUT STANDING LOAN'
# 		verbose_name_plural = 'OUT STANDING LOANS'

# 	def __unicode__(self):
# 		return self.premium_loan_amount

# class Security(models.Model):

# 	# F.SECURITY

# 	total_shares = models.CharField(_("1. Total Shares (K)"),max_length=255, null=True, blank=True)
# 	terminal_benefits_accured = models.CharField(_("2. Terminal Benefits Accrued (K)"),max_length=255, null=True, blank=True)
# 	total = models.CharField(_("3. Total (K)"),max_length=255, null=True, blank=True)
# 	signaturea = models.BooleanField(_("Signature"),default=False)
# 	signatureb = models.BooleanField(_("Signature"),default=False)
# 	datea = models.DateTimeField(auto_now_add=False)
# 	dateb = models.DateTimeField(auto_now_add=False)
# 	created = models.DateTimeField(auto_now_add=True)

# 	class Meta:
# 		ordering = ['-created']
# 		verbose_name = 'SECURITY'
# 		verbose_name_plural = 'SECURITIES'

# 	def __unicode__(self):
# 		return self.total_shares

# class Declaration(models.Model):

# 	# G. DECLARATION(to be filled by applicant)
# 	applicant_name = models.CharField(_("Applicant name"),max_length=255, null=True, blank=True)
# 	datea = models.DateTimeField(auto_now_add=False)
# 	signature = models.BooleanField(_("Signature"),default=False)
# 	dateb = models.DateTimeField(auto_now_add=False)
# 	bank_name = models.CharField(_("Bank Name"),max_length=255, null=True, blank=True)
# 	account_no = models.CharField(_("Account No"),max_length=255, null=True, blank=True)
# 	branch = models.CharField(_("Branch"),max_length=255, null=True, blank=True)
# 	cheque = models.BooleanField(_("Signature"),default=False)
# 	bank_transfer = models.BooleanField(_("Signature"),default=False)
# 	created = models.DateTimeField(auto_now_add=True)

# 	class Meta:
# 		ordering = ['-created']
# 		verbose_name = 'DECLARATION'
# 		verbose_name_plural = 'DECLARATIONS'

# 	def __unicode__(self):
# 		return self.applicant_name

# class ReviewedByCoOperativeManager(models.Model):

# 	# H.REVIEWED BY COOPERATE GENERAL MANAGER/FINANCE CORDINATOR

# 	name = models.CharField(_("NAME"),max_length=255, null=True, blank=True)
# 	date = models.DateTimeField(auto_now_add=False)
# 	signature = models.BooleanField(_("Signature"),default=False)
# 	created = models.DateTimeField(auto_now_add=True)

# 	class Meta:
# 		ordering = ['-created']
# 		verbose_name = 'REVIEWED BY CO OPERATIVE MANAGER'
# 		verbose_name_plural = 'REVIEWED BY CO OPERATIVE MANAGERS'

# 	def __unicode__(self):
# 		return self.name

# class LoanAnalysisAndApprovalByLoans(models.Model):

# 	# I. LOAN ANALYSIS AND APPROVAL BY LOANS COMMITTEEE
# 	comments = models.TextField(_("Comments"), null=True,blank=True)

# 	chair_person_name = models.CharField(_("Chair Person Name"),max_length=255, null=True, blank=True)
# 	chair_person_signature = models.CharField(_("Chair Person Sign"),max_length=255, null=True, blank=True)
# 	chair_person_date = models.DateTimeField(auto_now_add=False)

# 	Treasurer_name = models.CharField(_("Treasurer Name"),max_length=255, null=True, blank=True)
# 	Treasurer_signature = models.CharField(_("Treasurer Sign"),max_length=255, null=True, blank=True)
# 	Treasurer_date = models.CharField(_("Treasurer Date"),max_length=255, null=True, blank=True)

# 	committee_member_name = models.CharField(_("Committee Member Name"),max_length=255, null=True, blank=True)
# 	committee_member_signature = models.CharField(_("Committee Member Sign"),max_length=255, null=True, blank=True)
# 	committee_member_date = models.CharField(_("Committee Member Date"),max_length=255, null=True, blank=True)
# 	created = models.DateTimeField(auto_now_add=True)

# 	class Meta:
# 		ordering = ['-created']
# 		verbose_name = 'LOAN ANALYSIS AND APPROVAL BY LOAN'
# 		verbose_name_plural = 'LOAN ANALYSIS AND APPROVAL BY LOANS'

# 	def __unicode__(self):
# 		return self.comments

# class NameSignatureDate(models.Model):

# 	# J. BOARD RESOLUTION (Applicable to loans of above K10000)

# 	name = models.CharField(_("Name"),max_length=255, null=True, blank=True)
# 	signature = models.CharField(_("Signature"),max_length=255, null=True, blank=True)
# 	date = models.CharField(_("Date"),max_length=255, null=True, blank=True)
# 	created = models.DateTimeField(auto_now_add=True)


# 	class Meta:
# 		ordering = ['-created']
# 		verbose_name = 'NAME SIGNATURE DATE'
# 		verbose_name_plural = 'NAME SIGNATURE DATES'

# 	def __unicode__(self):
# 		return self.name

# class SuccessStories(models.Model):
#
# 	message = models.TextField(null=True, blank=True)
# 	name = models.CharField(_('Name of Member'),max_length=255, null=True, blank=True)
# 	carecoopnumber = models.CharField(_('CareCoop Number'),max_legnth=255, null=True, blank=True)
#
# 	#Start contact numbers
# 	home = models.CharField(_('Home'),max_length=255, null=True, blank=True)
# 	cell = models.CharField(_('Cell'),max_length=255, null=True, blank=True)
# 	work = models.CharField(_('Work'),max_length=255, null=True, blank=True)
#
# 	#End contact numbers
# 	#Direct debit mandate Start
# 	barclays = models.BooleanField(_('Barclays Bank Zambia Plc'))
# 	firstalliance = models.BooleanField(_('First Alliance Bank Ltd'))
# 	stanbic = models.BooleanField(_('Stanbic Bank (Z) Ltd'))
# 	cavmont = models.BooleanField(_('Cavmont Capital Bank Ltd'))
# 	indo = models.BooleanField(_('Indo Bank Zambia Ltd'))
# 	standard = models.BooleanField(_('Standard Chartered Bank Plc'))
# 	investtrust = models.BooleanField(_('Investrust Mechant Bank Plc'))
# 	zanaco = models.BooleanField(_('Zambia National Commercial Bank Plc'))
# 	finance = models.BooleanField(_('Finance Bank (Z) Ltd'))
# 	citybank = models.BooleanField(_('Citybank (Z) Ltd'))
# 	others = models.BooleanField(_('Others'),max_length=255, null=True, blank=True)
#
# 	#Direct debit mandate end
# 	tomanager = models.BooleanField(_('To The Manager:'),max_length=255, null=True, blank=True)
# 	bankaddress = models.BooleanField(_('Address'),max_length=255, null=True, blank=True)
# 	postcode = models.BooleanField(_('Post Code'),max_length=255, null=True, blank=True)
# 	bankshortcode = models.BooleanField(_('Bank Short Code'),max_length=255, null=True, blank=True)
# 	accnumber = models.BooleanField(_('Account Number'),max_length=255, null=True, blank=True)
# 	amount = models.BooleanField(_('Amount K:'),max_length=50, null=True, blank=True)
# 	effect = models.DateTimeField(auto_now_add=False)
# 	payday = models.DateTimeField(auto_now_add=False)
#
# 	class meta:
# 			ordering = ['-created']
# 			verbose_name = ('Approval Form')
# 			verbose_name_plural = ('Approval Forms')
#
# 	def __unicode__(self):
# 			return self.carecoopnumber