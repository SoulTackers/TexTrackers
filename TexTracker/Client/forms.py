from django import forms
from crispy_forms.helper import FormHelper
from .models import (AccountType,
                    Client,
                    ClientAccountantInfo,
                    ClientBankInfo,
                    ClientLegalInfo,
                    ClientPassword,
                    Services,)

class AccountTypeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
    class Meta:
        model = AccountType
        fields = [
            'account_type_name',
            'account_type_details',
        ]

class ClientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
    class Meta:
        model = Client
        fields = [
            'client_name',
            ######## selection #########
            'client_account_type',
            ############################
            'client_office_address1',
            'client_office_address2',
            'client_office_pin',
            ######## phone #########
            'client_phone',
            ########################
            'client_email',
            'client_service_id',
            ######## selection #########
            'client_type_of_dealer',
            ############################
        ]

class ClientBankInfoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
    class Meta:
        model = ClientBankInfo
        fields = [
            'client_bank_info_bank_name',
            'client_bank_info_account_no',
            'client_bank_info_branch',
        ]

class ClientAccountantInfoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
    class Meta:
        model = ClientAccountantInfo
        fields = [
            'client_acc_info_accountant_name',
            'client_acc_info_accountant_phone',
            'client_acc_info_accountant_email',
            'client_acc_info_accountant_counsultant_name',
            'client_acc_info_accountant_counsultant_phone',
            'client_acc_info_accountant_counsultant_email',
            'client_acc_info_ca_name',
            'client_acc_info_ca_phone',
            'client_acc_info_ca_email',
        ]

class ClientLegalInfoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
    class Meta:
        model = ClientLegalInfo
        fields = [
            'client_leg_info_date_of_incorporation',
            'client_leg_info_st_file_no',
            'client_leg_info_it_file_no',
            'client_leg_info_tds_file_no',
            'client_leg_info_vat_file_no',
            'client_leg_info_vat_audit_file_no',
            'client_leg_info_exercise_file_no',
            'client_leg_info_vat_tin_no',
            'client_leg_info_date1',
            'client_leg_info_cst_tin_no',
            'client_leg_info_date2',
            'client_leg_info_service_tax_no',
            'client_leg_info_date3',
            'client_leg_info_ecc_no',
            'client_leg_info_date4',
            'client_leg_info_pancard_no',
            'client_leg_info_tds_no',
            'client_leg_info_firm_registration',
            'client_leg_info_iec_no',
            'client_leg_info_elect_no',
            'client_leg_info_pte1',
            'client_leg_info_pte2',
        ]

class ClientPasswordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
    class Meta:
        model = ClientPassword
        fields = [
            'client_password_vat',
            'client_password_it',
            'client_passwordclient_password_tds',
            'client_password_st',
            'client_password_excise',
            'client_password_vat_unique_id',

        ]


class ServicesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
    class Meta:
            model = Services
            fields = [
                'service_name',
                'service_details',
            ]